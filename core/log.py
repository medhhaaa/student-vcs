import os
import json

COMMITS_FILE = ".myvcs/commits.json"

def get_log():
    if not os.path.exists(COMMITS_FILE):
        return {
            "success": False,
            "message": "No commits found"
        }

    file = open(COMMITS_FILE, "r")
    commits = json.load(file)
    file.close()

    history = []

    # latest commit first (better for UI)
    for commit in reversed(commits):
        history.append({
            "id": commit["id"],
            "message": commit["message"],
            "timestamp": commit["timestamp"],
            "parent": commit["parent"]
        })

    return {
        "success": True,
        "commits": history
    }
