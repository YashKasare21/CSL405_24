from pathlib import Path

files = [f for f in Path('.').iterdir() if f.is_file()]  

print("Files in the current directory:")
for file in files:
    print(file.name)  

'''
The above scipt uses os module to perform the required function.
Utilize the pathlib module to perform the same functionality.
'''