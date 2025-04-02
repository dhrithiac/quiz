import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render! Your Flask app is running successfully."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render dynamically assigns a port
    app.run(host="0.0.0.0", port=port)

app = Flask(__quiz__)

# Load quiz questions from Excel
def load_questions():
    file_path = "questions_Gmat_PYA.xlsx"  # Make sure this file is in the same folder as this script
    df = pd.read_excel(file_path)
    return df

@app.route('/')
def quiz():
    df = load_questions()
    return render_template('quiz.html', questions=df.iterrows())

@app.route('/submit', methods=['POST'])
def submit():
    df = load_questions()
    score = 0
    
    for index, row in df.iterrows():
        correct_answer = str(row['Correct Answer']).strip().upper()
        user_answer = request.form.get(f'question_{index}', '').strip().upper()
        
        if user_answer == correct_answer:
            score += 1
    
    return render_template('result.html', score=score, total=len(df))

if __name__ == '__main__':
    app.run(debug=True)
