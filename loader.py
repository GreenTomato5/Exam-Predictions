import json
import os

class exam_loader:
    
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(exam_loader, self).__new__(self)
        return self.instance
    
    def __init__(self):
        self.data = []
        self.exam_path = 'Data/Known-Exams/JSON/files/'
        self.excluded_exams = ['exam_schema.json']
    

    def get_exams(self):
        if (self.data == []):
            for exam in os.listdir(self.exam_path):
                if exam.endswith('.json') and exam not in self.excluded_exams:
                    with open(os.path.join(self.exam_path, exam), 'r') as f:
                        self.data.append(json.load(f))
        return self.data
            
                
            