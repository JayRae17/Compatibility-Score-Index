"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, SignUp, SignUpOrgnzr, AboutYou
# from app.forms import AboutYou
from werkzeug.security import check_password_hash
from app.models import GeneralUser, Regular, Organizer, Grouped, joinGroup, Scores


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():

        # Query if User exists
        user = db.session.query(GeneralUser).filter_by(
            username=form.username.data).first()

        # If valid credentials, flash success and redirect
        if user is not None and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard', username=current_user.username))

        # Flash error message with incorrect username/password
        flash(u'Invalid Credentials', 'danger')
    return render_template("login.html", form=form)




@app.route("/logout")
@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))


@app.route('/register')
def register():
    """Render the website's register page."""
    form = LoginForm()
    if request.method == "POST":
        # change this to actually validate the entire form submission
        # and not just one field
        if form.username.data:
            # Get the username and password values from the form.

            # using your model, query database for a user based on the username
            # and password submitted. Remember you need to compare the password hash.
            # You will need to import the appropriate function to do so.
            # Then store the result of that query to a `user` variable so it can be
            # passed to the login_user() method below.

            # get user id, load into session
            # login_user(user)

            # remember to flash a message to the user
            # they should be redirected to a secure-page route instead
            return render_template('about_you.html')
    return render_template('register.html', form=form)



@app.route('/registerRegular/', methods=["GET", "POST"])
def registerRegular():
    # First Name, Last Name, Email, Password and Username are collected from the SignUp Form
    form = SignUp()

    if request.method == "POST" and form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        username = form.username.data
        password = form.password.data
        email = form.email.data


        # Checks in User Table if another user has this username
        existing_username = db.session.query(GeneralUser).filter_by(username=username).first()

        # Checks in User Table if another user has this email address
        existing_email = db.session.query(GeneralUser).filter_by(email=email).first()

        if existing_username is None and existing_email is None:
             #JADA ADDED
            user = GeneralUser(type = "regular", first_name = fname, last_name=lname, occupation = "", username = username, password = password, email = email)
            db.session.add(user)
            # Adds a regular user info to the database
            db.session.commit()
            
            # Success Message Appears
            flash('successfully registered', 'success')

            # return redirect(url_for("aboutRegular"))
            login_user(user)
            return redirect(url_for('dashboard', username=current_user.username))
    flash_errors(form)
    return render_template("signup.html", form=form)


@app.route('/registerOrganizer/', methods=["GET", "POST"])
def registerOrgnzr():
    form = SignUpOrgnzr()

    if request.method == "POST" and form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        occupation = form.occupation.data
        username = form.username.data
        password = form.password.data
        email = form.email.data


        # Checks in User Table if another user has this username
        existing_username = db.session.query(GeneralUser).filter_by(username=username).first()

        # Checks in User Table if another user has this email address
        existing_email = db.session.query(GeneralUser).filter_by(email=email).first()

        if existing_username is None and existing_email is None:
             #JADA ADDED
            user = GeneralUser(type = "organizer", first_name = fname, last_name=lname, occupation = occupation, username = username, password = password, email = email)
            db.session.add(user)
            # Adds a regular user info to the database
            db.session.commit()
            
            # Success Message Appears
            flash('successfully registered', 'success')

            login_user(user)
            return redirect(url_for('dashboard', username=current_user.username))    #JADA ADDED
    flash_errors(form)
    return render_template("signupOrgnzr.html", form=form)




@app.route('/dashboard/<username>')
@login_required
def dashboard(username):
    """Render the website's dashboard page."""
    return render_template('dashbrd.html', user = db.session.query(GeneralUser).filter_by(username = username).first())



@app.route('/aboutRegular/', methods=["GET", "POST"])
def aboutRegular():
    form = AboutYou()

    if request.method == "POST" and form.validate_on_submit():
        sex = form.sex.data
        age = form.age.data
        height = form.height.data
        ethnicity = form.ethnicity.data
        personality = form.personality.data
        work = form.work.data

        leadership = form.leadership.data
        education = form.education.data
        hobby = form.hobby.data

        faculty = form.faculty.data


        user = Regular(ethnicity = ethnicity, age = age, height = height, personality = personality, leadership = leadership, gender = sex, hobby = hobby, education = education, faculty = faculty, work = work)
        db.session.add(user)
            
        db.session.commit()
               
        flash('successfully registered', 'success')

        return redirect(url_for('dashboard', username=current_user.username)) 
# in the case the data is not saved in the database

    return render_template('about_you.html', form=form)



@app.route('/results',  methods=['GET', 'POST'])
def result():
    """Render the website's result page."""
    return render_template('results.html')

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return GeneralUser.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('login'))
###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

# Flash errors from the form if validation fails


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
