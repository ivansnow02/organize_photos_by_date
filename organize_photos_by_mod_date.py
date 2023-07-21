import datetime
import os
import shutil


def get_month(filepath):
    ctime = os.path.getctime(filepath)
    date = datetime.datetime.fromtimestamp(ctime)
    return date.strftime("%m")


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
                print(f'Failed to get date for {filepath}')


if __name__ == '__main__':
    src_dir = input("Please enter the photo folder path:")
    if not os.path.isdir(src_dir):
        print("Invalid photo folder path")
        exit()
    organize_photos(src_dir)
