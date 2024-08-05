import re
import tkinter as tk
from tkinter import scrolledtext

def process_text():
    input_text = text_area.get("1.0", tk.END)
    if not input_text.strip():
        update_status("Please enter some text to process", "red")
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
    update_status("Text processed successfully", "green")

def cut_text():
    selected_text = text_area.get("1.0", tk.END).strip()
    if selected_text:
        app.clipboard_clear()
        app.clipboard_append(selected_text)
        text_area.delete("1.0", tk.END)
        update_status("Text cut to clipboard", "green")
    else:
        update_status("No text to cut", "red")

def update_status(message, color):
    status_label.config(text=message, fg=color)
    app.after(3000, clear_status)  # Clear the status after 3 seconds

def clear_status():
    status_label.config(text='')

def on_enter(event, widget):
    widget.config(bg='#AED6F1')  # Change to a lighter color on hover

def on_leave(event, widget):
    widget.config(bg='#5DADE2')  # Revert to original color on leave

# Create the main application window
app = tk.Tk()
app.title("Text Processor")
app.geometry("1000x728")

# Center the window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 1000
window_height = 700
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
app.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Create a text area
text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=100, height=35)
text_area.pack(pady=20)

# Create a frame for buttons
button_frame = tk.Frame(app, bg='#E8F8F5')
button_frame.pack(pady=10)

# Create Process and Cut buttons with larger size and rounded corners
button_style = {
    "font": ("Helvetica", 14),
    "bg": "#5DADE2",
    "fg": "white",
    "activebackground": "#3498DB",
    "activeforeground": "white",
    "relief": "flat",
    "bd": 5,
    "width": 15,
    "height": 1
}

process_button = tk.Button(button_frame, text="Process Text", command=process_text, **button_style)
process_button.grid(row=0, column=0, padx=20)
process_button.bind("<Enter>", lambda event: on_enter(event, process_button))
process_button.bind("<Leave>", lambda event: on_leave(event, process_button))

cut_button = tk.Button(button_frame, text="Cut Text", command=cut_text, **button_style)
cut_button.grid(row=0, column=1, padx=20)
cut_button.bind("<Enter>", lambda event: on_enter(event, cut_button))
cut_button.bind("<Leave>", lambda event: on_leave(event, cut_button))

# Create a status bar
status_label = tk.Label(app, text='', bd=1, relief=tk.SUNKEN, anchor=tk.W, bg='#E8F8F5', pady=10)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

# Run the application
app.mainloop()
