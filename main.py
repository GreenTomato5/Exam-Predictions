from calcs_if_new_to_chat import Calculations
from question_types import QuestionsType


calc = Calculations()

mc = calc.get_question_distribution(decay=1, type = QuestionsType.MCQ)
frq = calc.get_question_distribution(decay=1, type = QuestionsType.FRQ)
tf = calc.get_question_distribution(decay=1, type = QuestionsType.TF)


def get_results(res, label):
    sum=0
    print(f"XXXXXX These are the results for {label} XXXXXX")
    for result in sorted(res, key=lambda x: x[1], reverse=True):
        sum += result[1]
        print(f"Name: {result[0]} | Probability: {result[1]}")
    print(f'Total P: {sum}')
    
get_results(mc, 'MCQ')
get_results(frq, 'FRQ')
get_results(tf, 'True False')