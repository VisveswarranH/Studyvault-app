import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import subprocess
import pygame  # Import pygame for music playback

# Create base uploads folder if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# List of subjects
subjects = ["Math", "Science", "English", "History", "Other"]

# Initialize Pygame mixer for playing music
pygame.mixer.init()

# Function to upload a file to the selected subject folder
def upload_file():
    subject = subject_var.get()
    if subject == "":
        status_label.config(text="Please select a subject first.")
        return

    file_path = filedialog.askopenfilename()
    if file_path:
        subject_folder = os.path.join("uploads", subject)
        os.makedirs(subject_folder, exist_ok=True)

        file_name = os.path.basename(file_path)
        destination = os.path.join(subject_folder, file_name)
        shutil.copy(file_path, destination)
        status_label.config(text=f"Saved to {subject}/{file_name}")

# Function to open uploads folder
def open_uploads_folder():
    folder_path = os.path.abspath("uploads")
    if os.name == "nt":
        os.startfile(folder_path)
    elif os.name == "posix":
        subprocess.Popen(["open", folder_path])

# Function to view uploaded files in the selected subject
def view_files():
    subject = subject_var.get()
    if subject == "":
        messagebox.showwarning("No Subject Selected", "Please select a subject first.")
        return
    
    subject_folder = os.path.join("uploads", subject)
    if not os.path.exists(subject_folder):
        messagebox.showinfo("No Files", f"No files uploaded for {subject}.")
        return

    # List all files in the selected subject folder
    files = os.listdir(subject_folder)
    if files:
        files_str = "\n".join(files)
        messagebox.showinfo(f"Files in {subject}", files_str)
    else:
        messagebox.showinfo(f"No Files in {subject}", f"No files uploaded for {subject}.")

# Initialize Pygame mixer for playing music
pygame.mixer.init()

# Function to play background music
def play_music():
    # Load the music file
    pygame.mixer.music.load(r"C:\Users\admin\Downloads\badass.mp3")  # Use raw string for Windows path
    
    # Play the music in a loop (-1 means infinite loop)
    pygame.mixer.music.play(-1, 0.0)

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# You can call play_music() to start playing the music
# Example: play_music()


# Create main app window
app = tk.Tk()
app.title("StudyVault - File Organizer")
app.geometry("500x650")  # Adjust window size

# Styling for the interface
app.config(bg="#e1f5fe")  # Light blue background color

# Heading label with new styling
heading = tk.Label(app, text="📚 StudyVault", font=("Helvetica", 28, "bold"), bg="#e1f5fe", fg="#0d47a1")
heading.pack(pady=30)

# Subject selection dropdown with styling
subject_label = tk.Label(app, text="Select Subject:", font=("Helvetica", 16), bg="#e1f5fe", fg="#0d47a1")
subject_label.pack(pady=5)
subject_var = tk.StringVar(app)
subject_menu = tk.OptionMenu(app, subject_var, *subjects)
subject_menu.config(font=("Helvetica", 14), width=15, relief="solid", bd=2)
subject_menu.pack(pady=10)

# Upload button with hover effect and rounded corners
def on_enter_upload(e):
    upload_btn.config(bg="#388e3c")

def on_leave_upload(e):
    upload_btn.config(bg="#4CAF50")

upload_btn = tk.Button(app, text="Upload File", command=upload_file, font=("Helvetica", 14), bg="#4CAF50", fg="white", width=20, height=2, bd=3, relief="raised", activebackground="#388e3c", activeforeground="white")
upload_btn.pack(pady=10)
upload_btn.bind("<Enter>", on_enter_upload)
upload_btn.bind("<Leave>", on_leave_upload)

# View Files button with hover effect and rounded corners
def on_enter_view(e):
    view_files_btn.config(bg="#0288d1")

def on_leave_view(e):
    view_files_btn.config(bg="#2196F3")

view_files_btn = tk.Button(app, text="View Files", command=view_files, font=("Helvetica", 14), bg="#2196F3", fg="white", width=20, height=2, bd=3, relief="raised", activebackground="#0288d1", activeforeground="white")
view_files_btn.pack(pady=10)
view_files_btn.bind("<Enter>", on_enter_view)
view_files_btn.bind("<Leave>", on_leave_view)

# Open folder button with hover effect and rounded corners
def on_enter_open(e):
    open_folder_btn.config(bg="#ff8f00")

def on_leave_open(e):
    open_folder_btn.config(bg="#FF9800")

open_folder_btn = tk.Button(app, text="Open Uploads Folder", command=open_uploads_folder, font=("Helvetica", 14), bg="#FF9800", fg="white", width=20, height=2, bd=3, relief="raised", activebackground="#ff8f00", activeforeground="white")
open_folder_btn.pack(pady=10)
open_folder_btn.bind("<Enter>", on_enter_open)
open_folder_btn.bind("<Leave>", on_leave_open)

# Play Music button
play_music_btn = tk.Button(app, text="Play Music", command=play_music, font=("Helvetica", 14), bg="#8e24aa", fg="white", width=20, height=2, bd=3, relief="raised", activebackground="#7b1fa2", activeforeground="white")
play_music_btn.pack(pady=10)

# Stop Music button
stop_music_btn = tk.Button(app, text="Stop Music", command=stop_music, font=("Helvetica", 14), bg="#d32f2f", fg="white", width=20, height=2, bd=3, relief="raised", activebackground="#c62828", activeforeground="white")
stop_music_btn.pack(pady=10)

# Status label with font styling
status_label = tk.Label(app, text="No file uploaded yet.", font=("Helvetica", 14), bg="#e1f5fe", fg="#0d47a1")
status_label.pack(pady=10)

# Run the app
app.mainloop()
