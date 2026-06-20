import os

folders = [
    "01_Basics",
    "02_ControlFlow",
    "03_Modules",
    "04_Functions",
    "05_FileHandling",
    "06_Collections",
    "07_OOP",
    "08_Projects"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("DN Structure Created")