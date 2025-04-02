from flask import Flask, render_template_string, request
import pandas as pd
import random

app = Flask(__quiz__)

# Load the questions from the Excel file
file_path = "questions_Gmat_PYA.xlsx"  # Update if needed
df = pd.read_excel(file_path)

def get_random_question():
    """Fetches a random question from the dataframe."""
    question_row = df.sample(n=1).iloc[0]
    question = question_row['Question']
    options = [question_row['Option A'], question_row['Option B'], question_row['Option C'], question_row['Option D'question_row['Option E']]
    correct_answer = question_row['Answer']
    return question, options, correct_answer

@app.route('/', methods=['GET', 'POST'])
def quiz():
    feedback = ""
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        correct_answer = request.form.get('correct_answer')
        if user_answer == correct_answer:
            feedback = "Correct! ✅"
        else:
            feedback = f"Incorrect ❌ The correct answer was {correct_answer}."
    
    # Get a new question
    question, options, correct_answer = get_random_question()
    
    return render_template_string('''
        <html>
        <head>
            <title>Simple Quiz</title>
        </head>
        <body>
            <h2>{{ question }}</h2>
            <form method="post">
                {% for option in options %}
                    <input type="radio" name="answer" value="{{ option }}" required> {{ option }}<br>
                {% endfor %}
                <input type="hidden" name="correct_answer" value="{{ correct_answer }}">
                <br>
                <input type="submit" value="Submit">
            </form>
            <p>{{ feedback }}</p>
        </body>
        </html>
    ''', question=question, options=options, correct_answer=correct_answer, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
