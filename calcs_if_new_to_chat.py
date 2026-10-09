import loader
import random

loader = loader.exam_loader()

class calculations:
    
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(calculations, self).__new__(self)
        return self.instance
    
    
    def __init__(self):
        self.exams = loader.get_exams()
    
    def exam_info(self):
        exam = self.exams[random.randrange(0,len(self.exams) -1 , 1)]
        # print(f"Exam: {exam['exam_id']}")
        # print(f"Number of pts: {exam['total_points']}")
        # print(f"Sections: {exam['sections']}")
                    
        questions = exam['sections']['type' == 'TF']['items']
        
        results = []
        pts = exam['sections']['type' == 'TF']['points']
    
        for tf_question in questions:
            results.append((tf_question['points'], tf_question['tags']))
        
        print(f'Num pts: {pts}')
        # print(f'Questions and weight: {results}\n')
        
        qtap = []
        
        for item in results:
            if item[1] not in [tag for tag, weight in qtap]:
                qtap.append((item[1], item[0] / pts))
            else:
                index = [tag == item[1] for tag, weight in qtap].index(True)
                qtap[index] = (qtap[index][0], qtap[index][1] + (item[0] / pts))
        
        
        def get_ya(e):
            return e[1]
        
        
        for tap in qtap:
            print(tap, "\n")        
            
calc = calculations()

calc.exam_info() 