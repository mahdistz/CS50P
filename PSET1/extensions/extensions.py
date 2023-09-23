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
file_name, extension = os.path.splitext(text)
if extension in extensions:
    print(extensions[extension])
else:
    print("application/octet-stream")
