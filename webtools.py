import requests
import subprocess
import sys
import platform
import os
import shutil

# معلومات المبرمج
programmer_name = "Ayham Alwdy"
programmer_github = "https://github.com/ayhamalwdy2024/webtools-"
programmer_email = "ayhamalwdy2024@gmail.com"

# ألوان النصوص
HEADER_COLOR = "\033[95m"
OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"

def print_header():
    print(f"{HEADER_COLOR}--- Web Vulnerability Scanner ---{ENDC}")
    print(f"{OKBLUE}Programmer: {programmer_name}{ENDC}")
    print(f"{OKBLUE}GitHub: {programmer_github}{ENDC}")
    print(f"{OKBLUE}Email: {programmer_email}{ENDC}")
    print("-" * 50)

def install_required_libraries():
    print(f"{OKBLUE}[INFO] Checking and installing required libraries...{ENDC}")
    try:
        import requests
    except ImportError:
        print(f"{WARNING}[INFO] Installing 'requests' library...{ENDC}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    tools = {
        "nmap": "sudo apt install -y nmap" if platform.system().lower() != "android" else "pkg install -y nmap",
        "sqlmap": "sudo apt install -y sqlmap" if platform.system().lower() != "android" else "pkg install -y sqlmap",
    }
    for tool, install_command in tools.items():
        if not shutil.which(tool):
            print(f"{WARNING}[INFO] {tool} is not installed. Installing...{ENDC}")
            os.system(install_command)

def sql_injection_check(url):
    print(f"{OKBLUE}[INFO] Checking for SQL Injection on {url}{ENDC}")
    try:
        subprocess.call(["sqlmap", "-u", url, "--batch"])
    except Exception as e:
        print(f"{FAIL}[ERROR] {e}{ENDC}")

def xss_check(url):
    print(f"{OKBLUE}[INFO] Checking for XSS on {url}{ENDC}")
    payload = "<script>alert('XSS')</script>"
    try:
        response = requests.get(url, params={"q": payload})
        if payload in response.text:
            print(f"{FAIL}[VULNERABLE] XSS Detected!{ENDC}")
        else:
            print(f"{OKGREEN}[SAFE] No XSS vulnerability detected.{ENDC}")
    except requests.RequestException as e:
        print(f"{FAIL}[ERROR] {e}{ENDC}")

def lfi_check(url):
    print(f"{OKBLUE}[INFO] Checking for LFI on {url}{ENDC}")
    payloads = ["../../../../etc/passwd", "../etc/passwd"]
    for payload in payloads:
        full_url = f"{url}/{payload}"
        try:
            response = requests.get(full_url)
            if "root:x" in response.text:
                print(f"{FAIL}[VULNERABLE] LFI Detected with payload: {payload}{ENDC}")
                return
            else:
                print(f"{OKGREEN}[SAFE] No LFI with payload: {payload}{ENDC}")
        except requests.RequestException as e:
            print(f"{FAIL}[ERROR] {e}{ENDC}")

def admin_page_search(url):
    print(f"{OKBLUE}[INFO] Searching for Admin Pages on {url}{ENDC}")
    paths = [
        "admin/", "admin/login/", "administrator/", "adminpanel/", "login/", "controlpanel/",
        "wp-admin/", "wp-login.php", "admin.php", "user/login", "dashboard/", "cms/", "manage/",
        "admin_area/", "admin1/", "admin2/", "admin3/", "admincontrol/", "backend/", "memberadmin/"
    ]
    for path in paths:
        full_url = f"{url.rstrip('/')}/{path}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"{OKGREEN}[FOUND] Admin page found: {full_url}{ENDC}")
            else:
                print(f"{WARNING}[NOT FOUND] Tried: {full_url}{ENDC}")
        except requests.RequestException as e:
            print(f"{FAIL}[ERROR] {e}{ENDC}")

def tool_selection_menu():
    print(f"{OKGREEN}--- Vulnerability Type Selection ---{ENDC}")
    tools = [
        "SQL Injection Check",
        "XSS Check",
        "LFI Check",
        "Admin Page Search",
        "Exit",
    ]
    for index, tool in enumerate(tools, 1):
        print(f"{OKBLUE}{index}. {tool}{ENDC}")
    choice = input(f"{HEADER_COLOR}Enter the number of your choice: {ENDC}")
    return choice

def main():
    install_required_libraries()
    print_header()

    while True:
        choice = tool_selection_menu()
        if choice == "1":
            url = input("Enter target URL for SQL Injection Check: ")
            sql_injection_check(url)
        elif choice == "2":
            url = input("Enter target URL for XSS Check: ")
            xss_check(url)
        elif choice == "3":
            url = input("Enter target URL for LFI Check: ")
            lfi_check(url)
        elif choice == "4":
            url = input("Enter target URL for Admin Page Search: ")
            admin_page_search(url)
        elif choice == "5":
            print(f"{OKBLUE}Exiting the tool. Goodbye!{ENDC}")
            break
        else:
            print(f"{FAIL}Invalid choice. Please enter a number from 1 to 5.{ENDC}")

if __name__ == "__main__":
    main()
