# Large Language Model Bias Analysis

## Project Overview
This project investigates political bias in large language models (LLMs) by analyzing their responses to politically sensitive prompts using an open-source BERT-based classifier from Hugging Face. Models evaluated include OpenAI’s ChatGPT, Anthropic’s Claude, Google’s Gemini, and xAI’s Grok.

The goal is to classify responses as Left, Center, or Right-leaning, visualize distribution patterns, and reflect on the ethical implications of political bias in generative AI.

---

## Methodology

### 1. Prompt Selection
Forty politically relevant prompts covering contemporary issues were curated, including:  
- Gun control, healthcare, and immigration  
- DEI programs in workplaces  
- Transgender athletes in sports  
- Abortion access and reproductive rights  

### 2. Model Response Collection
- Each prompt was submitted to four LLMs under consistent settings using fresh accounts.  
- Each model generated a textual response (e.g., headlines), collected into a shared CSV dataset.  

### 3. Bias Classification
- Responses were labeled using the **politicalBiasBERT** transformer model from Hugging Face.  
- Each response was assigned a label: **Left**, **Center**, or **Right**.  
- A pretrained classifier was used for efficiency and reliability, leveraging its fine-tuning on political bias detection tasks and GPU acceleration for batch processing.  

### 4. Data Analysis & Visualization
- Results were stored in a structured CSV containing prompts, responses, the model name, and predicted bias.  
- Visualizations were created using **matplotlib** and **pandas**, including:  
  - Overall bias distribution charts  
  - Prompt-level heatmaps  
  - Comparative bar graphs across models

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
  We use the Hugging Face model: `bucketresearch/politicalBiasBERT`
  This transformer-based model labels text as:
  - Left
  - Center
  - Right

  It helps us quantify political leaning in each LLM response.

---

## Customization
- To test different prompts or models, modify data/LLM_prompts.csv

- To use a different classifier, change the model name in analyze_bias.py

- To enhance visualizations, update plotting code in bias_results.py

---

## Ethical Questions
- Do these models unintentionally promote political ideologies?

- How could biased outputs affect user beliefs or public discourse?

- How should developers balance fairness, transparency, and freedom of expression?

---

## Requirements

- Python 3.8+
- transformers
- pandas
- matplotlib
- numpy

Install all requirements with: pip install -r requirements.txt

---

