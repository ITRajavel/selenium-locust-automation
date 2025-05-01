import subprocess
from generate_locust_code import generate_locust_script

# Choose your demo website
host_url = "https://fakestoreapi.com"

# Step 1: Generate test file
generate_locust_script(host_url)

# Step 2: Run the load test
subprocess.run([
    "locust",
    "-f", "locustfile.py",
    "--host", host_url,
    "--headless",
    "-u", "10",         # total users
    "-r", "2",          # spawn rate (users/sec)
    "--run-time", "1m", # total time
    "--html", "report.html"
])

print("✅ Test completed. Open report.html to view results.")
