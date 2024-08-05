import re
import tkinter as tk
from tkinter import scrolledtext, messagebox

def process_text():
    input_text = text_area.get("1.0", tk.END)
    if not input_text.strip():
        messagebox.showwarning("Warning", "Please enter some text to process")
        return
    
    # Define a function to handle the replacement logic
    def replace_func(match):
        content = match.group(1)
        return content if content == 'client' else ''
    
    # Replace square bracket content except for 'client'
    processed_text = re.sub(r'\[(.*?)\]', replace_func, input_text)
    
    # Remove *, (, )
    processed_text = re.sub(r'\*|\(|\)', '', processed_text)
    
    # Clear the text area and insert the processed text
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.INSERT, processed_text)
    
def clear_text():
    text_area.delete("1.0", tk.END)

# Create the main application window
app = tk.Tk()
app.title("Text Processor")
app.geometry("600x400")

# Create a text area
text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=70, height=20)
text_area.pack(pady=10)

# Create a frame for buttons
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

# Create Process and Clear buttons
process_button = tk.Button(button_frame, text="Process Text", command=process_text)
process_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear Text", command=clear_text)
clear_button.grid(row=0, column=1, padx=10)

# Run the application
app.mainloop()
