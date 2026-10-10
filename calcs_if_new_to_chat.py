import loader
import math
from question_types import QuestionsType

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
    
    def get_question_distribution(self, decay = 1, type=QuestionsType):
        exams = self.exams
        
        # (age, probability array)
        distribution = []
        
        # collect probabilities of each tag type occurinng in TF questions for all the exams, throw that in distributions array
        for exam in exams:
            # Find the section in the list where the 'type' matches the requested type
            section = next((s for s in exam['sections'] if s.get('type') == type.value), None)
            
            # should never hit
            if not section:
                print(f"something bad happened, {exam['exam_id']} has no section type {type.value}")
                continue
                
            questions = section['items']
            results = []
            pts = section['points']
            
            for question in questions:
                for tag in question['tags']:
                    if tag not in [tag_r for tag_r, weight in results]:
                        results.append((tag, (question['points'] / (pts * len(question['tags'])))))
                    else:
                        index = [tag_r2 == tag for tag_r2, weight in results].index(True)
                        results[index] = (tag, results[index][1] + (question['points'] / (pts * len(question['tags']))))            
            distribution.append((exam['age'], results))  
                    
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
            