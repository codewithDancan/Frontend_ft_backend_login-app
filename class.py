class Person:
    x = 0
    nam = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)
        
q = Person('Dancan')  
m = Person('Vyoone')  
        
        
q.party()
m.party()
q.party()