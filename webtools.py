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

def tool_selection_menu():
    print(f"{OKGREEN}--- Vulnerability Type Selection ---{ENDC}")
    tools = [
        "SQL Injection Check",
        "XSS Check",
        "LFI Check",
        "CSRF Check",
        "Admin Page Search",
        "Directory Traversal Check",
        "Subdomain Enumeration",
        "Open Redirect Check",
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
            print(f"{OKGREEN}Performing SQL Injection Check on {url}...{ENDC}")
            subprocess.call(["sqlmap", "-u", url, "--batch"])
        elif choice == "2":
            url = input("Enter target URL for XSS Check: ")
            print(f"{OKGREEN}Performing XSS Check on {url}...{ENDC}")
            # Add XSS check logic here
        elif choice == "3":
            url = input("Enter target URL for LFI Check: ")
            print(f"{OKGREEN}Performing LFI Check on {url}...{ENDC}")
            # Add LFI check logic here
        elif choice == "4":
            url = input("Enter target URL for CSRF Check: ")
            print(f"{OKGREEN}Performing CSRF Check on {url}...{ENDC}")
            # Add CSRF check logic here
        elif choice == "5":
            url = input("Enter target URL for Admin Page Search: ")
            print(f"{OKGREEN}Searching for Admin Pages on {url}...{ENDC}")
            # Add admin page search logic here
        elif choice == "6":
            url = input("Enter target URL for Directory Traversal Check: ")
            print(f"{OKGREEN}Performing Directory Traversal Check on {url}...{ENDC}")
            # Add Directory Traversal check logic here
        elif choice == "7":
            url = input("Enter target URL for Subdomain Enumeration: ")
            print(f"{OKGREEN}Performing Subdomain Enumeration on {url}...{ENDC}")
            # Add Subdomain Enumeration logic here
        elif choice == "8":
            url = input("Enter target URL for Open Redirect Check: ")
            print(f"{OKGREEN}Performing Open Redirect Check on {url}...{ENDC}")
            # Add Open Redirect check logic here
        elif choice == "9":
            print(f"{OKBLUE}Exiting the tool. Goodbye!{ENDC}")
            break
        else:
            print(f"{FAIL}Invalid choice. Please enter a number from 1 to 9.{ENDC}")

if __name__ == "__main__":
    main()
