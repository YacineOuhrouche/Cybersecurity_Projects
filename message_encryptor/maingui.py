import tkinter as tk
from tkinter import messagebox
from colorama import Fore, Style, init

# Initialize colorama for automatic color reset (for terminal)
init(autoreset=True)

# Encrypt function using Caesar Cipher
def encrypt_message(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char  # non-alphabetic characters remain unchanged
    return encrypted_message

# Decrypt function (reverse the shift)
def decrypt_message(encrypted_message, shift):
    return encrypt_message(encrypted_message, -shift)  # Decrypt by reversing the shift

# Function to display results
def process_message():
    try:
        message = message_entry.get()  # Get message from input field
        shift = int(shift_entry.get())  # Get shift from input field
        encrypted = encrypt_message(message, shift)  # Encrypt the message
        decrypted = decrypt_message(encrypted, shift)  # Decrypt the message
        
        # Show results in the result text area
        encrypted_label.config(text=f"Encrypted Message: {encrypted}")
        decrypted_label.config(text=f"Decrypted Message: {decrypted}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the shift value.")

# Creating the main window
root = tk.Tk()
root.title("📝 Caesar Cipher Encryption/Decryption Tool")
root.geometry("600x400")  # Window size

# Heading Label
heading_label = tk.Label(root, text="Caesar Cipher Tool", font=("Arial", 24, "bold"), fg="#4CAF50")
heading_label.pack(pady=20)

# Message Label and Entry
message_label = tk.Label(root, text="Enter Message to Encrypt:", font=("Arial", 14))
message_label.pack(pady=5)
message_entry = tk.Entry(root, font=("Arial", 14), width=40)
message_entry.pack(pady=5)

# Shift Value Label and Entry
shift_label = tk.Label(root, text="Enter Shift Value (Integer):", font=("Arial", 14))
shift_label.pack(pady=5)
shift_entry = tk.Entry(root, font=("Arial", 14), width=40)
shift_entry.pack(pady=5)

# Encrypt Button
encrypt_button = tk.Button(root, text="Encrypt & Decrypt", font=("Arial", 14), bg="#4CAF50", fg="white", command=process_message)
encrypt_button.pack(pady=20)

# Labels for the results
encrypted_label = tk.Label(root, text="Encrypted Message: ", font=("Arial", 12), wraplength=500)
encrypted_label.pack(pady=5)
decrypted_label = tk.Label(root, text="Decrypted Message: ", font=("Arial", 12), wraplength=500)
decrypted_label.pack(pady=5)

# Footer Label
footer_label = tk.Label(root, text="Thank you for using the Caesar Cipher Tool!", font=("Arial", 10), fg="gray")
footer_label.pack(side=tk.BOTTOM, pady=20)

# Start the GUI event loop
root.mainloop()
