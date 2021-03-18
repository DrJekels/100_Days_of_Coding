from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

for questions in question_data:
    question = Question(questions["question"], questions["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")