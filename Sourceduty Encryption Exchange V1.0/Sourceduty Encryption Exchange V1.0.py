# Sourceduty Encrypted Exchange V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.
# Manage remote exchanges of encrypted .txt files sent between two or more users.

import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class SymmetricEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sourceduty Encrypted Exchange V1.0")
        self.root.configure(bg="#2e2e2e")
        self.root.geometry("500x380")
        self.root.resizable(False, False)

        self.role = tk.StringVar(value="sender")
        self.progress_text = tk.StringVar(value="Please select your role and start the process.")
        self.symmetric_key = None
        self.encrypted_data = None
        self.decrypted_data = None
        self.selected_file = None
        self.key_file = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Sourceduty Encrypted Exchange", font=("Arial", 16), bg="#2e2e2e", fg="white").grid(row=0, column=0, pady=10, padx=20, sticky="w")

        tk.Label(self.root, text="Select Role:", font=("Arial", 12), bg="#2e2e2e", fg="white").grid(row=1, column=0, sticky="w", padx=20)
        role_frame = tk.Frame(self.root, bg="#2e2e2e")
        role_frame.grid(row=2, column=0, sticky="w", padx=20, pady=5)
        tk.Radiobutton(role_frame, text="Sender", variable=self.role, value="sender", command=self.update_role, bg="#2e2e2e", fg="white", selectcolor="#4e4e4e").grid(row=0, column=0, padx=5)
        tk.Radiobutton(role_frame, text="Receiver", variable=self.role, value="receiver", command=self.update_role, bg="#2e2e2e", fg="white", selectcolor="#4e4e4e").grid(row=0, column=1, padx=5)

        self.file_button = tk.Button(self.root, text="Step 1: Select File", command=self.select_file, bg="#4e4e4e", fg="white", width=50, anchor="w")
        self.file_button.grid(row=3, column=0, pady=5, padx=20, sticky="w")

        self.step2_button = tk.Button(self.root, text="", command=self.step2_action, bg="#4e4e4e", fg="white", width=50, anchor="w", state="disabled")
        self.step2_button.grid(row=4, column=0, pady=5, padx=20, sticky="w")

        self.step3_button = tk.Button(self.root, text="", command=self.step3_action, bg="#4e4e4e", fg="white", width=50, anchor="w", state="disabled")
        self.step3_button.grid(row=5, column=0, pady=5, padx=20, sticky="w")

        tk.Label(self.root, text="Progress:", font=("Arial", 12), bg="#2e2e2e", fg="white").grid(row=6, column=0, pady=10, padx=20, sticky="w")
        self.progress_label = tk.Label(self.root, textvariable=self.progress_text, font=("Arial", 10), fg="white", bg="#2e2e2e", wraplength=460, justify="left")
        self.progress_label.grid(row=7, column=0, padx=20, sticky="w")

        self.update_role()

    def update_role(self):
        role = self.role.get()
        self.reset_vars()
        self.file_button.config(state="normal")
        if role == "sender":
            self.file_button.config(text="Step 1: Select File (.txt)")
            self.step2_button.config(text="Step 2: Generate and Save Key", state="normal")
            self.step3_button.config(text="Step 3: Encrypt File", state="disabled")
            self.update_progress("Role set to Sender. Start by selecting a file and generating a key.")

        elif role == "receiver":
            self.file_button.config(text="Step 1: Select Encrypted File (.enc)")
            self.step2_button.config(text="Step 2: Select Key File", state="normal")
            self.step3_button.config(text="Step 3: Decrypt File", state="disabled")
            self.update_progress("Role set to Receiver. Start by selecting an encrypted file and the key file.")

    def select_file(self):
        if self.role.get() == "sender":
            self.selected_file = filedialog.askopenfilename(
                title="Select file for encryption",
                initialdir=os.path.abspath(os.getcwd()),
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if self.selected_file:
                self.update_progress(f"File selected: {self.selected_file}")
                self.step3_button.config(state="normal")
            else:
                messagebox.showerror("Error", "No file selected.")
        elif self.role.get() == "receiver":
            self.selected_file = filedialog.askopenfilename(
                title="Select encrypted file",
                initialdir=os.path.abspath(os.getcwd()),
                filetypes=[("Encrypted files", "*.enc"), ("All files", "*.*")]
            )
            if self.selected_file:
                self.update_progress(f"Encrypted file selected: {self.selected_file}")
                self.step3_button.config(state="normal")
            else:
                messagebox.showerror("Error", "No encrypted file selected.")

    def step2_action(self):
        role = self.role.get()
        if role == "sender":
            self.generate_key()
        elif role == "receiver":
            self.load_key()

    def step3_action(self):
        role = self.role.get()
        if role == "sender":
            if self.selected_file and self.symmetric_key:
                self.encrypt_file()
            else:
                messagebox.showerror("Error", "File or key not available for encryption.")
        elif role == "receiver":
            if self.selected_file and self.symmetric_key:
                self.decrypt_file()
            else:
                messagebox.showerror("Error", "File or key not available for decryption.")

    def generate_key(self):
        try:
            self.symmetric_key = os.urandom(32)  # Generate a 256-bit AES key
            key_file = filedialog.asksaveasfilename(
                title="Save Symmetric Key",
                defaultextension=".key",
                filetypes=[("Key files", "*.key"), ("All files", "*.*")]
            )
            if key_file:
                with open(key_file, 'wb') as f:
                    f.write(self.symmetric_key)
                self.update_progress(f"Symmetric key generated and saved as {key_file}")
            else:
                messagebox.showerror("Error", "No file selected to save the key.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate key: {str(e)}")

    def load_key(self):
        self.key_file = filedialog.askopenfilename(
            title="Select Key File",
            initialdir=os.path.abspath(os.getcwd()),
            filetypes=[("Key files", "*.key"), ("All files", "*.*")]
        )
        if self.key_file:
            try:
                with open(self.key_file, 'rb') as f:
                    self.symmetric_key = f.read()
                self.update_progress(f"Symmetric key loaded successfully from {self.key_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load key: {str(e)}")
        else:
            messagebox.showerror("Error", "No key file selected.")

    def encrypt_file(self):
        if self.selected_file and self.symmetric_key:
            try:
                with open(self.selected_file, 'rb') as f:
                    plaintext = f.read()

                iv = os.urandom(16)
                cipher = Cipher(algorithms.AES(self.symmetric_key), modes.CFB(iv))
                encryptor = cipher.encryptor()
                encrypted_data = iv + encryptor.update(plaintext) + encryptor.finalize()

                encrypted_file = os.path.splitext(self.selected_file)[0] + '.enc'
                with open(encrypted_file, 'wb') as f:
                    f.write(encrypted_data)

                self.update_progress(f"File encrypted successfully. Encrypted file saved as {encrypted_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to encrypt data: {str(e)}")

    def decrypt_file(self):
        if self.selected_file and self.symmetric_key:
            try:
                with open(self.selected_file, 'rb') as f:
                    encrypted_data = f.read()

                iv = encrypted_data[:16]
                encrypted_data = encrypted_data[16:]
                cipher = Cipher(algorithms.AES(self.symmetric_key), modes.CFB(iv))
                decryptor = cipher.decryptor()
                decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

                decrypted_file = os.path.splitext(self.selected_file)[0] + '_decrypted.txt'
                with open(decrypted_file, 'wb') as f:
                    f.write(decrypted_data)

                self.update_progress(f"File decrypted successfully. Decrypted file saved as {decrypted_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to decrypt data: {str(e)}")

    def reset_vars(self):
        self.symmetric_key = None
        self.encrypted_data = None
        self.decrypted_data = None
        self.selected_file = None
        self.key_file = None

    def update_progress(self, message):
        self.progress_text.set(message)

if __name__ == "__main__":
    root = tk.Tk()
    app = SymmetricEncryptionApp(root)
    root.mainloop()
