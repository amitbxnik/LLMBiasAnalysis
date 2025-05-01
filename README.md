# CSE 3000 Final Project - Bias Analysis

## Project Overview
This project investigates political bias in large language models (LLMs) by analyzing their responses to politically sensitive prompts. We evaluated models such as OpenAI’s ChatGPT, Anthropic’s Claude, Google’s Gemini, and xAI’s Grok using a transformer-based classifier.

The goal is to classify responses as Left, Center, or Right-leaning, visualize distribution patterns, and reflect on the ethical implications of political bias in generative AI.

---

## Project Structure

bias_analysis_project/
  - data/
    - LLM_prompts.csv — Prompt, model, and response dataset
    - bias_results_hf.csv — Results with political bias labels

  - scripts/
    - analyze_bias.py — Uses a Hugging Face model to classify LLM responses
    - bias_results.py — Generates charts and a multipage summary report

  - requirements.txt — Required Python libraries
  - README.md - Project Documentation

---

## Installation

1. Clone this repository: 
  git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
  cd YOUR_REPO_NAME
2. Install all required Python libraries: pip install -r requirements.txt
   pip install -r requirements.txt

---

## How to Run

Step 1: Analyze Political Bias
  Run the script to classify all LLM responses by bias:
  python scripts/analyze_bias.py

  This creates:
  - data/bias_results_hf.csv

Step 2: Generate Visualizations
  Run the following to create summary charts and a PDF report:
  python scripts/bias_results.py

  This generates:
  - fig1_bias_distribution.pdf
  - fig2_bias_by_prompt_horizontal.pdf
  - fig3_bias_prompt_heatmap.pdf
  - fig4_model_distributions.pdf
  - fig5_bias_by_model_grouped.pdf
  - bias_analysis_report.pdf

---

## Classifier Model
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

