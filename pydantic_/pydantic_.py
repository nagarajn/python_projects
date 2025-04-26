
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int    

user = User(name="John", age=30)
print(user)