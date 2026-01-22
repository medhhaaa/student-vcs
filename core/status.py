import os
import json
from core.hasher import hash_file

VCS_DIR = ".myvcs"
COMMITS_FILE = ".myvcs/commits.json"

def get_status():
    if not os.path.exists(VCS_DIR):
        return {
            "success": False,
            "message": "Not a VCS repository"
        }

    # load commits
    file = open(COMMITS_FILE, "r")
    commits = json.load(file)
    file.close()

    if len(commits) == 0:
        return {
            "success": True,
            "new": [],
            "modified": [],
            "deleted": []
        }

    last_commit = commits[-1]
    committed_files = last_commit["files"]

    current_files = {}

    # scan working directory
    for root, dirs, files in os.walk("."):
        if ".myvcs" in root:
            continue

        for name in files:
            if name == ".vcsignore":
                continue

            path = os.path.join(root, name)
            current_files[path] = hash_file(path)

    new_files = []
    modified_files = []
    deleted_files = []

    # check new and modified
    for path in current_files:
        if path not in committed_files:
            new_files.append(path)
        elif current_files[path] != committed_files[path]:
            modified_files.append(path)

    # check deleted
    for path in committed_files:
        if path not in current_files:
            deleted_files.append(path)

    return {
        "success": True,
        "new": new_files,
        "modified": modified_files,
        "deleted": deleted_files
    }
