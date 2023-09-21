import os

extensions = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
}
text = input("File name: ").lower().strip()
file_extension = os.path.splitext(text)
if file_extension[1] in extensions:
    print(extensions[file_extension[1]])
else:
    print("application/octet-stream")
