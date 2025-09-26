# Collaborators: Amit Banik, Matt Huang,Tom Kuriakose, Ethan Ondek

import os
import csv
from transformers import pipeline # imports HuggingFace (open-source ML Python library) pipeline tool for pretrained model

# file paths
INPUT_CSV    = "./data/LLM_prompts.csv" 
OUTPUT_CSV   = "./data/bias_results_hf.csv"

# HuggingFace model used for project, specific model labels response w/ Left, Center, & Right labels
MODEL_NAME   = "bucketresearch/politicalBiasBERT" 

def main():
    # loads pipeline for text classification
    classifier = pipeline(
        "text-classification",
        model=MODEL_NAME,
        tokenizer=MODEL_NAME,
        return_all_scores=False,    
        device=0                   
    )

    # opens input CSV & output CSV files
    with open(INPUT_CSV, newline='', encoding='utf-8') as fin, \
         open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as fout:

        reader = csv.DictReader(fin) # reads CSV into dict per row
        fieldnames = reader.fieldnames + ["bias"] # adds new "bias" col. to store the results
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader() # writes dict to file out

        # process each row in the input CSV file
        for row in reader:
            text = row.get("response", "").strip() # gets & strips response text of white space
            if text:
                try:
                    result = classifier(text, truncation=True)[0] # run model & get top result
                    row["bias"] = result["label"] # add result label to row
                except Exception as e:
                    print(f"Error on line {reader.line_num}: {e}")
                    row["bias"] = ""
            else:
                row["bias"] = "" # if there isn't a match, leave label as empty
            writer.writerow(row)

    print(f"Done—bias results written to {OUTPUT_CSV}") # confirmation message

if __name__ == "__main__":
    main()
