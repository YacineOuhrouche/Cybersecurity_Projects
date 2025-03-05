import random
import string
import tkinter as tk
from tkinter import messagebox, filedialog
import secrets  # More secure random generation

# Function to generate the password (using secrets for cryptographic security)
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Use secrets for cryptographically secure random password generation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Function to handle the button click event
def generate_and_display_password():
    try:
        password_length = int(length_entry.get())  # Get password length from input field
        
        if password_length < 6:
            messagebox.showwarning("Input Error", "Password length must be at least 6 characters.")
        else:
            # Get user preferences for character types
            use_upper = upper_var.get()
            use_lower = lower_var.get()
            use_digits = digits_var.get()
            use_symbols = symbols_var.get()
            
            generated_password = generate_password(password_length, use_upper, use_lower, use_digits, use_symbols)
            password_label.config(text=f"Generated Password: {generated_password}")  # Display password
            password_label.config(fg="#FF6347")  # Change text color to a brighter red
            
            # Store the generated password in the global variable
            global current_password
            current_password = generated_password
            
            # Display password strength (simple evaluation based on character variety)
            password_strength = evaluate_password_strength(generated_password)
            strength_label.config(text=f"Password Strength: {password_strength}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")

# Function to evaluate password strength
def evaluate_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Moderate"
    else:
        return "Strong"

# Function to save the password to a file
def save_password():
    try:
        # If a password hasn't been generated yet, show a warning
        if not current_password:
            messagebox.showwarning("No Password", "Please generate a password first.")
            return
        
        # Ask user where to save the password
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        
        if file_path:  # If the user provided a valid path
            with open(file_path, "w") as file:
                file.write(current_password)
            messagebox.showinfo("Success", f"Password saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("🔑 Random Password Generator")
root.geometry("500x550")  # Increased window size for better spacing

# Set a background color and padding for better visual appeal
root.configure(bg="#f0f0f0")

# Heading Label with custom font and color
heading_label = tk.Label(root, text="Random Password Generator", font=("Arial", 24, "bold"), fg="#4CAF50", bg="#f0f0f0")
heading_label.pack(pady=20)

# Instruction Label
instruction_label = tk.Label(root, text="Enter the desired length for your password", font=("Arial", 12), bg="#f0f0f0")
instruction_label.pack(pady=10)

# Password Length Label and Entry
length_label = tk.Label(root, text="Password Length:", font=("Arial", 14), bg="#f0f0f0")
length_label.pack(pady=5)

length_entry = tk.Entry(root, font=("Arial", 14), width=20, bd=2, relief="solid", justify="center")
length_entry.pack(pady=10)

# Character Type Checkboxes
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

upper_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, bg="#f0f0f0", font=("Arial", 12))
upper_checkbox.pack()

lower_checkbox = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, bg="#f0f0f0", font=("Arial", 12))
lower_checkbox.pack()

digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg="#f0f0f0", font=("Arial", 12))
digits_checkbox.pack()

symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#f0f0f0", font=("Arial", 12))
symbols_checkbox.pack()

# Generate Button with a modern look and feel
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 16), bg="#4CAF50", fg="white", bd=0, relief="solid", width=20, height=2, command=generate_and_display_password)
generate_button.pack(pady=20)

# Password Display Label with bigger font and added padding
password_label = tk.Label(root, text="Generated Password: ", font=("Arial", 16), wraplength=400, bg="#f0f0f0")
password_label.pack(pady=10)

# Password Strength Label
strength_label = tk.Label(root, text="Password Strength: ", font=("Arial", 14), bg="#f0f0f0")
strength_label.pack(pady=5)

# Save Button with a modern look and feel
save_button = tk.Button(root, text="Save Password", font=("Arial", 16), bg="#FF6347", fg="white", bd=0, relief="solid", width=20, height=2, command=save_password)
save_button.pack(pady=10)

# Footer Label with gray color and small font
footer_label = tk.Label(root, text="Powered by Random Password Generator", font=("Arial", 10), fg="gray", bg="#f0f0f0")
footer_label.pack(side=tk.BOTTOM, pady=20)

# Initialize a global variable to store the current generated password
current_password = ""

# Start the GUI event loop
root.mainloop()
