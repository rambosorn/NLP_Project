# Machine Translation project working on Khmer language to English
Project Inspired by **Prof.Chaky** and fully support from our TA **Amanda**.
- Prof.github: https://github.com/chaklam-silpasuwanchai/Python-for-NLP

## Environment Setup
- This Machine Translation project going to run test in localhost with flask.
- Dataset for Khmer language I used the protain dataset: Helsinki-NLP/opus-mt-km-en
1. Install the required libraries: 
- pip install transformers flask
2. Import the required libraries: 
- from flask import Flask, request, jsonify
- from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
3. Load the pre-trained model and tokenizer:
- model_name = "Helsinki-NLP/opus-mt-km-en" # pre-trained model for Khmer-English translation
- tokenizer = AutoTokenizer.from_pretrained(model_name)
- model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
4. Create Flask to run your local machine


#### Sentiment submit form
<img src="https://github.com/rambosorn/NLP_Project/blob/main/Sentiment%20Analysis/image/form.png" alt="Alt text"
title="Optional title">
#### Output result
<img src="https://github.com/rambosorn/NLP_Project/blob/main/Sentiment%20Analysis/image/result.png" alt="Alt text" title="Optional title">


