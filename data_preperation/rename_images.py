import os
import re
from pathlib import Path

# --- CONFIGURATION ---
# Set the target directory path. "." means current directory.
TARGET_DIR = Path(".") 
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp'}

def rename_images():
    print(f"📂 Starting process in: {TARGET_DIR.resolve()}")
    
    # Regex to find files ending with digits (e.g., 'image1234.jpg')
    # You can adjust this regex if your raw files have a different pattern
    file_pattern = re.compile(r'(\d+)', re.IGNORECASE)

    for folder_path in TARGET_DIR.iterdir():
        # Skip if it's not a directory or hidden folder
        if not folder_path.is_dir() or folder_path.name.startswith('.'):
            continue

        folder_name = folder_path.name
        print(f"\n🔹 Processing Folder: {folder_name}")

        for file_path in folder_path.iterdir():
            if file_path.suffix.lower() not in ALLOWED_EXTENSIONS:
                continue

            # Check if file matches the pattern or just needs standardized naming
            # Here we take the numbers from original filename to keep order
            match = file_pattern.search(file_path.name)
            
            if match:
                file_number = match.group(1)
                new_filename = f"{folder_name}_{file_number}{file_path.suffix.lower()}"
                new_file_path = folder_path / new_filename

                if file_path == new_file_path:
                    print(f"  ✅ Already correct: {file_path.name}")
                    continue

                try:
                    file_path.rename(new_file_path)
                    print(f"  🔄 Renamed: {file_path.name} -> {new_filename}")
                except Exception as e:
                    print(f"  ❌ Error renaming {file_path.name}: {e}")

    print("\n✨ Renaming process completed successfully.")

if __name__ == "__main__":
    rename_images()