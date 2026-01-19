import sys
import os

# Add parent directory to path so we can import core module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.repo import init_repo
from core.index import add_files

if len(sys.argv) < 2:
    print("Usage: vcs <command>")
    sys.exit()

command = sys.argv[1]

if command == "init":
    result = init_repo()
    print(result["message"])

elif command == "add":
    if len(sys.argv) < 3 or sys.argv[2] != ".":
        print("Usage: vcs add .")
    else:
        result = add_files()
        print(result["message"])
        print("Files tracked:", result.get("count", 0))

else:
    print("Unknown command")
