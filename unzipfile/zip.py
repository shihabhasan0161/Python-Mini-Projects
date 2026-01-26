import os
import sys
import shutil

def zip_file(fname):
    try:
        output_name = os.path.splitext(fname)[0]
        shutil.make_archive(output_name, "zip", fname)
        print(f"Created: {output_name}.zip")
    except FileNotFoundError:
        print(f"{fname} not found.")
zip_file(sys.argv[1])