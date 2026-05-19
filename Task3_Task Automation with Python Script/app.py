import os
import shutil

print("JPG File Mover")

source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

count = 0

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):  # handles JPG, jpg
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")
        count += 1

print(f"\n{count} JPG files moved successfully!")
