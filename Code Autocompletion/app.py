from flask import Flask, request, jsonify, render_template
import openai
import os

openai.api_key = " "

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.get_json()
    input_code = data['code']

    model_engine = "davinci-codex"
    prompt = (f"Given the following Python code, complete the code:\n\n{input_code}\n\nCode:")
    try:
        completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=150, n=1,stop=None,temperature=0.7)
        message = completions.choices[0].text
        return jsonify({'suggestions': [message]})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
