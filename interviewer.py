# Interviewer.py

# CrewAI agents and logic for interview questions and feedback.

class Interviewer:
    def __init__(self):
        self.questions = []
        self.feedback = ''

    def add_question(self, question):
        self.questions.append(question)

    def conduct_interview(self):
        for question in self.questions:
            answer = input(question)
            self.provide_feedback(answer)

    def provide_feedback(self, answer):
        # Logic for providing feedback based on the answer
        self.feedback += f'Feedback for answer: {answer}\n'

    def show_feedback(self):
        print(self.feedback)