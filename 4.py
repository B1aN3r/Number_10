from typing import List
from pydantic import BaseModel


class Person(BaseModel):
    age: int
    name: str
    children: list[dict]
    married: bool
    city: None

data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {
            'age': 3,
            'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
}

person = Person(**data)
print(person.children)
