"""Module for renaming from meta"""

from collections import Counter
import os
import shutil

# Pillow library for working with images
from PIL import Image
from PIL.ExifTags import TAGS

BASE_DIR = os.getcwd()
PIC_DIR = os.path.join(BASE_DIR, "source")
RENAMED_DIR = os.path.join(BASE_DIR, "renamed")

# creating source and target folders
os.makedirs(RENAMED_DIR, exist_ok=True)


def get_creation_dates(image_dir) -> list[tuple[str, str]]:
    """Creating list of tuples containing the date and filename"""
    dates = []
    image_list = os.listdir(image_dir)
    for filename in image_list:
        image_path = os.path.join(image_dir, filename)
        try:
            # Open the image file
            img = Image.open(image_path)

            # Extract EXIF data
            exif_data = img._getexif()

            # Check if EXIF data exists
            if exif_data is not None:
                # Iterate through the EXIF tags
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == "DateTimeOriginal":
                        # creating list of tuples with dates and filenames
                        dates.append((value, filename))
            else:
                print (f'{filename} has no metadata')
        except Exception as e:
            print(f"Error: {e}")
    # sorting list before return in order the earliest photos of the day
    # are the first
    return sorted(dates)


def rename_files(date_pairs: list[tuple[str, str]]) -> None:
    """Copying original file with new names based on date of creation"""
    # Counter creates dictionary like object
    # counting how many times a value is found in list
    suffix_counter = Counter()
    for date, old_filename in date_pairs:
        # removing hours of creation and format date for
        # being proper name because date in meta comes like 2022:08:27
        date_formatted = date.split()[0].replace(":", "_")
        # counting how many photos of this date are there
        suffix_counter[date_formatted] += 1
        new_filename = f"{date_formatted}_{suffix_counter[date_formatted]}.jpg"
        # Copying files saving meta info (method copy2)
        shutil.copy2(
            os.path.join(PIC_DIR, old_filename), os.path.join(RENAMED_DIR, new_filename)
        )


if __name__ == "__main__":
    date_pairs = get_creation_dates(PIC_DIR)
    rename_files(date_pairs)
