#!/usr/bin/env python3

import crypt
import getpass

# Configuration
RETRY_LIMIT = 3

# Data in /etc/passwd and /etc/shadow
USER_NAME = "cliff"
HASH_TYPE_ID = "6"  # SHA-512
SALT = "iB6z.Wi1AdARgNKi"
ENCRYPTED_PASSWORD = "VyBMc4pjbFtTbLQluqxSNUJZ0TGbD6VJHN8GYXHs06TP/xzCXxWT19tBHvRxUcF4N4nZsZXgmyVkQSOEVlkqV."

# Input user name
user = input("login as: ")
salt = ""
auth = ""
if user == USER_NAME:
    # `salt` may be one of the `crypt.METHOD_*` values, or a string as returned by `crypt.mksalt()`
    salt = f"${HASH_TYPE_ID}${SALT}"
    auth = f"{salt}${ENCRYPTED_PASSWORD}"
print(f"[Debug] {auth}")

# Authentication
for i in range(RETRY_LIMIT):
    # Input password
    password = getpass.getpass(f"{user}'s password: ")
    result = crypt.crypt(password, salt)
    print(f"[Debug] {result}")
    if result == auth:
        print("Access granted")
        break
    else:
        print("Access denied")
