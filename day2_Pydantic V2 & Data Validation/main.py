
from user import User

user = User(
    name="Jabir",
    age=22,
    email="jabir@gmail.com"
)

print(user.model_dump())