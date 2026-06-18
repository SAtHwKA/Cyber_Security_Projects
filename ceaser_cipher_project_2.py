# Caesar Cipher (Encrypt / Decrypt)

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            result += char

    return result


# main

print("🔐 Caesar Cipher Tool")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1/2): ")

text = input("Enter text: ")
shift = int(input("Enter shift key: "))


if choice == "1":
    result = encrypt(text, shift)
    print("🔒 Encrypted Text:", result)

elif choice == "2":
    result = decrypt(text, shift)
    print("🔓 Decrypted Text:", result)

else:
    print("❌ Invalid Choice")