import sys
import os

arguments = sys.argv[1:]

print(arguments)

os.system("dir > mydir.txt")
try:
    os.mkdir("test_dir")
except Exception:
    sys.exit(1)
else:
    print("File created successfully.")
