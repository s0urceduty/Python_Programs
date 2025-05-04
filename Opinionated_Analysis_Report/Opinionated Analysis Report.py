import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from docx import Document
import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict, Counter
from string import punctuation

# Ensure NLTK data files are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Initialize global variables
document_content = ""
current_document_name = ""

def load_personality(personality_file):
    log_progress("Loading personality file...")
    with open(personality_file, 'r') as file:
        personality = json.load(file)
    log_progress("Personality file loaded.")
    return personality

def read_document(filepath):
    log_progress(f"Reading document: {filepath}")
    if filepath.endswith('.txt'):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                log_progress(f"Document content loaded (first 100 characters): {content[:100]}")
                return content
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='latin-1') as file:
                content = file.read()
                log_progress(f"Document content loaded with latin-1 encoding (first 100 characters): {content[:100]}")
                return content
    elif filepath.endswith('.docx'):
        doc = Document(filepath)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        content = '\n'.join(full_text)
        log_progress(f"Document content loaded (first 100 characters): {content[:100]}")
        return content
    elif filepath.endswith('.pdf'):
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            full_text = []
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                full_text.append(page.extract_text())
            content = '\n'.join(full_text)
            log_progress(f"Document content loaded (first 100 characters): {content[:100]}")
            return content
    return ""

def generate_opinionated_analysis(content, personality):
    log_progress("Generating opinionated analysis based on personality...")
    personality_descriptions = []
    for model, traits in personality.items():
        for trait, details in traits.items():
            if details["selected"]:
                personality_descriptions.append(details['options'][details['selected']])
    
    personality_traits_summary = "\n".join(personality_descriptions)
    
    # General personalized insights based on personality and document content
    words = word_tokenize(content.lower())
    stop_words = set(stopwords.words('english') + list(punctuation))
    meaningful_words = [word for word in words if word.isalnum() and word not in stop_words]
    most_common_words = [word for word, freq in Counter(meaningful_words).most_common(10)]
    
    key_themes = f"The document discusses various aspects, prominently including {', '.join(most_common_words)}."
    
    opinionated_analysis = (
        "Opinionated Analysis Report\n"
        "===========================\n\n"
        f"Introduction:\nThe document provides a comprehensive overview of its topic. {key_themes}\n\n"
        "Key Themes and Topics:\n"
        "----------------------\n"
        f"{', '.join(most_common_words)}\n\n"
        "Emotional Tone and Sentiment:\n"
        "-----------------------------\n"
        f"The emotional tone of the document can be described as "
        f"{'positive' if sum(1 for word in words if word in ['good', 'happy', 'positive', 'excellent', 'fortunate', 'correct', 'superior']) > sum(1 for word in words if word in ['bad', 'sad', 'negative', 'poor', 'unfortunate', 'wrong', 'inferior']) else 'negative' if sum(1 for word in words if word in ['bad', 'sad', 'negative', 'poor', 'unfortunate', 'wrong', 'inferior']) > sum(1 for word in words if word in ['good', 'happy', 'positive', 'excellent', 'fortunate', 'correct', 'superior']) else 'neutral'}.\n\n"
        "Structure and Organization:\n"
        "---------------------------\n"
        "The document is well-organized with clear sections and a coherent flow of ideas. The structure aids in conveying the main points effectively, making it easier for the reader to follow.\n\n"
        "Language and Style:\n"
        "------------------\n"
        "The language used in the document is straightforward and focused, with frequent use of words such as "
        f"{', '.join(most_common_words)}, which suggests a specific focus on these areas.\n\n"
        "Opinion Based on Personality Traits:\n"
        "===================================\n"
        f"{personality_traits_summary}\n"
    )
    
    return opinionated_analysis

def analyze_document(content, personality):
    log_progress("Analyzing document content...")
    words = word_tokenize(content.lower())
    stop_words = set(stopwords.words('english') + list(punctuation))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Generate opinionated analysis
    opinionated_analysis = generate_opinionated_analysis(content, personality)

    # Sentiment Analysis
    positive_words = set(["good", "happy", "positive", "excellent", "fortunate", "correct", "superior"])
    negative_words = set(["bad", "sad", "negative", "poor", "unfortunate", "wrong", "inferior"])
    sentiment_score = sum(1 for word in words if word in positive_words) - sum(1 for word in words if word in negative_words)

    # Document Structure Analysis
    paragraphs = content.split('\n\n')
    num_paragraphs = len(paragraphs)
    num_sentences = len(sent_tokenize(content))

    # Word Frequency Analysis
    word_freq = Counter(filtered_words).most_common(10)

    analysis = defaultdict(list)
    for model, traits in personality.items():
        for trait, details in traits.items():
            opinion = details["options"][details["selected"]]
            analysis[model].append(f"{trait}: {opinion}")

    report = generate_report_text(analysis, opinionated_analysis, sentiment_score, num_paragraphs, num_sentences, word_freq)
    log_progress("Document analysis complete.")
    return report

def generate_report_text(analysis, opinionated_analysis, sentiment_score, num_paragraphs, num_sentences, word_freq):
    report_lines = [f"{opinionated_analysis}\n"]
    report_lines.append("-" * 80)
    report_lines.append(f"Sentiment Analysis:\n{'=' * 80}\n{'Positive' if sentiment_score > 0 else 'Negative' if sentiment_score < 0 else 'Neutral'} (score: {sentiment_score})\n")
    report_lines.append("-" * 80)
    report_lines.append(f"Document Structure:\n{'=' * 80}\n  Paragraphs: {num_paragraphs}\n  Sentences: {num_sentences}\n")
    report_lines.append("-" * 80)
    report_lines.append("Word Frequency Analysis:\n" + '=' * 80)
    for word, freq in word_freq:
        report_lines.append(f"  {word}: {freq}")
    report_lines.append("-" * 80)
    report_lines.append("Opinion-based Analysis:\n" + '=' * 80)
    for model, traits in analysis.items():
        report_lines.append(f"{model}:")
        for trait_opinion in traits:
            report_lines.append(f"  {trait_opinion}")
    report_lines.append("-" * 80)

    report_text = '\n'.join(report_lines)
    log_progress(f"Generated report text (first 100 characters): {report_text[:100]}")
    return report_text

def save_report(report_text, output_folder, document_name):
    os.makedirs(output_folder, exist_ok=True)
    report_path = os.path.join(output_folder, f"{document_name}_report.txt")
    with open(report_path, 'w') as report_file:
        report_file.write(report_text)
    messagebox.showinfo("Report Saved", f"Report saved to {report_path}")
    log_progress(f"Report saved to {report_path}")

def load_document():
    global document_content, current_document_name
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Word documents", "*.docx"), ("PDF files", "*.pdf")])
    if not filepath:
        return

    document_content = read_document(filepath)
    document_display.delete('1.0', tk.END)
    document_display.insert(tk.END, document_content)
    
    analyze_button.config(state=tk.NORMAL)
    current_document_name = os.path.splitext(os.path.basename(filepath))[0]
    log_progress(f"Loaded document: {current_document_name}")

def analyze_document_action():
    global document_content
    if document_content:
        log_progress("Starting document analysis...")
        report_text = analyze_document(document_content, personality)
        if report_text:
            report_display.delete('1.0', tk.END)
            report_display.insert(tk.END, report_text)
            export_button.config(state=tk.NORMAL)
            log_progress("Document analysis complete.")
        else:
            log_progress("Analysis report is empty.")
            messagebox.showerror("Error", "Analysis failed. The report is empty.")
    else:
        messagebox.showerror("Error", "No document loaded to analyze!")
        log_progress("Error: No document loaded to analyze.")

def export_analysis():
    global current_document_name
    report_text = report_display.get('1.0', tk.END).strip()
    if report_text:
        save_report(report_text, 'Analysis Reports', current_document_name)
    else:
        messagebox.showerror("Error", "No report to save!")
        log_progress("Error: No report to save.")

def log_progress(message):
    progress_display.config(state=tk.NORMAL)
    progress_display.insert(tk.END, message + "\n")
    progress_display.see(tk.END)
    progress_display.config(state=tk.DISABLED)
    print(message)

# Set up the GUI
root = tk.Tk()
root.title("Opinionated Document Analyzer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

left_frame = tk.Frame(frame)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = tk.Frame(frame, bg="black")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(left_frame)
button_frame.pack(pady=5)

load_button = tk.Button(button_frame, text="Load Document", command=load_document)
load_button.pack(side=tk.LEFT, padx=5)

analyze_button = tk.Button(button_frame, text="Analyze Document", command=analyze_document_action, state=tk.DISABLED)
analyze_button.pack(side=tk.LEFT, padx=5)

export_button = tk.Button(button_frame, text="Export Analysis", command=export_analysis, state=tk.DISABLED)
export_button.pack(side=tk.LEFT, padx=5)

document_label = tk.Label(left_frame, text="Document Content:")
document_label.pack(anchor='w')

document_display = scrolledtext.ScrolledText(left_frame, width=80, height=15, wrap=tk.WORD)
document_display.pack(pady=5)

report_label = tk.Label(left_frame, text="Analysis Report:")
report_label.pack(anchor='w')

report_display = scrolledtext.ScrolledText(left_frame, width=80, height=15, wrap=tk.WORD)
report_display.pack(pady=5)

progress_label = tk.Label(right_frame, text="Progress Log", bg="black", fg="white")
progress_label.pack(pady=5)

progress_display = scrolledtext.ScrolledText(right_frame, width=40, height=40, wrap=tk.WORD, bg="black", fg="white")
progress_display.pack(pady=5)

# Load personality file from the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
personality_file = os.path.join(script_dir, 'Personality.json')
personality = load_personality(personality_file)

root.mainloop()
