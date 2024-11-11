#cat entity
class Cat:
    #the consttructor:
    #constructor creates cat in code
    #to create a cat name and colour needed
    #self is the cat we are creating
    #__ is special__
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour
        self.age=1
        self.energy=50
        self.intelligence=5
        self.mass=5
    def train(self):
        print(f'{self.name} is training...')#put varibles directly into string
        self.energy-= 5
        self.intelligence+=1
        self.age += 0.1
        if self.energy<0 or self.intelligence<0 or self.age<60:
            print('cat is dead')
            return "DEAD"
    def feed(self):
        print(f'{self.name} is eating;...')
        self.energy += 10
        self.mass +=1 
        self.age +=0.1
    def play(self):
        print(f'{self.name} is playing...')
        self.energy -=10
        self.intelligence +=0.1
        self.age+=1
    def sleep(self):
        print(f'{self.name} is sleeping...')
        self.energy +=15
        self.intelligence +=0.01
        self.age+=2
    def show_stats(self):
        print(f'{'age is ',self.age,'energy is ',self.energy,'intelligence is ',self.intelligence,'mass is ',self.mass}')
        
    
#now make 2 cats
#these are called instances of cat
sid = Cat('sid','black')
mista= Cat('mista','white')

sid.train()
print(sid.intelligence)
print(mista.intelligence)