class Employee:
    def __init__(self,id,name,occupation):
        self.id = id
        self.name = name
        self.occupation = occupation


    def do_work(self):
        if self.occupation == "tennis player":
            print (self.id,self.name,"plays tennis")
        elif self.occupation == "actors":
            print (self.id,self.name,"shoots a film")
        elif self.occupation == "dancer":
            print (self.id,self.name,"performs dancing")

    def speaks(self):
        if self.id == "1":
            print(self.id,self.name,"speaks english")
        elif self.id == "2":
            print(self.id,self.name,"speaks spanish")

tom = Employee("1","tom cruise","tennis player")
tom.do_work()
tom.speaks()
shara = Employee("2","Shara pova","actors")
shara.do_work()
shara.speaks()

