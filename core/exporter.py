import os
import json
import zipfile
from datetime import datetime

VCS_DIR = ".myvcs"

def export_repo(output_file):
    if not os.path.exists(VCS_DIR):
        return {
            "success": False,
            "message": "Not a VCS repository"
        }

    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zipf:

        # metadata
        meta = {
            "exported_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "format": "student-vcs-v1"
        }

        zipf.writestr("meta.json", json.dumps(meta, indent=2))

        # pack .myvcs contents
        for root, dirs, files in os.walk(VCS_DIR):
            for name in files:
                full_path = os.path.join(root, name)
                arc_name = os.path.join("repo", full_path)
                zipf.write(full_path, arc_name)

    return {
        "success": True,
        "message": f"Repository exported to {output_file}"
    }
