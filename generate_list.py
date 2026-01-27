import os

# CHANGE THIS to your pfps folder path
FOLDER_PATH = r"D:\html_files\profile_card\recommend_pfps"

# Allowed image extensions
EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp")

files = sorted(
    f for f in os.listdir(FOLDER_PATH)
    if f.lower().endswith(EXTENSIONS)
)

print("[")
for f in files:
    print(f'"recommend_pfps/{f}",')
print("]")
