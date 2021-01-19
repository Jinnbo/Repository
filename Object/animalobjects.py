# animalobjects.py
# practice object-oriented programming
# in the context of animals


class Animal():
    # constructor

    def __init__(self):
        self.name = "Unnamed"
        self.legs = 0
        #print("testing ")

# method

    def talk(self):
        if self.name != "Unnamed":
            print(f"Hello my name {self.name}!")
        else:
            print("Hello.")



# creating an animal object
some_animal = Animal()

# access properties
print(some_animal.name)
some_animal.name = "rex"
some_animal.legs = 2
print(some_animal.name)


# Create a new object
#   * name it whatever you like
#   * Give it 20 legs
#   * print out the name and legs


some_other_animal = Animal()
some_other_animal.name = "Jimbo"
some_other_animal.legs = 20
print(f"{some_other_animal.name}\n{some_other_animal.legs}")

print(type(some_other_animal))

some_other_animal.talk()