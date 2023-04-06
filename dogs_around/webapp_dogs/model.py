from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# таблица для связи многие-ко многим владелец-собака, так как у собаки может быть более 1 владельца
association_table = db.Table('association',
        db.Column('user_id', db.String, db.ForeignKey('user.id_user')),
        db.Column('dog_id', db.String, db.ForeignKey('dog.id_dog'))
)

# а этот класс для отображаения "дружбы" между собаками
# status может принимать варианты accepted, declined, friendship - хранятся в config.py
class Friendship(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        sender_dog_id = db.Column(db.String, db.ForeignKey('dog.id_dog'))
        receiver_dog_id = db.Column(db.String, db.ForeignKey('dog.id_dog'))
        status = db.Column(db.String, default="pending")
        
        def accept_request(self):
                self.status = "accepted"
                db.session.commit()

        def decline_request(self):
                self.status = "declined"
                db.session.commit()


class Dog(db.Model):
        id_dog = db.Column(db.String, unique=True, primary_key=True, nullable=False)
        name_dog = db.Column(db.String, nullable=False)
        age_dog = db.Column(db.Integer, nullable=False, default=0)
        breed_dog = db.Column(db.String, nullable=False)
        response_date = db.Column(db.DateTime, nullable=False)
        city_dog = db.Column(db.String, nullable=True)
        foto_dog = db.Column(db.Blob, nullable=False)
        voice_dog = db.Column(db.Blob, nullable=False)
        users = db.relationship('User', secondary=association_table, back_populates='dogs')

        def get_friend_requests(self):
                #для получения списка всех запросов на дружбу для конкретной собаки
                friend_requests = Friendship.query.filter_by(receiver_dog_id=self.id_dog, status="pending").all()
                return friend_requests
        
        def send_friend_request(self, other_dog):
                #для получения списка всех запросов на дружбу для конкретной собаки
                friendship = Friendship(sender_dog_id=self.id_dog, receiver_dog_id=other_dog.id_dog)
                db.session.add(friendship)
                db.session.commit()

        #Эти методы будут находить соответствующий запрос 
        # на дружбу между двумя собаками и менять его статус на "подтвержденный" или "отклоненный"
        def accept_friend_request(self, other_dog):
                friendship = Friendship.query.filter_by(sender_dog_id=other_dog.id_dog, receiver_dog_id=self.id_dog).first()
                if friendship:
                        friendship.accept_request()

        def decline_friend_request(self, other_dog):
                friendship = Friendship.query.filter_by(sender_dog_id=other_dog.id_dog, receiver_dog_id=self.id_dog).first()
                if friendship:
                        friendship.decline_request()

        def __repr__(self):
                return f' Отзыв: {self.name_dog}, {self.breed_dog}, {self.age_dog}'


class User(db.Model):
        id_user = db.Column(db.String,unique=True, primary_key=True, nullable=False)
        first_name = db.Column(db.String, nullable=False)
        last_name = db.Column(db.String, nullable=False)
        user_name = db.Column(db.String, nullable=True)
        chat_id = db.Column(db.String,unique=True, nullable=True)
        subscribed = db.Column(db.Boolean, default=False)
        dogs = db.relationship('Dog', secondary=association_table, back_populates='users')


