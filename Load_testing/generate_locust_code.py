import json
import re
from groq import Groq

def get_api_key():
    with open("config.json", "r") as f:
        return json.load(f)["GROQ_API_KEY"]

def extract_python_code(text):
    # Extracts the code block from markdown response
    matches = re.findall(r"```python(.*?)```", text, re.DOTALL)
    if matches:
        return matches[0].strip()
    else:
        # fallback: remove any line starting with non-python
        lines = text.splitlines()
        python_lines = [line for line in lines if not line.strip().lower().startswith("here is")]
        return "\n".join(python_lines).strip()

def generate_locust_script(endpoint_base):
    client = Groq(api_key=get_api_key())

    prompt = f"""
    Generate only valid Python code. Create a class-based Locust test for endpoints:
    - /
    - /products
    - /products/1
    Base URL: {endpoint_base}
    Use HttpUser, task, and between for wait_time.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_content = response.choices[0].message.content
    code = extract_python_code(raw_content)

    with open("locustfile.py", "w") as f:
        f.write(code)

    print("✅ Clean Locustfile generated successfully!")
