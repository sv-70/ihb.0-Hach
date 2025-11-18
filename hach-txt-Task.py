
import sys
import binascii
import hashlib

# -----------------------------------------
# Detect hash type based on length
# -----------------------------------------
def detect_hash_type(hash_str):
    length = len(hash_str)

    hash_types = {
        32: "MD5",
        40: "SHA1",
        64: "SHA256",
        96: "SHA384",
        128: "SHA512"
    }

    return hash_types.get(length, None)


# -----------------------------------------
# Check if valid hex string
# -----------------------------------------
def is_valid_hex(s):
    try:
        binascii.unhexlify(s)
        return True
    except Exception:
        return False


# -----------------------------------------
# Generate MD5 for plaintext
# -----------------------------------------
def generate_md5(plaintext):
    return hashlib.md5(plaintext.encode()).hexdigest()


# -----------------------------------------
# Interactive menu mode
# -----------------------------------------
def interactive_mode():
    while True:
        print("""
	$$\ $$\       $$\           $$$$$$\          $$\   $$\                     $$\       
	\__|$$ |      $$ |         $$$ __$$\         $$ |  $$ |                    $$ |      
	$$\ $$$$$$$\  $$$$$$$\     $$$$\ $$ |        $$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$$\  
	$$ |$$  __$$\ $$  __$$\    $$\$$\$$ |$$$$$$\ $$$$$$$$ | \____$$\ $$  _____|$$  __$$\ 
	$$ |$$ |  $$ |$$ |  $$ |   $$ \$$$$ |\______|$$  __$$ | $$$$$$$ |$$ /      $$ |  $$ |
	$$ |$$ |  $$ |$$ |  $$ |   $$ |\$$$ |        $$ |  $$ |$$  __$$ |$$ |      $$ |  $$ |
	$$ |$$$$$$$  |$$ |  $$ |$$\\$$$$$$  /        $$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |
	\__|\_______/ \__|  \__|\__|\______/         \__|  \__| \_______| \_______|\__|  \__|""")
        print("\n========== Hash Utility ==========")
        print("1) Detect hash type")
        print("2) Generate MD5 from plaintext")
        print("3) Exit")
        print("===================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            h = input("Enter hash string: ").strip().lower()

            if not is_valid_hex(h):
                print("\n[!] Invalid hex string. Only characters 0-9 and a-f are allowed.")
                continue

            hash_type = detect_hash_type(h)
            if hash_type:
                print(f"\nDetected hash type: {hash_type}")
            else:
                print("\nUnknown hash type")

        elif choice == "2":
            plaintext = input("Enter plaintext: ").strip()
            md5_value = generate_md5(plaintext)
            print(f"\nMD5: {md5_value}")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("\n[!] Invalid option, try again.")


# -----------------------------------------
# CLI argument mode
# -----------------------------------------
def cli_mode(hash_str):

    hash_str = hash_str.lower()

    if not is_valid_hex(hash_str):
        print("Invalid hex string.")
        return

    hash_type = detect_hash_type(hash_str)
    if hash_type:
        print(f"Detected hash type: {hash_type}")
    else:
        print("Unknown hash type")


# -----------------------------------------
# Main entry
# -----------------------------------------
if __name__ == "__main__":

    # Help message
    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 hash_task1.py <hash>")
        sys.exit()

    if len(sys.argv) == 2:
        # CLI mode
        cli_mode(sys.argv[1])
    else:
        # Interactive mode
        interactive_mode()
