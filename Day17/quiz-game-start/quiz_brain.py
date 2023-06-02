class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        question = self.question_list[self.question_number].text
        self.question_number += 1
        answer=input(f"Q.{self.question_number} : {question} (true/False) : ")

    def still_has_questions(self):
        return self.question_number<len(self.question_list)

    def

