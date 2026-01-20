import csv
import os
from pathlib import Path

# --- CONFIGURATION ---
dataset_root = Path("yemek") # Name of your image folder
output_csv = "turkish_food_dataset.csv"

# --- KNOWLEDGE BASE (QA PAIRS) ---
# Note: Questions and Answers are in Turkish as the model target language is Turkish.
qa_database = {
    "mercimek_corbasi": [
        {"question": "Bu nedir?", "answer": "Bu bir kase mercimek çorbası."},
        {"question": "Bu kase kaç kalori?", "answer": "Bir kase mercimek çorbası yaklaşık 150 kaloridir (kcal)."},
        {"question": "Protein miktarı ne kadar?", "answer": "Bu bir kase çorbada yaklaşık 6g protein bulunur."},
        {"question": "Diyette içilir mi?", "answer": "Evet, yüksek lif içeriği sayesinde tok tutar ve diyette uygundur."}
    ],
    "sutlac": [
        {"question": "Bu tatlı nedir?", "answer": "Bu, fırınlanmış bir sütlaçtır."},
        {"question": "Kalorisi ne kadar?", "answer": "Bir kase sütlaç yaklaşık 280 kaloridir."},
        {"question": "İçinde ne var?", "answer": "Süt, pirinç, şeker ve pirinç unu içerir."},
        {"question": "Sağlıklı mı?", "answer": "Şeker içerdiği için porsiyon kontrolüyle tüketilmelidir."}
    ],
    # ... You should paste your full QA dictionary here ...
    # (Senin orijinal dosyanın içindeki tüm yemek listesini buraya kopyalaman lazım)
}

def generate_csv_dataset():
    print(f"📂 Scanning directory: {dataset_root}")
    
    if not dataset_root.exists():
        print(f"❌ Error: Directory '{dataset_root}' not found.")
        return

    row_count = 0
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp'}

    # Using utf-8-sig for better Excel compatibility with Turkish characters
    with open(output_csv, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        # Header
        writer.writerow(['image_path', 'question', 'answer'])

        # Iterate through food folders
        for food_dir in dataset_root.iterdir():
            if not food_dir.is_dir() or food_dir.name.startswith('.'):
                continue
            
            food_name = food_dir.name
            
            if food_name not in qa_database:
                print(f"⚠️ Warning: No QA data found for '{food_name}'. Skipping.")
                continue
            
            print(f"🔹 Processing category: {food_name}")
            qa_list = qa_database[food_name]

            # Iterate through images in the folder
            for image_file in food_dir.iterdir():
                if image_file.suffix.lower() not in image_extensions:
                    continue
                
                # Create relative path (e.g., "mercimek_corbasi/mercimek1.jpg")
                relative_path = f"{food_name}/{image_file.name}"

                # Generate a row for each Question-Answer pair for this image
                for qa_pair in qa_list:
                    writer.writerow([relative_path, qa_pair["question"], qa_pair["answer"]])
                    row_count += 1

    print(f"\n✅ SUCCESS: Dataset generated at '{output_csv}'")
    print(f"📊 Total Data Rows: {row_count}")

if __name__ == "__main__":
    generate_csv_dataset()