from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def generate_question():
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    op = random.choice(['+', '-', '*'])
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    else:
        answer = a * b
    question = f"What is {a} {op} {b}?"
    return {"question": question, "answer": answer}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question')
def question():
    q = generate_question()
    return jsonify(q)

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    correct = int(data['user_answer']) == int(data['correct_answer'])
    return jsonify({"correct": correct})

if __name__ == '__main__':
    app.run(debug=True)
