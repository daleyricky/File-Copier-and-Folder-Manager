# File Copier and Folder Manager

This is a simple desktop application built with **Python** and **Tkinter** that helps manage folders and files.  
It provides two main features:  

1. **Create Folders and (Optionally) Copy Files**  
   - Create multiple folders at once in a selected destination directory.  
   - Optionally copy selected files into each newly created folder.  

2. **Copy Files to All Subfolders**  
   - Select a parent directory.  
   - Copy one or more files into all its immediate subfolders.  

---

## Features

- User-friendly **graphical interface** (Tkinter-based).  
- **Browse dialogs** for selecting destination directories and files.  
- **Error handling** with clear popup messages.  
- **Optional file copying** when creating folders.  
- **Clear form buttons** to reset inputs for both parts of the app.  

---

## Requirements

- Python **3.7+**  
- Built-in libraries only:  
  - `os`  
  - `shutil`  
  - `tkinter`  

No external dependencies are required.  

---

## Installation

1. Make sure Python 3 is installed on your system.  
2. Download or clone this repository.  
3. Navigate to the project directory.  
4. Run the application:  

   ```bash
   python copy_file.py
   ```

---

## Usage

### Part 1: Create Folders and Copy Files (Optional)
1. Select a **destination directory**.  
2. Enter one or more **folder names** (one per line).  
3. (Optional) Browse and select files to copy.  
4. Click **"Create Folders (and Copy Files)"**.  

   - The app will create all listed folders inside the selected directory.  
   - If files were selected, they will be copied into each newly created folder.  

---

### Part 2: Copy Files to All Subfolders
1. Select a **parent directory** that contains subfolders.  
2. Browse and select one or more files to copy.  
3. Click **"Copy Files to Subfolders"**.  

   - The selected files will be copied into each immediate subfolder of the chosen directory.  

---

## Example Use Cases

- Creating project folders for multiple clients or tasks.  
- Copying template files into every newly created folder.  
- Distributing files (e.g., reports, images) to all subfolders of a directory in one click.  

---

## Notes

- Subfolders are detected only at the **first level** of the selected parent directory (not recursive).  
- Existing folders are skipped during creation.  
- If files already exist in a folder, they will be **overwritten**.  
