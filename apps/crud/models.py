from apps.app import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    contents = db.Column(db.String)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
