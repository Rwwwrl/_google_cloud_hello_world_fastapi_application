from beanie import Document


class User(Document):
    name: str

    class Settings:
        name = "users"
