with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\n")


with open("sample.txt", "r") as f:
    print(f.read())


with open("sample.txt", "a") as f:
    f.write("Line 3\n")

with open("sample.txt", "r") as f:
    print(f.read())

import shutil

shutil.copy("sample.txt", "backup.txt")


import os

if os.path.exists("backup.txt"):
    os.remove("backup.txt")
