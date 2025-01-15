import datetime

class StudentDomain:
    def __init__(self, student_id: str, name: str, email: str):
        self.ID = student_id
        self.Name = name
        self.Email = email
        self.Passwords = []
        self.CreatedAt = datetime.now()
        self.Active = True

    def to_json(self):
        return {
            "id": self.ID,
            "name": self.Name,
            "email": self.Email,
            "passwords": [password.Hash for password in self.Passwords],
            "createdAt": self.CreatedAt,
            "updatedAt": self.UpdatedAt,
            "active": self.Active
        }

class PasswordDomain:
    def __init__(self, hash: str):
        self.Hash
        self.CreatedAt = datetime.min()

    def to_json(self):
        return {
            "hash": self.Hash,
            "createdAt": self.CreatedAt
        }