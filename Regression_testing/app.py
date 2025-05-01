import streamlit as st
import json
import os
from form_extractor import extract_all_elements
from test_case_generator import generate_prompt, generate_test_case

st.set_page_config(page_title="🧪 Selenium Test Generator")

# Load API key configuration (your preferred style)
config = json.load(open("config.json"))
os.environ["GROQ_API_KEY"] = config["GROQ_API_KEY"]

st.title("🔧 Selenium + Pytest Test Case Generator")

# Input Fields
driver_path = st.text_input(
    "Chromedriver Path",
    value="C:/Users/RAJAVEL/Desktop/virtusa4/selenium_tests/chromedriver-win64/chromedriver.exe"
)
url = st.text_input("Page URL", placeholder="https://example.com")
username = st.text_input("Username (if login required)", value="", key="username")
password = st.text_input("Password (if login required)", type="password", key="password")
test_flow = st.text_input("Test Flow (e.g., 'Login → Inventory → Cart → Checkout → Logout')")
test_type = st.text_input("Test Scenario Description (e.g., 'Complete purchase flow')")
conditions = st.text_area("Additional Test Conditions (Optional)")

if st.button("Generate Test Case"):
    if not url or not driver_path or not test_flow:
        st.warning("Please provide the URL, Chromedriver path, and test flow sequence.")
    else:
        with st.spinner("🔍 Logging in (if needed) and extracting page elements..."):
            # Initialize the list to store test steps for each page
            all_fields = []
            flow_pages = test_flow.split("→")  # Split the test flow into pages
            
            for page in flow_pages:
                page = page.strip()  # Clean any extra spaces
                page_url = f"{url}/{page.lower().replace(' ', '_')}"  # Form a URL from the page name (you can adjust the logic here)
                
                fields = extract_all_elements(page_url, driver_path, username=username, password=password)

                if not fields:
                    st.error(f"❌ No elements found on the {page} page.")
                    break
                else:
                    all_fields.append({"page": page, "fields": fields})
            
            if all_fields:
                # Generate the complete test case
                prompt = generate_prompt(test_type, all_fields, url, conditions)
                code = generate_test_case(prompt)

                st.success("✅ Test case generated successfully!")
                st.code(code, language="python")

                # Save the test case to a file and allow download
                os.makedirs("output", exist_ok=True)
                with open("output/selenium_test_case.py", "w") as f:
                    f.write(code)
                with open("output/selenium_test_case.py", "rb") as f:
                    st.download_button("📥 Download Test Case", f, file_name="selenium_test_case.py")
