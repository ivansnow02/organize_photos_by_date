import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
import time


def get_month(filepath):
    with Image.open(filepath) as img:
        exif_data = get_exif_data(img)
        if "DateTimeOriginal" in exif_data:
            return exif_data["DateTimeOriginal"][5:7]
    return None


def get_exif_data(image):
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "DateTimeOriginal":
                exif_data[decoded] = value
    return exif_data



def organize_photos(src_dir):
    for filename in os.listdir(src_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(src_dir, filename)
            month = get_month(filepath)
            if month:
                dest_dir = os.path.join(src_dir, month)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(filepath, dest_dir)
                print(f'Moved {filepath} to {dest_dir}')
            else:
                print(f'No EXIF data for {filepath}')


if __name__ == '__main__':
    src_dir = input("Please enter the photo folder path:")
    if not os.path.isdir(src_dir):
        print("Invalid photo folder path")
        exit()
    organize_photos(src_dir)
