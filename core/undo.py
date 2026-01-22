import os
import json

COMMITS_FILE = ".myvcs/commits.json"
OBJECTS_DIR = ".myvcs/objects"

def undo_last_commit():
    if not os.path.exists(COMMITS_FILE):
        return {
            "success": False,
            "message": "No commits to undo"
        }

    file = open(COMMITS_FILE, "r")
    commits = json.load(file)
    file.close()

    if len(commits) < 2:
        return {
            "success": False,
            "message": "Cannot undo the first commit"
        }

    # remove last commit
    commits.pop()

    previous_commit = commits[-1]
    files = previous_commit["files"]

    # restore files
    for path, file_hash in files.items():
        object_path = os.path.join(OBJECTS_DIR, file_hash)

        if os.path.exists(object_path):
            src = open(object_path, "rb")
            dst = open(path, "wb")
            dst.write(src.read())
            src.close()
            dst.close()

    # save updated commits
    file = open(COMMITS_FILE, "w")
    json.dump(commits, file, indent=2)
    file.close()

    return {
        "success": True,
        "message": "Last commit undone",
        "current_commit": previous_commit["id"]
    }
