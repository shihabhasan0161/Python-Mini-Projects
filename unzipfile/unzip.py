import os
import sys
import zipfile

def unzip_file(fname):
    try:
        output_name = os.path.splitext(fname)[0]
        with zipfile.ZipFile(fname) as f:
            f.extractall(output_name)
        print(f"{fname} is unzipped at {output_name}")
    except zipfile.BadZipFile:
        print("Invalid or corrupted zip file")
    except FileNotFoundError:
        print("Zip file not found")
    except PermissionError:
        print("Permission denied")

unzip_file(sys.argv[1])