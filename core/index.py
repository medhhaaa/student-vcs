import os
import json
from core.hasher import hash_file

VCS_DIR = ".myvcs"
OBJECTS_DIR = ".myvcs/objects"
INDEX_FILE = ".myvcs/index.json"

def add_files():
    if not os.path.exists(VCS_DIR):
        return {
            "success": False,
            "message": "Not a VCS repository"
        }

    file = open(INDEX_FILE, "r")
    index_data = json.load(file)
    file.close()

    added_files = []

    for root, dirs, files in os.walk("."):
        if ".myvcs" in root:
            continue

        for name in files:
            if name == ".vcsignore":
                continue

            path = os.path.join(root, name)

            file_hash = hash_file(path)
            object_path = OBJECTS_DIR + "/" + file_hash

            if not os.path.exists(object_path):
                src = open(path, "rb")
                dst = open(object_path, "wb")
                dst.write(src.read())
                src.close()
                dst.close()

            index_data[path] = file_hash
            added_files.append(path)

    file = open(INDEX_FILE, "w")
    json.dump(index_data, file, indent=2)
    file.close()

    return {
        "success": True,
        "message": "Files added",
        "files": added_files,
        "count": len(added_files)
    }
