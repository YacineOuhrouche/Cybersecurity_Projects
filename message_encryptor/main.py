def encrypt_message(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char  # non-alphabetic characters remain unchanged
    return encrypted_message

def decrypt_message(encrypted_message, shift):
    return encrypt_message(encrypted_message, -shift)  # Decrypt by reversing the shift

# Example usage
message = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value (integer): "))

encrypted = encrypt_message(message, shift)
print(f"Encrypted message: {encrypted}")

decrypted = decrypt_message(encrypted, shift)
print(f"Decrypted message: {decrypted}")
