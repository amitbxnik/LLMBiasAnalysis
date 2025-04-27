# scripts/analyze_demographics.py
import pandas as pd
import os
from deepface import DeepFace

# === Step 1: Settings ===
INPUT_CSV = "../data/collected_data.csv"
OUTPUT_CSV = "../data/collected_data_with_demographics.csv"
ANALYZE_ACTIONS = ['age', 'gender', 'race']  # You can adjust easily here

# === Step 2: Load Collected Data ===
df = pd.read_csv(INPUT_CSV)

# Add new columns if not exist
for col in ["Predicted Gender", "Predicted Age", "Predicted Race"]:
    if col not in df.columns:
        df[col] = ""

# === Step 3: Analyze Demographics ===
for idx, row in df.iterrows():
    img_path = row["Image Path"]
    if os.path.exists(img_path):
        try:
            analysis = DeepFace.analyze(img_path=img_path, actions=ANALYZE_ACTIONS, enforce_detection=False)
            df.at[idx, "Predicted Gender"] = analysis.get("gender", "")
            df.at[idx, "Predicted Age"] = analysis.get("age", "")
            df.at[idx, "Predicted Race"] = analysis.get("dominant_race", "")
            print(f"Analyzed: {img_path}")
        except Exception as e:
            print(f"❌ Failed to analyze {img_path}: {e}")

# === Step 4: Save the Results ===
df.to_csv(OUTPUT_CSV, index=False)
print(f"✅ Demographic analysis saved to {OUTPUT_CSV}")
