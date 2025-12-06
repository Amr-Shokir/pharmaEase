from models.user_model import UserModel

class UserRepository:
    def __init__(self):
        self.db = UserModel()

    def get_all(self):
        return self.db.get_all()

    def get_by_id(self, user_id):
        return self.db.find_by_id(user_id)

    def authenticate(self, email, password):
        all_users = self.db.get_all()
        for user in all_users:
            if user['email'] == email and user['password_hash'] == password:
                return user
        return None

    def create_user(self, username, email, password):
        new_user = {
            'username': username,
            'email': email,
            'password_hash': password
        }
        return self.db.create(new_user)
