from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Load questions from Excel file
file_path = "questions_Gmat_PYA.xlsx"
df = pd.read_excel(file_path)

def get_random_question():
    question_row = df.sample(n=1).iloc[0]
    question = question_row['Question']
    options = [
        question_row['Option A'], 
        question_row['Option B'], 
        question_row['Option C'], 
        question_row['Option D'], 
        question_row.get('Option E', None)  # Handle missing Option E
    ]
    options = [opt for opt in options if pd.notna(opt)]  # Remove None values
    correct_answer = question_row['Correct Answer']
    return question, options, correct_answer

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        correct_answer = request.form.get('correct_answer')
        message = "Correct!" if user_answer == correct_answer else "Wrong! The correct answer is: " + correct_answer
    else:
        message = None
    
    question, options, correct_answer = get_random_question()
    return render_template('quiz.html', question=question, options=options, correct_answer=correct_answer, message=message)

if __name__ == '__main__':
    app.run(debug=True)
