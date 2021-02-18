from dataclasses import dataclass, field, FrozenInstanceError

@dataclass
class Character:
    name: str = field(repr=False)
    age: int
    race: str
    height: float
    hp: int

myself = Character(name="Alexandre",
                   age=21,
                   race="Human",
                   height=1.80,
                   hp=10)

print(myself) # Character(name='Alexandre', age=21, race='Human', height=1.8, hp=10)

print(myself.name,
      myself.age,
      myself.height) # Alexandre 21 1.8

print(myself.__dict__) # {'name': 'Alexandre', 'age': 21, 'race': 'Human', 'height': 1.8, 'hp': 10}

@dataclass(frozen=True) # Creating unmutable dataclasses
class User:
    nickname: str
    email: str
    password: str
    remember_me: bool = field(default=False, repr=False)

user = User(nickname="AlexandreSenpai",
            email="alexandre@gmail.com",
            password="samplepassword123")

print(user) # User(nickname='AlexandreSenpai', email='alexandre@gmail.com', password='samplepassword123')

try:
    user.nickname = "SoraHikki"
except FrozenInstanceError as err:
    print('You cannot change a frozen class property. =(')

# Using __post_init__
@dataclass
class Calculations:
    num_1: int = field(default=10)
    num_2: int = field(default=155)
    res: int = field(default=0, repr=False)

    def __post_init__(self):
        self.res = self.num_1 + self.num_2

calc = Calculations()

print(calc.res) # 165

calc_2 = Calculations(num_1=99, num_2=872)

print(calc_2.res) # 971