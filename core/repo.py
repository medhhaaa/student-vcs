import os
import json

VCS_DIR = ".myvcs"
OBJECTS_DIR = ".myvcs/objects"
INDEX_FILE = ".myvcs/index.json"
COMMITS_FILE = ".myvcs/commits.json"

def init_repo():
    if os.path.exists(VCS_DIR):
        return {
            "success": False,
            "message": "Repository already initialized"
        }

    os.mkdir(VCS_DIR)
    os.mkdir(OBJECTS_DIR)

    file = open(INDEX_FILE, "w")
    file.write("{}")
    file.close()

    file = open(COMMITS_FILE, "w")
    file.write("[]")
    file.close()

    return {
        "success": True,
        "message": "Repository initialized"
    }
