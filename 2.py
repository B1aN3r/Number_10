import pickle


class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'My name is {self.name} and i am {self.age} years old'

m = Man('Sasha', 23)

# сохраним объект
with open("man.pickle", "wb") as file:
    pickle.dump(m, file)

# загрузим его
with open("man.pickle", "rb") as file:
    m2 = pickle.load(file)

print(m)
print(m2)
