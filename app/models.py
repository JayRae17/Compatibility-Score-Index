import string
import uuid
import random
from . import db
from app.models import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(255))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def __init__(self, type, first_name, last_name, email, username, password):
        self.type = type
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = generate_password_hash(
            password, method='pbkdf2:sha256')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.user_id)  # python 2 support
        except NameError:
            return str(self.user_id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)


class Organizer (User):
    __tablename__ = 'organizer'

    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.user_id'), primary_key=True)
    occupation = db.Column(db.String(30))
    groups = db.relationship('Grouped', backref='admin')

    def __init__(self, type, first_name, last_name, email, username, password, occupation):
        super().__init__(type, first_name, last_name, email, username, password)
        self.occupation = occupation

    __mapper_args__ = {
        'polymorphic_identity': 'Organizer'
    }


class Regular (User):
    __tablename__ = 'regular'

    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.user_id'), primary_key=True)
    gender = db.Column(db.String(50))
    age = db.Column(db.String(50))
    height = db.Column(db.String(50))
    leadership = db.Column(db.String(30))
    ethnicity = db.Column(db.String(30))
    personality = db.Column(db.String(30))
    education = db.Column(db.String(50))
    hobby = db.Column(db.String(50))
    work = db.Column(db.String(50))

    def __init__(self, type, first_name, last_name, email, username, password, gender, age, height, leadership, ethnicity, personality, education, hobby, work):
        super().__init__(type, first_name, last_name, email, username, password)
        self.ethnicity = ethnicity
        self.age = age
        self.height = height
        self.personality = personality
        self.leadership = leadership
        self.gender = gender
        self.hobby = hobby
        self.education = education
        self.work = work

    __mapper_args__ = {
        'polymorphic_identity': 'Regular'
    }


class Grouped (db.Model):
    __tablename__ = 'grouped'

    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(20), unique=True)
    purpose = db.Column(db.String(30))
    code = db.Column(db.String(10))
    administrator = db.Column(db.Integer, db.ForeignKey(
        'organizer.user_id'))

    def __init__(self, group_name, purpose, administrator):
        def random_Coder(lgth):
            """Generate a random string of letters, digits and special characters """
            return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(lgth))

        def random_Coder2(lgth):
            """Generate a random string of letters, digits and special characters Option 2"""
            return uuid.uuid4().hex.upper()[0:lgth]

        self.group_name = group_name
        self.purpose = purpose
        self.administrator = administrator
        # self.code = random_Coder(10)
        self.code = random_Coder2(10)

    def get_id(self):
        try:
            return unicode(self.group_id)  # python 2 support
        except NameError:
            return str(self.group_id)  # python 3 support

    def get_Code(self):
        try:
            return unicode(self.code)  # python 2 support
        except NameError:
            return str(self.code)  # python 3 support


class joinGroup(db.Model):
    __tablename__ = 'joingroup'

    user_id = db.Column(db.Integer, db.ForeignKey(
        'regular.user_id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey(
        'grouped.group_id'), primary_key=True)

    def get_id(self):
        try:
            return unicode(self.group_id)  # python 2 support
        except NameError:
            return str(self.group_id)  # python 3 support


class Scores(db.Model):
    __tablename__ = 'userscore'

    user_id = db.Column(db.Integer, db.ForeignKey(
        'regular.user_id'), primary_key=True)
    feature = db.Column(db.String(20), primary_key=True)
    weight = db.Column(db.DECIMAL(2, 1))



class formedGrps2(db.Model):
    __tablename__ = 'formedgrps2'

    minigrp_id = db.Column(db.Integer, primary_key=True)

    group_id = db.Column(db.Integer, db.ForeignKey('grouped.group_id'))

    mbr1 = db.Column(db.String(30))

    mbr2 = db.Column(db.String(30))

    criteria = db.Column(db.String(30))

    def __init__(self, group_id, mbr1, mbr2, criteria):
        self.group_id = group_id
        self.mbr1 = mbr1
        self.mbr2 = mbr2
        self.criteria = criteria



class formedGrps3(db.Model):
    __tablename__ = 'formedgrps3'

    minigrp_id = db.Column(db.Integer, primary_key=True)

    group_id = db.Column(db.Integer, db.ForeignKey('grouped.group_id'))

    mbr1 = db.Column(db.String(30))

    mbr2 = db.Column(db.String(30))

    mbr3 = db.Column(db.String(30))

    criteria = db.Column(db.String(30))

    def __init__(self, group_id, mbr1, mbr2, mbr3,criteria):
        self.group_id = group_id
        self.mbr1 = mbr1
        self.mbr2 = mbr2
        self.mbr3 = mbr3
        self.criteria = criteria



class formedGrps4(db.Model):
    __tablename__ = 'formedgrps4'

    minigrp_id = db.Column(db.Integer, primary_key=True)

    group_id = db.Column(db.Integer, db.ForeignKey('grouped.group_id'))

    mbr1 = db.Column(db.String(30))

    mbr2 = db.Column(db.String(30))

    mbr3 = db.Column(db.String(30))

    mbr4 = db.Column(db.String(30))

    criteria = db.Column(db.String(30))

    def __init__(self, group_id, mbr1, mbr2, mbr3, mbr4, criteria):
        self.group_id = group_id
        self.mbr1 = mbr1
        self.mbr2 = mbr2
        self.mbr3 = mbr3
        self.mbr4 = mbr4
        self.criteria = criteria


class formedGrps5(db.Model):
    __tablename__ = 'formedgrps5'

    minigrp_id = db.Column(db.Integer, primary_key=True)

    group_id = db.Column(db.Integer, db.ForeignKey('grouped.group_id'))

    mbr1 = db.Column(db.String(30))

    mbr2 = db.Column(db.String(30))

    mbr3 = db.Column(db.String(30))

    mbr4 = db.Column(db.String(30))

    mbr5 = db.Column(db.String(30))

    criteria = db.Column(db.String(30))

    def __init__(self, group_id, mbr1, mbr2, mbr3, mbr4, mbr5, criteria):
        self.group_id = group_id
        self.mbr1 = mbr1
        self.mbr2 = mbr2
        self.mbr3 = mbr3
        self.mbr4 = mbr4
        self.mbr5 = mbr5
        self.criteria = criteria





    