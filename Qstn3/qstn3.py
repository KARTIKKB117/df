# Create a program to generate and compare file hashes using algorithms
# like MD5 and SHA-256

import hashlib

filename = input("Enter the file name: ")

try:
    with open(filename, "rb") as file:
        data = file.read()

    md5_hash = hashlib.md5(data).hexdigest()

    sha256_hash = hashlib.sha256(data).hexdigest()

    print("\nMD5 Hash:")
    print(md5_hash)

    print("\nSHA-256 Hash:")
    print(sha256_hash)

except FileNotFoundError:
    print("File not found. Please check the file name.")

# TEXT DOCUMENT
# evidence.txt
# This is my digital evidence file
# Modified txt :
# This is my modified digital evidence file

# ACTUAL COMPARISON

# import hashlib

# filename = input("Enter the file name: ")

# try:
#     with open(filename, "rb") as file:
#         data = file.read()

#     md5_hash = hashlib.md5(data).hexdigest()
#     sha256_hash = hashlib.sha256(data).hexdigest()

#     print("\nCurrent MD5:")
#     print(md5_hash)

#     print("\nCurrent SHA-256:")
#     print(sha256_hash)

#     original_hash = input("\nEnter the original SHA-256 hash: ").strip()

#     if sha256_hash == original_hash:
#         print("\nRESULT: File is unchanged.")
#         print("Integrity check PASSED.")
#     else:
#         print("\nRESULT: File has been modified.")
#         print("Integrity check FAILED.")

# except FileNotFoundError:
#     print("File not found. Please check the file name.")

# Fo - Qstn3
#     F-evidence.txt
#     F-Modified.txt
#     F-qstn3.py
#     F-qstn3_2.py

# cd Qstn3
# python qstn3.py

# PS C:\Users\Kunal\OneDrive\Documents\DF exam\Qstn3> python qstn3.py
# Enter the file name: evidence.txt

# SHA-256 Hash:
# 1167c687df06a07c96120ed99fd23ab8a03dddb16852216832c77af1d8f942b0
# PS C:\Users\Kunal\OneDrive\Documents\DF exam\Qstn3> python qstn3_2.py
# Enter the file name: Modified.txt

# Current MD5:
# adc34059dcef187d570830e8058060e5

# Current SHA-256:
# 3e2b4bc23d2b45e627224151ce6ad895f2bff402a72b5e05936faf9f56cb525e

# Enter the original SHA-256 hash: 1167c687df06a07c96120ed99fd23ab8a03dddb16852216832c77af1d8f942b0






