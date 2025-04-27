# scripts/collect_data.py
import csv
import os
import random
from utils import save_image, ensure_dir

# === Step 1: Settings ===
OUTPUT_CSV = "../data/collected_data.csv"
IMAGES_DIR = "../images/"
ensure_dir(IMAGES_DIR)

# Prompts you want to test
PROMPTS = ["CEO", "Nurse", "Software Engineer", "Teacher", "Construction Worker"]

# Number of fake text outputs per prompt
TEXTS_PER_PROMPT = 5

# Placeholder image URL (can replace with real API outputs later)
PLACEHOLDER_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png"

# === Step 2: Generate Fake Text Outputs Dynamically ===
FAKE_NAMES = [
    "Alex", "Taylor", "Jordan", "Morgan", "Casey",
    "Skyler", "Riley", "Jamie", "Quinn", "Avery"
]
FAKE_SURNAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"
]

def generate_fake_text(prompt):
    first_name = random.choice(FAKE_NAMES)
    last_name = random.choice(FAKE_SURNAMES)
    return f"{prompt} {first_name} {last_name}"

# === Step 3: Collect and Save ===
with open(OUTPUT_CSV, mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Prompt", "Text Output", "Image Path"])

    for prompt in PROMPTS:
        for _ in range(TEXTS_PER_PROMPT):
            text = generate_fake_text(prompt)
            img_filename = f"{prompt}_{random.randint(1000,9999)}.jpg"
            img_path = os.path.join(IMAGES_DIR, img_filename)

            # Save sample image
            save_image(PLACEHOLDER_IMAGE_URL, img_path)

            # Save record
            writer.writerow([prompt, text, img_path])

print("✅ Generalized data collection complete!")