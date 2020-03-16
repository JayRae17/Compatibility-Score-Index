from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class General(FlaskForm):
    fname = StringField('First Name:', validators=[InputRequired()])
    lname = StringField('Last Name:', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class AboutYou(FlaskForm):
    sex = SelectField('Sex', choices=[(0, 'Female'), (1, 'Male')])

    age = SelectField(
        'Age', choices=[(19, '19'), (20, '20'), (21, '21'), (22, '22')])

    height = SelectField('Height', choices=[(142, '(4 ft 8 inches) 142 cm'), (
        144, '(4 ft 9 inches) 144 cm'), (147, '(4 ft 10 inches) 147 cm'), (149, '(4 ft 11 inches)  149 cm'), (152, '(5 ft 0 inches)	152 cm'), (154, '(5 ft 1 inches)	154 cm'), (157, '(5 ft 1 inches)	157 cm'), (160, '(5 ft 3 inches)	160 cm'), (162, '(5 ft 4 inches)	162 cm'), (165, '(5 ft 5 inches)	165 cm'), (168, '(5 ft 6 inches)	168 cm'), (170, '(5 ft 7 inches)	170 cm'), (172, '(5 ft 8 inches)	172 cm'), (175, '(5 ft 9 inches)	175 cm'), (177, '(5 ft 10 inches)	177 cm'), (180, '(5 ft 11 inches) 180 cm'), (183, '(6 ft 0 inches)	183 cm'), (185, '(6 ft 1 inches)	185 cm'), (188, '(6 ft 2 inches)	188 cm'), (191, '(6 ft 3 inches)	191 cm'), (194, '(6 ft 4 inches)	194 cm'), (196, '(6 ft 5 inches)	196 cm'), (198, '(6 ft 6 inches)	198 cm')])

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

    hobby = SelectField('What is your favourite hobby?', choices=[('Sports', 'Sports'), (
        'Music', 'Music'), ('Exercising', 'Exercising'), ('Shopping', 'Shopping'), ('Dancing', 'Dancing'), ('Watching TV', 'Watching TV'), ('Reading and Writing', 'Reading and Writing'), ('Arts', 'Arts')])
