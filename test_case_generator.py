import os
from groq import Groq

def generate_prompt(test_type, fields, url, additional):
    prompt_lines = [
        f"Generate a robust Pytest + Selenium automation script for a **{test_type.lower()}** web form located at: {url}",
        "",
        "### Form Fields Found on the Page:"
    ]

    for i, field in enumerate(fields, start=1):
        # Safely access field label and type
        label = field.get("label") or field.get("name") or field.get("id") or "Unnamed Field"
        field_type = field.get("type") or field.get("tag") or "Unknown Type"  # Safe fallback
        prompt_lines.append(f"{i}. **{label}** ({field_type})")

    prompt_lines.append("")
    prompt_lines.append("### Additional Testing Instructions / Conditions:")
    prompt_lines.append(additional if additional else "None provided.")

    if "login" in test_type.lower() or "username" in additional.lower() or "password" in additional.lower():
        prompt_lines.append("\n### Note:")
        prompt_lines.append("If the form requires login, include logic to enter username and password and submit the form.")

    return "\n".join(prompt_lines)


def generate_test_case(prompt):
    try:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Python expert that generates Pytest + Selenium test scriptswith Launch Chrome browser and  without base class. "
                        "Your code must be clean, modular, and include necessary imports and explanations as comments."
                        "use assert verification"
                        "extract element with ID only"
                        "write test case based on what are the elemnts present in the page"
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"# ❌ Error generating test case:\n# {str(e)}"
