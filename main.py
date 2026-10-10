from calcs_if_new_to_chat import Calculations
from question_types import QuestionsType


calc = Calculations()

res = calc.get_question_distribution(decay=1, type = QuestionsType.MCQ)

sum = 0

for result in sorted(res, key=lambda x: x[1], reverse=True):
    sum += result[1]
    print(f"Name: {result[0]} | Probability: {result[1]}")
print(f'Total P: {sum}')