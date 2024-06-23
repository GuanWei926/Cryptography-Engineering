import hashlib
import requests
from datetime import datetime


# Function to load password list from URL
def load_password_list(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print("Failed to download the password list.")
        return None


# Function to break SHA1 hash using password list
def break_sha1_hash(hash_to_break, password_list):
    start_time = datetime.now()
    attempts = 0
    for password in password_list:
        attempts += 1
        hashed_password = hashlib.sha1(password.encode()).hexdigest()
        if hashed_password == hash_to_break:
            end_time = datetime.now()
            time_taken = end_time - start_time
            time_taken_str = str(time_taken.total_seconds())
            print(f"Hash: {hash_to_break}")
            print(f"Password: {password}")
            print(
                f"Took {attempts} attempts to crack input hash. Time Taken: {time_taken_str}",
            )
            return
    print("Unable to crack the hash with the given password list.")


# Function to break SHA1 hash using password list to find salt
def find_salt(hash_to_break, password_list):
    for password in password_list:
        hashed_password = hashlib.sha1(password.encode()).hexdigest()
        if hashed_password == hash_to_break:
            return password
    print("Unable to crack the hash with the given password list.")


# Function to break SHA1 hash (with salt) using password list
def break_sha1_hash_with_salt(hash_to_break, password_list, salt):
    start_time = datetime.now()
    attempts = 0
    for password in password_list:
        attempts += 1
        hashed_password = hashlib.sha1((salt + password).encode()).hexdigest()
        if hashed_password == hash_to_break:
            end_time = datetime.now()
            time_taken = end_time - start_time
            time_taken_str = str(time_taken.total_seconds())
            print(f"Hash: {hash_to_break}")
            print(f"Password: {password}")
            print(
                f"Took {attempts} attempts to crack input hash. Time Taken: {time_taken_str}"
            )
            return
    print("Unable to crack the hash with the given password list.")


"""
# Function to break SHA1 hash (Leave a space between the two sets of password) using password list
def break_sha1_hash_concatenated(hash_to_break, password_list):
    start_time = datetime.now()
    attempts = 0
    for password1 in password_list:
        for password2 in password_list:
            attempts += 1
            password = password1 + " " + password2
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            if hashed_password == hash_to_break:
                end_time = datetime.now()
                time_taken = end_time - start_time
                time_taken_str = str(time_taken.total_seconds())
                print(f"Hash: {hash_to_break}")
                print(f"Password: {password}")
                print(
                    f"Took {attempts} attempts to crack input hash. Time Taken: {time_taken_str}"
                )
                return
    print("Unable to crack the hash with the given password list.")
"""

# Load password list
password_list_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
password_list = load_password_list(password_list_url)
if password_list:
    print("Easy hash:")
    # SHA1 hash to break
    hash_to_break = "ef0ebbb77298e1fbd81f756a4efc35b977c93dae"
    # Break the SHA1 hash
    break_sha1_hash(hash_to_break, password_list)
    print("")

    print("medium hash:")
    hash_to_break = "0bc2f4f2e1f8944866c2e952a5b59acabd1cebf2"
    break_sha1_hash(hash_to_break, password_list)
    print("")

    print("Leet hacker hash:")
    hash_salt = "dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06"
    salt = find_salt(hash_salt, password_list)
    print("salt: %s" % salt)
    hash_to_break = "9d6b628c1f81b4795c0266c0f12123c1e09a7ad3"
    break_sha1_hash_with_salt(hash_to_break, password_list, salt)
    print("")

"""
    print("Extra Credit:")
    hash_to_break = "44ac8049dd677cb5bc0ee2aac622a0f42838b34d"
    break_sha1_hash_concatenated(hash_to_break, password_list)
    print("")
"""
