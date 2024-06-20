class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def __str__(self):
    #     return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)
        #print(self.age)

p1 = Person("Lokesh", 26)
p1.age = 40

# print(p1.name, p1.age)
# print(p1)

p1.myfunc()
del p1

p1.myfunc()