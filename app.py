from flask import Flask, render_template, request
from groq_utils import learn_german, generate_mcq_questions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    input_text = ""
    if request.method == 'POST':
        input_text = request.form['english_text']
        translation = learn_german(input_text)
    return render_template('index.html', translation=translation, input_text=input_text)

def generate_mcqs():
    # You can replace this with your LLM or database-based logic
    return [
        {
            "question": "What is the capital of Germany?",
            "options": ["Berlin", "Munich", "Frankfurt", "Hamburg"],
            "answer": "Berlin"
        },
        {
            "question": "What is the German word for 'apple'?",
            "options": ["Apfel", "Banane", "Birne", "Traube"],
            "answer": "Apfel"
        }
    ]

 
@app.route('/daily-challenge')
def daily_challenge():
    mcqs = generate_mcq_questions()
    if not mcqs:
        return render_template('daily_challenge.html', mcqs=[], error="LLM returned invalid format.")
    return render_template('daily_challenge.html', mcqs=mcqs)



if __name__ == '__main__':
    app.run(debug=True)
