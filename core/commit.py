import os
import json
import hashlib
from datetime import datetime

VCS_DIR = ".myvcs"
INDEX_FILE = ".myvcs/index.json"
COMMITS_FILE = ".myvcs/commits.json"

def make_commit(message):
    if not os.path.exists(VCS_DIR):
        return {
            "success": False,
            "message": "Not a VCS repository"
        }

    # load index
    file = open(INDEX_FILE, "r")
    index_data = json.load(file)
    file.close()

    if len(index_data) == 0:
        return {
            "success": False,
            "message": "No files to commit"
        }

    # load commits
    if os.path.exists(COMMITS_FILE):
        file = open(COMMITS_FILE, "r")
        commits = json.load(file)
        file.close()
    else:
        commits = []

    parent_id = None
    if len(commits) > 0:
        parent_id = commits[-1]["id"]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    raw = message + timestamp + str(parent_id)
    commit_id = hashlib.sha1(raw.encode()).hexdigest()[:7]

    commit = {
        "id": commit_id,
        "message": message,
        "timestamp": timestamp,
        "parent": parent_id,
        "files": index_data
    }

    commits.append(commit)

    file = open(COMMITS_FILE, "w")
    json.dump(commits, file, indent=2)
    file.close()

    return {
        "success": True,
        "message": "Commit created",
        "commit": commit
    }
