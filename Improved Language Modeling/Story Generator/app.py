from flask import Flask, request, render_template
import openai
openai.api_key = "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"

app = Flask(__name__)

def generate_story(prompt):
    # Generate a story using OpenAI GPT-3
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=2048,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    story = response.choices[0].text
    return story

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    story = generate_story(prompt)
    return render_template('result.html', prompt=prompt, story=story)

if __name__ == '__main__':
    app.run(debug=True)
