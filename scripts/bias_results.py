# Collaborators: Amit Banik, Matt Huang, Tom Kuriakose, Ethan Ondek

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# file config
INPUT_CSV      = "./data/bias_results_hf.csv"
FIG1_PATH      = "fig1_bias_distribution.pdf"
FIG2_PATH      = "fig2_bias_by_prompt_horizontal.pdf"
FIG3_PATH      = "fig3_bias_prompt_heatmap.pdf"
FIG4_PATH      = "fig4_model_distributions.pdf"
FIG5_PATH      = "fig5_bias_by_model_grouped.pdf"
REPORT_PDF     = "bias_analysis_report.pdf"

# fixed order for bias labels
BIAS_ORDER = ["Left", "Center", "Right"]

def normalize_bias_column(df):
    # cleans and standardizes bias col. values and makes sure cols have consistent categorical ordering.
    df['bias'] = df['bias'].astype(str).str.strip().str.title()
    df.loc[~df['bias'].isin(BIAS_ORDER), 'bias'] = 'Center'
    df['bias'] = pd.Categorical(df['bias'], categories=BIAS_ORDER, ordered=True)
    return df

def make_fig1(df):
    # bar chart of total bias label dist.
    counts = df['bias'].value_counts().reindex(BIAS_ORDER, fill_value=0)
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(counts.index, counts.values)
    ax.set_title("Overall Political Bias Distribution")
    ax.set_xlabel("Bias Label")
    ax.set_ylabel("Number of Responses")
    fig.tight_layout()
    fig.savefig(FIG1_PATH)
    plt.close(fig)

def make_fig2(df):
    # creates horizontal stacked bar chart showing bias counts per prompt
    ct = pd.crosstab(df['prompt'], df['bias']).reindex(columns=BIAS_ORDER, fill_value=0)
    prompts = ct.index.tolist()
    data = ct.values
    fig, ax = plt.subplots(figsize=(10, max(6, len(prompts)*0.3)))
    cum = np.zeros(len(prompts))
    for i, lbl in enumerate(BIAS_ORDER):
        ax.barh(prompts, data[:, i], left=cum, label=lbl)
        cum += data[:, i]
    ax.set_xlabel('Count of Responses')
    ax.set_ylabel('Prompt')
    ax.set_title('Bias Distribution by Prompt')
    ax.legend(title='Bias')
    fig.tight_layout()
    fig.savefig(FIG2_PATH)
    plt.close(fig)

def make_fig3(df):
    # generates heatmap showing counts of each bias label per prompt
    ct = pd.crosstab(df['prompt'], df['bias']).reindex(columns=BIAS_ORDER, fill_value=0)
    prompts, labels = ct.index.tolist(), BIAS_ORDER
    mat = ct.values
    fig, ax = plt.subplots(figsize=(10, max(6, len(prompts)*0.3)))
    im = ax.imshow(mat, aspect='auto')
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            ax.text(j, i, str(mat[i, j]), ha='center', va='center', fontsize=8)
    fig.colorbar(im, ax=ax, label='Count')
    ax.set_yticks(np.arange(len(prompts)))
    ax.set_yticklabels(prompts)
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)
    ax.tick_params(axis='y', labelsize=8)
    ax.set_title('Annotated Heatmap of Bias vs. Prompt')
    fig.tight_layout()
    fig.savefig(FIG3_PATH)
    plt.close(fig)

def make_fig4(df):
    # creates subplots of bias distributions for each model
    models = df['model'].unique().tolist()
    ncols = 2
    nrows = math.ceil(len(models) / ncols)
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(6*ncols, 4*nrows))
    axes = axes.flatten()
    for ax, model in zip(axes, models):
        counts = df[df['model'] == model]['bias'].value_counts().reindex(BIAS_ORDER, fill_value=0)
        ax.bar(counts.index, counts.values)
        ax.set_title(f"Bias for {model}")
        ax.tick_params(axis='x', rotation=45)
        ax.set_ylabel("Count")
    for ax in axes[len(models):]:
        fig.delaxes(ax)
    fig.tight_layout()
    fig.savefig(FIG4_PATH)
    plt.close(fig)

def make_fig5(df):
    # plots grouped bar chart comparing bias distributions across models
    ct = pd.crosstab(df['model'], df['bias']).reindex(columns=BIAS_ORDER, fill_value=0)
    labels = BIAS_ORDER
    index = ct.index.tolist()
    data = ct.values
    x = np.arange(len(index))
    width = 0.8 / len(labels)
    fig, ax = plt.subplots(figsize=(8,5))
    for i, lbl in enumerate(labels):
        ax.bar(x + i*width, data[:, i], width, label=lbl)
    ax.set_xticks(x + width*(len(labels)-1)/2)
    ax.set_xticklabels(index, rotation=45)
    ax.set_xlabel('Model')
    ax.set_ylabel('Count')
    ax.set_title('Comparison of Bias Across Models')
    ax.legend(title='Bias')
    fig.tight_layout()
    fig.savefig(FIG5_PATH)
    plt.close(fig)

def make_report(df):
    # creates a multipage PDF summarizing all figures (1 through 5)
    with PdfPages(REPORT_PDF) as pdf:
        # Figure 1
        counts = df['bias'].value_counts().reindex(BIAS_ORDER, fill_value=0)
        fig, ax = plt.subplots(figsize=(6,4))
        ax.bar(counts.index, counts.values)
        ax.set_title("Overall Political Bias Distribution")
        ax.set_xlabel("Bias Label")
        ax.set_ylabel("Number of Responses")
        fig.tight_layout()
        pdf.savefig(fig)
        plt.close(fig)

        # Figure 2
        ct2 = pd.crosstab(df['prompt'], df['bias']).reindex(columns=BIAS_ORDER, fill_value=0)
        prompts = ct2.index.tolist()
        data2 = ct2.values
        fig, ax = plt.subplots(figsize=(10, max(6, len(prompts)*0.3)))
        cum = np.zeros(len(prompts))
        for i, lbl in enumerate(BIAS_ORDER):
            ax.barh(prompts, data2[:, i], left=cum, label=lbl)
            cum += data2[:, i]
        ax.set_xlabel('Count of Responses')
        ax.set_ylabel('Prompt')
        ax.set_title('Bias Distribution by Prompt')
        ax.legend(title='Bias')
        fig.tight_layout()
        pdf.savefig(fig)
        plt.close(fig)

        # Figure 3
        fig, ax = plt.subplots(figsize=(10, max(6, len(prompts)*0.3)))
        im = ax.imshow(data2, aspect='auto')
        for i in range(data2.shape[0]):
            for j in range(data2.shape[1]):
                ax.text(j, i, str(data2[i,j]), ha='center', va='center', fontsize=8)
        fig.colorbar(im, ax=ax, label='Count')
        ax.set_yticks(np.arange(len(prompts)))
        ax.set_yticklabels(prompts)
        ax.set_xticks(np.arange(len(BIAS_ORDER)))
        ax.set_xticklabels(BIAS_ORDER)
        ax.set_title('Annotated Heatmap of Bias vs. Prompt')
        fig.tight_layout()
        pdf.savefig(fig)
        plt.close(fig)

        # Figure 4
        models = df['model'].unique().tolist()
        ncols = 2
        nrows = math.ceil(len(models) / ncols)
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(6*ncols, 4*nrows))
        axes = axes.flatten()
        for ax, model in zip(axes, models):
            counts = df[df['model'] == model]['bias'].value_counts().reindex(BIAS_ORDER, fill_value=0)
            ax.bar(counts.index, counts.values)
            ax.set_title(f"Bias for {model}")
            ax.tick_params(axis='x', rotation=45)
        for ax in axes[len(models):]:
            fig.delaxes(ax)
        fig.tight_layout()
        pdf.savefig(fig)
        plt.close(fig)

        # Figure 5
        ct = pd.crosstab(df['model'], df['bias']).reindex(columns=BIAS_ORDER, fill_value=0)
        labels = BIAS_ORDER
        index = ct.index.tolist()
        data = ct.values
        x = np.arange(len(index))
        width = 0.8 / len(labels)
        fig, ax = plt.subplots(figsize=(8,5))
        for i, lbl in enumerate(labels):
            ax.bar(x + i*width, data[:, i], width, label=lbl)
        ax.set_xticks(x + width*(len(labels)-1)/2)
        ax.set_xticklabels(index, rotation=45)
        ax.set_xlabel('Model')
        ax.set_ylabel('Count')
        ax.set_title('Comparison of Bias Across Models')
        ax.legend(title='Bias')
        fig.tight_layout()
        pdf.savefig(fig)
        plt.close(fig)

if __name__ == '__main__':
    df = pd.read_csv(INPUT_CSV)
    df = normalize_bias_column(df)
    make_fig1(df)
    make_fig2(df)
    make_fig3(df)
    make_fig4(df)
    make_fig5(df)
    print(f"Saved PDFs: {FIG1_PATH}, {FIG2_PATH}, {FIG3_PATH}, {FIG4_PATH}, {FIG5_PATH}")
    make_report(df)
    print(f"Saved combined report: {REPORT_PDF}")