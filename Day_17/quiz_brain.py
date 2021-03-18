class QuizBrain:
    
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"The correct answer is: {c_answer}")
        print(f"Your score is: {self.score}/{self.question_number} \n")
        
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(answer, current_question.answer)