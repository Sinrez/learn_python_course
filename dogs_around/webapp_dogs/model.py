from flask_sqlalchemy import SQLAlchemy
import enum
from werkzeug.security import check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

def get_user_dogs(email):
        user = User.query.filter_by(email=email).first()  # ищем пользователя в базе данных по email
        if user:
                dogs = user.dogs  # получаем список собак, связанных с данным пользователем
                print(dogs)
                return dogs

#для обарботки статусов дружбы accepted, declined, friendship
class FrendStatusEnum(enum.Enum):
        pending = 0
        accepted = 1
        friendship = 2
        declined = 3

# таблица для связи многие-ко многим владелец-собака, так как у собаки может быть более 1 владельца
association_table = db.Table('association',
        db.Column('user_id', db.String, db.ForeignKey('user.id_user')),
        db.Column('dog_id', db.String, db.ForeignKey('dog.id_dog'))
)

# а этот класс для отображаения "дружбы" между собакой и собакой/собаками пользователя через пользовтеля класс User
# status может принимать варианты accepted, declined, friendship - хранятся в config.py
class Friendship(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        sender_dog_id = db.Column(db.String, db.ForeignKey('dog.id_dog'))
        receiver_dog_id = db.Column(db.String, db.ForeignKey('dog.id_dog'))
        status = db.Column(db.String, default=FrendStatusEnum.pending.value)
        
        def accept_request(self):
                self.status = FrendStatusEnum.accepted.value
                db.session.commit()

        def decline_request(self):
                self.status = FrendStatusEnum.declined.value
                db.session.commit()
        
        @classmethod
        def add_friendship(cls, sender_dog, receiver_user):
                # Создаем новый объект Friendship
                friendship = cls(sender_dog_id=sender_dog.id_dog, receiver_dog_id=receiver_user.dogs[0].id_dog)
                # Добавляем его в сессию для сохранения в базе данных
                db.session.add(friendship)
                db.session.commit()


class Dog(db.Model):
        id_dog = db.Column(db.String, unique=True, primary_key=True, nullable=False)
        name_dog = db.Column(db.String, nullable=False)
        age_dog = db.Column(db.Integer, nullable=False, default=0)
        breed_dog = db.Column(db.String, nullable=False)
        response_date = db.Column(db.DateTime, nullable=False)
        city_dog = db.Column(db.String, nullable=True)
        foto_dog = db.Column(db.String, nullable=True)
        voice_dog = db.Column(db.String, nullable=True)
        users = db.relationship('User', secondary=association_table, back_populates='dogs')

        def add_friend_request(self, user_id):
                friendship = Friendship(sender_dog_id=self.id_dog, receiver_dog_id=user_id)
                db.session.add(friendship)
                db.session.commit()

        def get_friends(self):
                friends = []
                friendships = Friendship.query.filter_by(status=FrendStatusEnum.accepted.value).all()
                for friendship in friendships:
                        if friendship.sender_dog_id == self.id_dog:
                                friend = Dog.query.filter_by(id_dog=friendship.receiver_dog_id).first()
                                if friend:
                                        friends.append(friend)
                        elif friendship.receiver_dog_id == self.id_dog:
                                friend = Dog.query.filter_by(id_dog=friendship.sender_dog_id).first()
                                if friend:
                                        friends.append(friend)
                        return friends

        def get_friend_requests(self):
                friend_requests = []
                requests_from_user = Friendship.query.filter_by(receiver_dog_id=self.id_dog, status=FrendStatusEnum.pending.value).all()
                print(requests_from_user)
                for req in requests_from_user:
                        print(f'req.sender_dog_id: {req.sender_dog_id}')
                        dog = Dog.query.filter_by(id_dog=req.sender_dog_id).first()
                        print(f'DOG {dog}')
                        if dog:
                                friend_requests.append(dog)
                        print(f'Список DOG {friend_requests}')
                return friend_requests


        def __repr__(self):
                return f'{self.id_dog}, {self.name_dog}, {self.breed_dog}, {self.age_dog}'
        


class User(db.Model):
        id_user = db.Column(db.String,unique=True, primary_key=True, nullable=False)
        first_name = db.Column(db.String, nullable=False)
        last_name = db.Column(db.String, nullable=False)
        user_name = db.Column(db.String, nullable=True)
        email = db.Column(db.String, nullable=False)
        password = db.Column(db.String, nullable=False)
        chat_id = db.Column(db.String,unique=True, nullable=True)
        subscribed = db.Column(db.Boolean, default=False, nullable=True)
        dogs = db.relationship('Dog', secondary=association_table, back_populates='users')

        def check_password(self, password):
                return check_password_hash(self.password, password)

        def is_active(self):
                # возвращает True, если пользователь активен, иначе - False
                return True
        
        def get_id(self):
                return str(self.id_user)
        
        def get_mail(self):
                return str(self.email)
        
        def is_authenticated(self):
                return True