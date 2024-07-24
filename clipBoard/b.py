import pyperclip
import time
import tkinter as tk
from threading import Thread

# Initialize the main window
root = tk.Tk()
root.title("Clipboard Text Buttons")

root.geometry("800x600")  # Width x Height

button_frame = tk.Frame(root)
button_frame.pack(pady=20, padx=20)

# Function to copy text to the clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)
    print(f"Copied to clipboard: {text}")

# Function to add a button
def add_button(text):
    button = tk.Button(button_frame, text=text, command=lambda: copy_to_clipboard(text))
    button.pack(fill='both', expand=True, padx=5, pady=5)

# Function to monitor clipboard and add buttons for new text
def monitor_clipboard():
    number = 0
    old_text = None
    all_words = []

    while True:
        text = pyperclip.paste()

        if number == 0:
            old_text = text
            number += 1

        if text != old_text:
            # Check if the text is already in all_words
            if text not in all_words:
                all_words.append(text)
                # Use the add_button function to add the button in the main thread
                root.after(0, add_button, text)
                old_text = text
                number = 0

# Start the clipboard monitoring in a separate thread
thread = Thread(target=monitor_clipboard, daemon=True)
thread.start()

# Start the Tkinter main loop
root.mainloop()
