import os
os.makedirs("test/inner/folder")

import os
print(os.listdir("."))


files = [f for f in os.listdir(".") if f.endswith(".txt")]
print(files)


import shutil

shutil.copy("sample.txt", "test/sample.txt")
shutil.move("sample.txt", "test/sample_moved.txt")