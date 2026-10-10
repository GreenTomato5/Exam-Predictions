import loader
import math

exam_loader = loader.exam_loader()

class Calculations:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Calculations, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.exams = exam_loader.get_exams()
    
    def exam_info(self):
        pass
    
    def get_mcq_distribution(self):
        pass
    
    def get_frq_distribution(self):
        pass
            
    def get_tf_distribution(self, decay = 1):
        exams = self.exams
        
        # (age, probability array)
        distribution = []
        
        # collect probabilities of each tag type occurinng in TF questions for all the exams, throw that in distributions array
        for exam in exams:
            questions = exam['sections']['type' == 'TF']['items']
        
            results = []
            pts = exam['sections']['type' == 'TF']['points']
            
            for question in questions:
                for tag in question['tags']:
                    if tag not in [tag_r for tag_r, weight in results]:
                        results.append((tag, (question['points']/(pts*len(question['tags'])))))
                    else:
                        index = [tag_r2 == tag for tag_r2, weight in results].index(True)
                        results[index] = (tag, results[index][1] + (question['points'] / (pts * len(question['tags']))))            
            distribution.append((exam['age'], results))      
            
        print(distribution[0])  
        
        # normalize the probabilities so unc exams are less important
        # (tag, probability)
        probabilities = []
        
        # configure decay
        lmda = decay
        
        total_age = sum(math.e**(-lmda * age) for age, result in distribution)

        # exam dist is (age, array)
        for exam_dist in distribution:
            # tag is (name, probabiliti)
            for tag in exam_dist[1]:
                tag = (tag[0], tag[1] * ((math.e**(-lmda * exam_dist[0]))/total_age))
                
                if tag[0] not in [tag_r for tag_r, weight in probabilities]:
                    probabilities.append(tag)
                else:
                    index = [tag_r == tag[0] for tag_r, weight in probabilities].index(True)
                    probabilities[index] = (tag[0], probabilities[index][1] + tag[1]) 
            
        return probabilities
            
calc = Calculations()

res = calc.get_tf_distribution(decay=4)

sum = 0

for result in sorted(res, key=lambda x: x[1], reverse=True):
    sum += result[1]
    print(f"Name: {result[0]} Probability: {result[1]}")
print(f'Total P: {sum}')