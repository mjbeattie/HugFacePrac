from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("I've been wating for a HuggingFace course!")