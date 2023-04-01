import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Set up the OpenAI API key
openai.api_key = "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"

# Define the translation function
def translate(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"translate from Khmer to English: {text}\n\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Define the routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    khmer_text = request.form['khmer_text']
    english_text = translate(khmer_text)
    return render_template('translation.html', khmer_text=khmer_text, english_text=english_text)

if __name__ == '__main__':
    app.run(debug=True)
