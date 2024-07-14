from flask import Flask, render_template, request, jsonify
from transformers import BertTokenizer, BertForSequenceClassification
import torch
from nltk.tokenize import sent_tokenize



# Load BERT model and tokenizerflasj
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)
model.eval()

# Preprocess the text
def preprocess_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    # Tokenize each sentence using BERT tokenizer
    tokenized_sentences = [tokenizer.encode(sentence, add_special_tokens=True, max_length=512, truncation=True) for sentence in sentences]
    # Pad tokenized sentences to the same length
    max_len = max(len(sentence) for sentence in tokenized_sentences)
    padded_sentences = [sentence + [0] * (max_len - len(sentence)) for sentence in tokenized_sentences]
    # Convert to PyTorch tensors
    input_ids = torch.tensor(padded_sentences)
    return input_ids

# Summarize the text using BERT
def generate_summary(text):
    input_ids = preprocess_text(text)
    with torch.no_grad():
        outputs = model(input_ids)
    # Assume the first output is the classification output
    logits = outputs[0]
    # Take the mean of logits across sentences as the summary score
    summary_logits = logits.mean(dim=0)
    # Convert logits to probabilities using softmax
    summary_probs = torch.softmax(summary_logits, dim=0)
    # Get the index of the sentence with the highest probability
    summary_index = summary_probs.argmax().item()
    # Get the corresponding sentence
    summary_sentence = sent_tokenize(text)[summary_index]
    return summary_sentence



