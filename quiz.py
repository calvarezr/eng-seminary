import yaml
import pandas as pd
import random
from collections import deque


class Quiz:
    def __init__(self, yaml_file, stats_file):
        with open(yaml_file, 'r') as file:
            self.questions = yaml.safe_load(file)
        self.stats_file = stats_file
        try:
            self.stats = pd.read_csv(stats_file, index_col='question')
        except FileNotFoundError:
            self.stats = pd.DataFrame(columns=['question', 'correct', 'total'])
            self.stats.set_index('question', inplace=True)


    def ask_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        answer = int(input("Your answer: "))
        return answer == question['answer']


    def update_stats(self, question, correct):
        if question in self.stats.index:
            self.stats.loc[question, 'total'] += 1
            if correct:
                self.stats.loc[question, 'correct'] += 1
        else:
            self.stats.loc[question] = [1, int(correct)]


    def save_stats(self):
        self.stats.to_csv(self.stats_file)


    def run_quiz(self, num_questions):
        questions = list(self.questions.keys())
        random.shuffle(questions)
        for question in questions[:num_questions]:
            correct = self.ask_question(self.questions[question])
            self.update_stats(question, correct)
        self.save_stats()


quiz = Quiz('questions.yaml', 'stats.csv')
quiz.run_quiz(10)