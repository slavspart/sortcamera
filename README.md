# Simple JPG Renaming Module

This Python module is designed to facilitate the renaming jpg files based on their metadata. It can be useful if you have photos from different sources which has different patterns of naming.

## Usage

1. **Copy images to source directory:**
   
   Create `source` directory
   ```
   mkdir source
   ```
   Copy images you want to rename to the `source` folder.

2. **Run the Script:**
   Execute the script, and it will process the images in the `source` folder, extract the creation dates from their metadata, and rename them accordingly. The renamed images will be saved in the `renamed` folder.
   
   ***Linux start script***
   
   Making initialization script executable (setting up venv and installing requirements)
    ```
   chmod +x commands.sh
    ```
    Running initialization script
    ```
   ./commands.sh
    ```
    Running the script
    ```
   python3 sort_meta.py
    ```
3. **Testing**

   You can test the script with sample photos in sample folder
## Requirements

- Python 3.x (Being developped on 3.10 version)
- Pillow library (`pip install Pillow`)


   - 
