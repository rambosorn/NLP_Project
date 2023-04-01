# Story Generator using Tranformer
Project Inspired by **Prof.Chaky** and fully support from our TA **Amanda**.
- Prof.github: https://github.com/chaklam-silpasuwanchai/Python-for-NLP

## Environment Setup
- This Machine Translation project going to run test in localhost with flask.
- Dataset for Khmer language I used the protain dataset: Helsinki-NLP/opus-mt-km-en.
- learn more here: https://huggingface.co/Helsinki-NLP/opus-mt-mul-en
1. Install the required libraries: 
- pip install transformers flask
2. Import the required libraries: 
- from flask import Flask, request, jsonify
- from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
3. Load the pre-trained model and tokenizer:
- model_name = "Helsinki-NLP/opus-mt-km-en" # pre-trained model for Khmer-English translation
- tokenizer = AutoTokenizer.from_pretrained(model_name)
- model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
4. Create Flask project to run on your local machine


#### result image here
<img src="#" alt="Alt text"
title="Optional title">
#### image 01
<img src="#" title="Optional title">


