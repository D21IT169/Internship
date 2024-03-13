import os

#TO remove files


file_path = "/home/hetvi/Documents/Hetvi_Python/OS_Modules/a/hey.txt"

try:
    os.remove(file_path)
    print(f"{file_path} has been deleted.")
    print("--------------------------------")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
