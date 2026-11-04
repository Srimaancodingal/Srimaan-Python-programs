class India:
    def capital(self):
        print ("Capital of India is Delhi")

    def language(self):
        print ("Hindi is the national language of India")

    def type(self):
        print ("India is a developing country")

class Japan:
    def capital(self):
        print ("Capital of Japan is Tokyo")

    def language(self):
        print ("Japanese is the national language of Japan")

    def type(self):
        print ("Japan is a developing country")

Ind = India ()
Jpn = Japan ()

for i in (Ind , Jpn):
    i.capital()
    i.language()
    i.type () 

