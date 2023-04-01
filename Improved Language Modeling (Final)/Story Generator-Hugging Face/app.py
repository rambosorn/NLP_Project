from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the language model using Hugging Face Transformers
story_generator = pipeline('text-generation', model='gpt2')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    length = int(request.form['length'])

    # Generate a story using the language model
    generated_story = story_generator(prompt, max_length=length, do_sample=True)[0]['generated_text']

    return render_template('result.html', prompt=prompt, generated_story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)
