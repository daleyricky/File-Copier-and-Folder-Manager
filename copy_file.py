import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to select directory
def select_directory(entry):
    folder_path = filedialog.askdirectory(title="Select destination directory")
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

# Function to clear Part 1 fields
def clear_part1_fields():
    folder_entry.delete(0, tk.END)
    folder_names_text.delete("1.0", tk.END)
    file_entry.delete(0, tk.END)

# Function to clear Part 2 fields
def clear_part2_fields():
    folder_entry_part2.delete(0, tk.END)
    file_entry_part2.delete(0, tk.END)

# Part 1: Folder Creation and Copying Files to Newly Created Folders
def create_folders(destination_directory, folder_names):
    """
    Creates folders in the destination directory.
    """
    if not os.path.isdir(destination_directory):
        messagebox.showerror("Error", f"The directory {destination_directory} does not exist.")
        return []

    created_folders = []
    for folder_name in folder_names:
        folder_path = os.path.join(destination_directory, folder_name.strip())
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder created: {folder_path}")
            created_folders.append(folder_path)
        else:
            print(f"Folder already exists: {folder_path}")
    
    if created_folders:
        messagebox.showinfo("Success", "Folders created successfully!")
    else:
        messagebox.showinfo("Notice", "No folders were created (they may already exist).")
    
    return created_folders

def copy_file_to_folders(file_paths, folders):
    """
    Copies selected files to newly created folders.
    """
    if not file_paths:
        return

    for file_path in file_paths:
        if not os.path.isfile(file_path):
            messagebox.showerror("Error", f"The file {file_path} does not exist.")
            return

        for folder in folders:
            shutil.copy(file_path, folder)
            print(f"Copied {file_path} to {folder}")
    
    messagebox.showinfo("Success", "Files copied to all folders successfully!")

# Folder creation and optional file copying
def on_create_folders_click():
    destination_dir = folder_entry.get()
    folder_names = folder_names_text.get("1.0", tk.END).splitlines()  # Split by lines
    folder_names = [folder_name for folder_name in folder_names if folder_name.strip()]  # Remove empty lines
    
    if not folder_names:
        messagebox.showwarning("No Folder Names", "Please enter folder names.")
        return

    created_folders = create_folders(destination_dir, folder_names)
    
    if created_folders:
        # Optionally copy files if any were selected
        file_paths = file_entry.get().split(",")
        if file_paths and file_paths[0]:  # Check if there's a file selected
            copy_file_to_folders(file_paths, created_folders)

# Part 2: Copy Files to All Subfolders of Selected Folder

def copy_to_all_subfolders(file_paths, parent_folder):
    """
    Copies selected files to all subfolders within the specified parent folder.
    """
    subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]

    if not subfolders:
        messagebox.showwarning("No Subfolders", "The selected folder does not contain any subfolders.")
        return

    for file_path in file_paths:
        if not os.path.isfile(file_path):
            messagebox.showerror("Error", f"The file {file_path} does not exist.")
            return

        for subfolder in subfolders:
            shutil.copy(file_path, subfolder)
            print(f"Copied {file_path} to {subfolder}")
    
    messagebox.showinfo("Success", "Files copied to all subfolders successfully!")

def on_copy_to_subfolders_click():
    parent_folder = folder_entry_part2.get()
    if not parent_folder or not os.path.isdir(parent_folder):
        messagebox.showerror("Error", "Please select a valid destination directory.")
        return

    file_paths = file_entry_part2.get().split(",")
    if not file_paths or not file_paths[0]:
        messagebox.showerror("Error", "Please select at least one file to copy.")
        return
    
    copy_to_all_subfolders(file_paths, parent_folder)

# File selection dialog
def select_files(entry):
    file_paths = filedialog.askopenfilenames(title="Select file(s) to copy")
    if file_paths:
        entry.delete(0, tk.END)
        entry.insert(0, ",".join(file_paths))

# Create the main window
root = tk.Tk()
root.title("File Copier and Folder Manager")

# Set standard width for input fields and buttons
entry_width = 60
button_width = 25

# PART 1: Folder Creation and Copying Files to New Folders

# Section label
folder_label = tk.Label(root, text="Part 1: Create Folders and Copy Files (Optional)")
folder_label.grid(row=0, column=1, padx=10, pady=10)

# Destination folder selection for creation
folder_label = tk.Label(root, text="Select Destination Directory:")
folder_label.grid(row=1, column=0, padx=10, pady=5)

folder_entry = tk.Entry(root, width=entry_width)
folder_entry.grid(row=1, column=1, padx=10, pady=5)

folder_button = tk.Button(root, text="Browse", command=lambda: select_directory(folder_entry), width=button_width)
folder_button.grid(row=1, column=2, padx=10, pady=5)

# Folder names input
folder_names_label = tk.Label(root, text="Enter Folder Names (one per line):")
folder_names_label.grid(row=2, column=0, padx=10, pady=5)

folder_names_text = tk.Text(root, width=entry_width, height=10)
folder_names_text.grid(row=2, column=1, padx=10, pady=5)

# File selection (optional)
file_label = tk.Label(root, text="Optional: Select Files to Copy:")
file_label.grid(row=3, column=0, padx=10, pady=5)

file_entry = tk.Entry(root, width=entry_width)
file_entry.grid(row=3, column=1, padx=10, pady=5)

file_button = tk.Button(root, text="Browse Files", command=lambda: select_files(file_entry), width=button_width)
file_button.grid(row=3, column=2, padx=10, pady=5)

# Button to create folders and optionally copy files
create_folders_and_copy_button = tk.Button(root, text="Create Folders (and Copy Files)", command=on_create_folders_click, width=button_width)
create_folders_and_copy_button.grid(row=4, column=1, pady=10)

# Button to clear Part 1 form
clear_part1_button = tk.Button(root, text="Clear Form", command=clear_part1_fields, width=button_width)
clear_part1_button.grid(row=4, column=2, padx=10, pady=10)

# PART 2: Copying Files to All Subfolders of Selected Folder

# Section label
existing_label = tk.Label(root, text="Part 2: Copy Files to All Subfolders")
existing_label.grid(row=5, column=1, padx=10, pady=10)

# Destination folder selection for copying to subfolders
folder_label_part2 = tk.Label(root, text="Select Destination Directory with Subfolders:")
folder_label_part2.grid(row=6, column=0, padx=10, pady=5)

folder_entry_part2 = tk.Entry(root, width=entry_width)
folder_entry_part2.grid(row=6, column=1, padx=10, pady=5)

folder_button_part2 = tk.Button(root, text="Browse", command=lambda: select_directory(folder_entry_part2), width=button_width)
folder_button_part2.grid(row=6, column=2, padx=10, pady=5)

# File selection for copying to subfolders
file_label_part2 = tk.Label(root, text="Select Files to Copy:")
file_label_part2.grid(row=7, column=0, padx=10, pady=5)

file_entry_part2 = tk.Entry(root, width=entry_width)
file_entry_part2.grid(row=7, column=1, padx=10, pady=5)

file_button_part2 = tk.Button(root, text="Browse Files", command=lambda: select_files(file_entry_part2), width=button_width)
file_button_part2.grid(row=7, column=2, padx=10, pady=5)

# Button to copy files to all subfolders
copy_subfolders_button = tk.Button(root, text="Copy Files to Subfolders", command=on_copy_to_subfolders_click, width=button_width)
copy_subfolders_button.grid(row=8, column=1, pady=10)

# Button to clear Part 2 form
clear_part2_button = tk.Button(root, text="Clear Form", command=clear_part2_fields, width=button_width)
clear_part2_button.grid(row=8, column=2, padx=10, pady=10)

# Run the application
root.mainloop()
