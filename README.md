# CSE 3000 Final Project - Bias Analysis

## Project Overview
This project explores the intersection of technology, ethics, and societal impact by quantitatively analyzing potential demographic bias (such as gender, race, or age) in AI-generated outputs.  
The goal is to detect and measure bias from platforms (real or simulated) and reflect on the ethical implications.

We simulate platform outputs and run demographic analysis to identify disparities.

---

## Project Structure

bias_analysis_project/
- data/
  - collected_data.csv (collected prompts, texts, image paths)
  - collected_data_with_demographics.csv (demographic analysis results)
- images/
  - (downloaded sample images)
- scripts/
  - collect_data.py (script to generate fake data)
  - analyze_demographics.py (script to analyze demographics)
  - utils.py (helper functions)
- requirements.txt
- README.md

---

## Installation

1. Clone this repository: git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git cd YOUR_REPO_NAME

2. Install all required Python libraries: pip install -r requirements.txt

---

## How to Run

1. Navigate to the `scripts/` directory: cd scripts

2. Generate fake data: python collect_data.py

3. Perform demographic analysis: python analyze_demographics.py

4. Check results:
- `data/collected_data.csv`
- `data/collected_data_with_demographics.csv`

---

## Customizing

- **Change prompts**: Edit the `PROMPTS` list in `collect_data.py`.
- **Use real data**: Replace the fake text/image generation in `collect_data.py` with real platform outputs.
- **Adjust analysis**: Modify `ANALYZE_ACTIONS` in `analyze_demographics.py` to detect only specific attributes.

---

## Ethical Considerations

- Should platforms mirror real-world employment distributions or strive for equal demographic representation?
- What are the risks of biased training data?
- How can over-correcting bias harm platform trust?

---

## Requirements

- Python 3.8+
- pandas
- deepface
- matplotlib
- seaborn
- scipy
- requests

Install all requirements with: pip install -r requirements.txt

---

## Author

- Name: Matt Huang, Amit Banik, Tom Kuriakose, Ethan Ondek
- Class: CSE 3000
- Semester: Spring 2025

