from datetime import datetime
from pydantic import BaseModel


class BarModel(BaseModel):
    whatever: int


print(BarModel(whatever=23).json())

class Foo(BaseModel):
    a:BarModel
    bar:datetime
    orange:str
c=Foo(a={"whatever":5})
c.json()
a.whatever=5
m = Foo(a={"whatever":5})

print(m.json())