from pydantic import ValidationError
from models.user import User

data = {
    "name": "Punit",
    "email": "punit@gmail.com",
    "age": "25",
    "address": {
        "city": "Ahmedabad",
        "pincode": 380001
    }
}

try:
    user = User(**data)

    print("Validated Data:")
    print(user)

    print("\nJSON Output:")
    print(user.model_dump_json(indent=4))

except ValidationError as e:
    print("Validation Error:")
    print(e)

print("\nAccessing Individual Fields:")