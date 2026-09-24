import os
import shutil
 
FOLDERS = {
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos":    [".mp4", ".mkv", ".avi", ".mov"],
    "Music":     [".mp3", ".wav", ".aac"],
    "Archives":  [".zip", ".rar", ".7z", ".tar"],
    "Programs":  [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
}
 
path = input("Enter the full path of the folder to organize : ")
 
if not os.path.isdir(path):
    print("Invalid folder path.")
else:
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
 
            target = "Others"
            for folder, extensions in FOLDERS.items():
                if ext in extensions:
                    target = folder
                    break
 
            destination = os.path.join(path, target)
            os.makedirs(destination, exist_ok=True)
            shutil.move(full_path, os.path.join(destination, file))
            print("Moved :", file, "-->", target)
 
    print("Folder organized successfully.")
