import hashlib

filename = input("Enter the file name: ")

try:
    with open(filename, "rb") as file:
        data = file.read()

    md5_hash = hashlib.md5(data).hexdigest()
    sha256_hash = hashlib.sha256(data).hexdigest()

    print("\nCurrent MD5:")
    print(md5_hash)

    print("\nCurrent SHA-256:")
    print(sha256_hash)

    original_hash = input("\nEnter the original SHA-256 hash: ").strip()

    if sha256_hash == original_hash:
        print("\nRESULT: File is unchanged.")
        print("Integrity check PASSED.")
    else:
        print("\nRESULT: File has been modified.")
        print("Integrity check FAILED.")

except FileNotFoundError:
    print("File not found. Please check the file name.")