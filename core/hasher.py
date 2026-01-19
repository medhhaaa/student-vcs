import hashlib

def hash_file(path):
    sha1 = hashlib.sha1()

    file = open(path, "rb")
    while True:
        data = file.read(4096)
        if not data:
            break
        sha1.update(data)
    file.close()

    return sha1.hexdigest()
