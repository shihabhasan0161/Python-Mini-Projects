from pathlib import Path
import shutil
import mimetypes

DOWNLOADS_FOLDER = Path.home() / "Downloads"
TARGET_FOLDER = Path.home() / "Organized"

TARGET_FOLDER.mkdir(exist_ok=True) # creates the target folder if it doesn't exist, exist_ok=True prevents an error if the folder already exists

def get_file_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        return "Others"
    if mime_type.startswith("image"):
        return "Images"
    elif mime_type.startswith("video"):
        return "Videos"
    elif mime_type.startswith("audio"):
        return "Audio"
    elif mime_type.startswith("application/pdf"):
        return "PDF"
    elif mime_type.startswith("application/zip"):
        return "Archives"
    elif mime_type.startswith("text") or "word" in mime_type:
        return "Documents"
    else:
        return "Others"
    
def move_file(file_path):
    file_type = get_file_type(file_path)
    target_folder = TARGET_FOLDER / file_type # joins the target folder with the file type [e.g. "Organized/Images"]
    target_folder.mkdir(exist_ok=True)
    target_path = target_folder / file_path.name
    
    counter = 1

    # If a file with the same name already exists, append a number to the filename to avoid overwriting
    while target_path.exists():
        target_path = target_folder / f"{file_path.stem}_{counter}{file_path.suffix}" # e.g. "file.txt" becomes "file_1.txt", "file_2.txt", etc. path.stem: https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.stem
        counter += 1

    shutil.move(file_path, target_path)

def organize_folder():
    for file in DOWNLOADS_FOLDER.iterdir():
        if file.is_file():
            move_file(file)

if __name__ == "__main__":
    organize_folder()
    print(f"Files have been organized successfully! from {DOWNLOADS_FOLDER} to {TARGET_FOLDER}")