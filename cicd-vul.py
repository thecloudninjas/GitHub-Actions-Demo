import subprocess
import sys
from pathlib import Path

requirements = """requests==2.19.1
Django==2.2.9
PyYAML==5.1
jinja2==2.10.1
pillow==6.2.1
urllib3==1.24.1
cryptography==2.3
flask==0.12.2
markdown==2.6.8
"""

def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        sys.exit(1)

def main():
    req_file = Path("requirements.txt")

    print("Creating requirements.txt...")
    req_file.write_text(requirements)

    print("Upgrading pip...")
    run_command([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

    print("Installing dependencies...")
    run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    print("Hello, world!")

if __name__ == "__main__":
    main()
