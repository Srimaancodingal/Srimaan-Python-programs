class bird:
    def __init__(self):
        print ("Construction for bird")

    def whoisthis (self):
        print ("Bird")

    def swim (self):
        print ("Swim faster")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print ("Constructer for penguin is created")

    def whoisthis (self):
        print ("Penguin")

    def run(self):
        print ("Run Faster")

p = penguin()
p.whoisthis()
p.swim ()
p.run ()

