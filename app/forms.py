from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class General(FlaskForm):
    fname = StringField('First Name:', validators=[InputRequired()])
    lname = StringField('Last Name:', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class AboutYou(FlaskForm):
    sex = SelectField('Sex', choices=[(0, 'Female'), (1, 'Male')])
    age = SelectField(
        'Age', choices=[(19, '19'), (20, '20'), (21, '21'), (22, '22')])
    height = StringField('Height:', validators=[InputRequired()])
    ethnicity = SelectField('What is your ethnicity?', choices=[(
        'Black', 'Black (Coloured)'), ('Chinese', 'Chinese'), ('White', 'White'), ('Indian', 'Indian')])
    personality = SelectField('What is your personality type?', choices=[(
        'Introvert', 'Introvert'), ('Extrovert', 'Extrovert'), ('Ambivert', 'Ambivert')])

    work = SelectField('To which work area do you belong?', choices=[
        ('Business', 'Business'), ('Education', 'Education'), ('Science', 'Science'), ('Technology', 'Technology'), ('Construction', 'Construction'), ('Communication', 'Communication'), ('Law', 'Law')])

    leadership = SelectField('How would you describe your leadership style?', choices=[(
        'Democratic', 'Democratic'), ('Autocratic', 'Autocratic'), ('Laissez-Faire', 'Laissez-Faire')])

    education = SelectField('Which is your level of education?', choices=[('Bachelors', 'Bachelors'), (
        'Masters', 'Masters'), ('PhD', 'PhD'), ('Diploma', 'Diploma'), ('Associate Degree', 'Associate Degree')])
    
    hobby = StringField('What is your favourite hobby?', validators=[InputRequired()])
