def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # isalpha() method in Python checks whether a string consists of only alphabetical characters.
            shift_amount = shift % 26 
            char_code =  # The ord() function returns the number representing the unicode code of a specified character.
            if char.islower():
                new_code = ord('a') + (char_code - ord('a') + shift_amount) % 26
            else:
                new_code = ord('A') + (char_code - ord('A') + shift_amount) % 26
            encrypted_text += chr(new_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("\nCaesar Cipher Tool")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
    
        choice = input("Enter your choice" '1/2/:')

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")


        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
