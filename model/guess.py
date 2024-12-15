
class Guess:
    def __init__(self, guess, correct_number=None, correct_location=None):
        self.guess_value = guess
        self.correct_number = correct_number
        self.correct_location = correct_location

    def judge_guess(self, answer):
        # method that evaluates the correct_number and correct_location for a guess & updates the guess model
        correct_number = 0
        correct_location = 0
        answer_count = {}

        for num in answer:
            answer_count[num] = answer_count.get(num, 0) + 1

        for i, num in enumerate(self.guess_value):
            if num == answer[i]:
                correct_location += 1
            if num in answer_count and answer_count[num] > 0:
                correct_number += 1
                answer_count[num] -= 1

        self.correct_number = correct_number
        self.correct_location = correct_location
