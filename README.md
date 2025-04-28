# 🧪 Automated Selenium Regression & Load Testing using Streamlit + GROQ API

A complete automation framework for:

- ✅ **Automated UI Regression Testing** (Selenium + PyTest)
- ✅ **Autonomous Load Testing** (Locust)
- ✅ **Streamlit-based Frontend** for easy test case generation
- ✅ **GROQ LLM API** integration (LLaMA 3.1 8B) for smart code generation
- ✅ **CI/CD Workflow** (GitHub Actions)

---

## 🚀 Features

- **Streamlit UI** to generate Selenium test cases dynamically
- **Automatic HTML Form Extraction** from pages
- **Prompt Engineering** for clean and stable PyTest code generation
- **Locust-based Load Testing** with auto-generated `locustfile.py`
- **Configurable settings** (ChromeDriver path, API keys)
- **Headless browser execution** for speed
- **HTML Reports** for Load Tests
- **CI/CD Pipeline** to test on every push/pull request

---

## 📁 Project Structure

```bash
selenium-locust-automation/
├── app.py                   # Streamlit UI to generate test cases
├── run_test.py               # Load testing entry point
├── form_extractor.py         # Extracts forms and elements
├── test_case_generator.py    # Interacts with GROQ API to generate PyTest code
├── generate_locust_code.py   # Generates locustfile.py dynamically
├── requirements.txt          # Python dependencies
├── Dockerfile                # (Optional) Docker containerization
├── config.json               # API Key storage
├── conftest.py               # Selenium WebDriver fixture for PyTest
├── .github/
│   └── workflows/
│       └── ci-cd.yml         # GitHub Actions CI/CD workflow
└── README.md                 # Project documentation (this file)
⚙️ Installation & Setup
Clone the repository

bash
Copy code
git clone https://github.com/YOUR_USERNAME/selenium-locust-automation.git
cd selenium-locust-automation
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set your API Key

Update the config.json file:

json
Copy code
{
  "api_key": "your-groq-api-key"
}
Run the Streamlit app

bash
Copy code
streamlit run app.py
Run Load Testing

bash
Copy code
python run_test.py
🧠 How it Works
Automated Regression Testing (Streamlit)
Enter URL, login details, navigation flow

App extracts all HTML form elements

GROQ LLM generates stable Selenium + PyTest code

Code is displayed and can be downloaded

Autonomous Load Testing (Locust)
App generates locustfile.py dynamically using GROQ

Targets endpoints like /, /products, /products/1

Runs load test with 10 users, spawn rate 2 users/sec, for 1 min

Outputs report.html after load test

🛠️ CI/CD Pipeline (GitHub Actions)
On Push / Pull Request:

Setup Python

Install dependencies

Test run Streamlit app (headless)

Run Load Testing script

Automatic pass/fail badge visible in GitHub Actions tab.

📦 Docker (Optional)
To run the app in a container:

bash
Copy code
docker build -t selenium-locust-automation .
docker run -p 8501:8501 selenium-locust-automation
📋 TODOs / Improvements
 Add better error handling for API failures

 Add Slack/email notifications for CI/CD results

 Deploy Streamlit app to Streamlit Cloud / AWS / Azure

🙌 Acknowledgements
GROQ LLM API

Streamlit

Locust

Selenium

PyTest

📢 License
This project is licensed under the MIT License.

🌟 Show your support
If you like this project, please ⭐ star the repo and share it with others!

ruby
Copy code

---

# 🧹 Quick Checklist for README:

| Section             | Status |
|:--------------------|:-------|
| Title + Overview     | ✅ |
| Features             | ✅ |
| Project Structure    | ✅ |
| Installation Steps   | ✅ |
| How it Works         | ✅ |
| CI/CD Pipeline Info  | ✅ |
| Docker Info          | ✅ |
| TODOs                | ✅ |
| Acknowledgements     | ✅ |
| License              | ✅ |

---

# ⚡ Next Step for you:

- Copy this `README.md` into your project root.
- Add small changes if needed (like project name, your GitHub username).
- Then do:

```bash
git add README.md
git commit -m "Added professional README"
git push
