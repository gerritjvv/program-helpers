# Making dataclasses subscriptable
# If you're a true dynamic programmer and start out with Dict[str, Any] but later want to gradually introduce dataclasses where needed,
# this trick helps create a dataclass that acts as a dictionary

from dataclasses import dataclass

@dataclass
class Product:
    id: str
    name: str

    def __getitem__(self, key):
        return self.__getattribute__(key)
    
    def __setitem__(self, key, value):
        self.__setattr__(key, value)


p = Product(id='123', name='Test')
print(p['id'])

p['a'] = 2
print(p.__dict__)

