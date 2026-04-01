import os
os.makedirs("tes/inner/folder")

import os
print(os.listdir("."))


files = [f for f in os.listdir(".") if f.endswith(".txt")]
print(files)


import shutil

shutil.copy("sample.txt", "tes/sample.txt")
shutil.move("sample.txt", "tes/sample_moved.txt")