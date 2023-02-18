from flask import Flask, request, render_template, url_for
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import base64
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np

nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']

    # Analyze sentiment
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    sentiment = ''
    if scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Create plot
    x = np.array([1, 2, 3, 4])
    y = np.array([scores['neg'], scores['neu'], scores['pos'], scores['compound']])
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xticks(x)
    ax.set_xticklabels(['Negative', 'Neutral', 'Positive', 'Compound'])
    ax.set_ylim([-1, 1])
    ax.set_ylabel('Score')
    ax.set_title('Sentiment Analysis')
    
    # Save plot to buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert plot to base64 encoded string
    image_png = base64.b64encode(buffer.getvalue()).decode('ascii')

    return render_template('result.html', response={'text': text, 'sentiment': sentiment, 'scores': scores, 'graphic': image_png})

@app.route('/plot/<graphic>')
def plot(graphic):
    image = base64.b64decode(graphic)
    buffer = io.BytesIO(image)
    canvas = FigureCanvas(plt.Figure())
    canvas.draw()
    return canvas.tostring_rgb(), {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(debug=True)
