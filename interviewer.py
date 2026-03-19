# Interviewer.py

import requests

class CrewAI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_web_dev_questions(self):
        url = 'https://api.groq.com/getWebDevQuestions'
        headers = {'Authorization': f'Bearer {self.api_key}' }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['questions']
        return []

    def get_feedback(self, answers):
        url = 'https://api.groq.com/getFeedback'
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        response = requests.post(url, json={'answers': answers}, headers=headers)
        if response.status_code == 200:
            return response.json()['feedback']
        return "No feedback available."

# Example usage:
# crew_ai = CrewAI(api_key='your_api_key_here')
# questions = crew_ai.get_web_dev_questions()
# feedback = crew_ai.get_feedback(['answer1', 'answer2'])