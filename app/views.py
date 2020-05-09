"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import math
import random
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, SignUp, AboutYou, Groupings, newGroup, joinNewGroup, TranferGrp, Criteria
from werkzeug.security import check_password_hash
from app.models import User, Regular, Organizer, Sets, joinSet, Scores, formedGrps
from sqlalchemy.sql import alias, select
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
        user = db.session.query(User).filter_by(
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






@app.route('/registerAs', methods=["GET", "POST"])
def registerAs():
    """Render the website's register page."""
    if request.method == "POST":
        if request.form.get('Regular') == 'Regular':
            return redirect(url_for('register', typeUser="Regular"))

        elif request.form.get('Organizer') == 'Organizer':
            return redirect(url_for('register', typeUser="Organizer"))
    return render_template('registerAs.html')






@app.route('/register/<typeUser>', methods=["GET", "POST"])
def register(typeUser):
    # First Name, Last Name, Email, Password and Username are collected from the SignUp Form
    form = SignUp()

    if request.method == "POST" and form.validate_on_submit():
        # Collects username and email info from form
        username = form.username.data
        email = form.email.data

        # Checks if another user has this username
        existing_username = db.session.query(
            User).filter_by(username=username).first()

        # Checks if another user has this email address
        existing_email = db.session.query(User).filter_by(email=email).first()

        # If unique email address and username provided then log new user
        if existing_username is None and existing_email is None:
            if typeUser == "Regular":
                user = Regular(type=typeUser, first_name=request.form['fname'], last_name=request.form['lname'],
                               email=request.form['email'], username=request.form['username'], password=request.form['password'], gender="", age="", height="", leadership="", ethnicity="", personality="", education="", hobby="", faculty="", work="")
            else:
                user = Organizer(type=typeUser, first_name=request.form['fname'], last_name=request.form['lname'],
                                 email=request.form['email'], username=request.form['username'], password=request.form['password'], occupation="")
            # Adds a regular user info to the database
            db.session.add(user)
            db.session.commit()

            # Success Message Appears
            flash('Successfully registered', 'success')

            # Logs in a newly registered user
            login_user(user)

            # Redirects to Profile Page
            return redirect(url_for('dashboard', username=user.username))

    return render_template("signup.html", form=form)





@login_required
@app.route('/<username>/createSet',  methods=['GET', 'POST'])
def createSet(username):
    """Render the website's  page."""
    form = newGroup()
    if request.method == "POST" and form.validate_on_submit():
        set_name = form.group_name.data

        if set_name is not None:
            sets = Sets(
                set_name=set_name, purpose=request.form['purpose'], administrator=current_user.user_id)

            # Adds a regular user info to the database
            db.session.add(sets)
            db.session.commit()

            # Success Message Appears
            flash('Set Added', 'success')

            # Redirects to Profile Page
            return redirect(url_for('dashboard', username=current_user.username))
    return render_template('createGroup.html', form=form)





@login_required
@app.route('/<username>/joinSet',  methods=['GET', 'POST'])
def joinASet(username):
    """Render the website's  page."""
    form = joinNewGroup()
    if request.method == "POST" and form.validate_on_submit():
        # Collects username and email info from form
        # group_name = form.group_name.data
        scode = form.group_code.data

        # Checks if another user has this username
        existing_set = db.session.query(Sets).filter_by(code=scode).first()

        # If valid credentials, flash success and redirect
        if existing_set.code == scode:
            join_st = joinSet(user_id=current_user.user_id, set_id=existing_set.set_id)

            db.session.add(join_st)
            db.session.commit()

            flash('Successfully Added to a Set','success')

            # return redirect(url_for('dashboard', username=current_user.username))

        return redirect(url_for('dashboard', username=current_user.username))
    return render_template('joinGroup.html', form=form)





@login_required
@app.route('/members/<set_id>',  methods=['GET', 'POST'])
def members(set_id):
    set_name = Sets.query.filter_by(set_id=set_id).first()

    if current_user.type == "Organizer":
        # groups = db.session.query(formedGrps2).filter_by(group_id=gp_id).all()
        # if groups :

        getMembers = (db.session.query(joinSet, Regular, User).join(joinSet).filter_by(set_id=set_id).all())
        """Render the website's  page."""
        
        form = Groupings()
        if request.method == "POST" and form.validate_on_submit():

            grpBy = form.grpBy.data
            numPersons = form.numPersons.data

            # CALCULATES THE AMOUNT OF GROUPS BASED ON NUMBER ENTERED
            length = len(getMembers)
            grpAmt = length/int(numPersons)
            grpAmt = math.ceil(grpAmt)

            # SAVES ALL THE NAMES IN THE SPECIFIC SET TO 'MBRNAMES'
            mbrIDs = (db.session.query(Regular.user_id).join(joinSet, Regular.user_id == joinSet.user_id).filter_by(set_id=set_id).all())


            lst = []
            for i in mbrIDs:
                lst.append(mbrIDs)

            x = 0
            for i in range(lst):
                x+=1
                for a in range(grpAmt):
                    grp = formedGrps(grp_id = x,set_id= set_id, user_id = user_id, criteria=str(grpBy)) 

            # NEEDS WORK!!!
                
                db.session.add(grp)
                db.session.commit()
                # if len(lst) == 1:
                #     mini = formedGrps2(group_id= gp_id, mbr1=lst[0], mbr2="", criteria=str(grpBy))
                # else:
                #     break


            return redirect(url_for('Groups', set_id = set_id, numPersons = numPersons, mbrIDs = mbrIDs))

    return render_template('members.html', getMembers=getMembers, set_name= set_name, set_id = set_id, form = form)
        
   




@login_required
@app.route('/Groups/<set_id>/<numPersons>/<mbrIDs>',  methods=['GET', 'POST'])

def Groups(set_id,numPersons,mbrIDs):
    allSets = Sets.query.filter_by(set_id=set_id).first()
    
    if int(numPersons) == 2:
        groups = db.session.query(formedGrps).filter_by(set_id=set_id).all()
    
    
    form2 = TranferGrp()
    if request.method == "POST" and form2.validate_on_submit():
        grpNum = form2.grpNum.data 
        grpNum2 = form2.grpNum2.data
        # return redirect
    return render_template('miniGrps.html', set_id = set_id, allSets=allSets, numPersons=numPersons, groups= groups, mbrIDs=mbrIDs,form2 = form2)



@app.route('/recommend/<username>', methods=['GET', 'POST'])
@login_required
def recommend(username):
    """Render the website's recommended matches page."""
    form = Criteria()
    if request.method == "POST":
        crit = form.crit.data
        
        if crit == "compatible":
            matches = (db.session.query(Scores, User).join(Scores, Scores.other_id == User.user_id).filter_by(user_id = current_user.user_id).order_by(Scores.score.desc()).limit(9).all())
        else:
            matches = (db.session.query(Scores, User).join(Scores, Scores.other_id == User.user_id).filter_by(user_id = current_user.user_id).order_by(Scores.score.asc()).limit(9).all())
        
        return render_template('recomnd.html', form = form, matches = matches)
    
    matches = (db.session.query(Scores, User).join(Scores, Scores.other_id == User.user_id).filter_by(user_id = current_user.user_id).order_by(Scores.score.desc()).limit(9).all())
    # each = Scores(user_id=current_user.user_id, other_id=13, score = 0.10)

    # db.session.add(each)
    # db.session.commit()



    return render_template('recomnd.html', form = form, matches=matches)




@app.route('/dashboard/<username>')
@login_required
def dashboard(username):
    """Render the website's dashboard page."""
    if current_user.type == "Organizer":
        getSets = Sets.query.filter_by(
            administrator=current_user.user_id).all()
    else:
        getSets = Sets.query.join(joinSet).filter_by(user_id=current_user.user_id).all()

    return render_template('dashbrd.html', sets=getSets)



@app.route('/about/<typeUser>', methods=["GET", "POST"])
def aboutUser(typeUser):
    # How am I going to pass the above information
    form = AboutYou()
    if request.method == "POST" and form.validate_on_submit():
        gender=request.form['sex']
        # JUST ADDED (CONTINUE WORKING ON IT!)
        pref_gender=request.form['pref_sex']

        age=request.form['age']
        height=request.form['height'] 
        leadership=request.form['leadership'] 
        ethnicity=request.form['ethnicity']
        # JUST ADDED (CONTINUE WORKING ON IT!)
        pref_ethnicity=request.form['pref_ethnicity']

        personality=request.form['personality'] 
        education=request.form['education']
        hobby=request.form['hobby'] 
        work=request.form['work']

        db.session.query(Regular).filter(Regular.user_id == current_user.user_id).update({Regular.gender: gender, Regular.age: age, Regular.height: height, Regular.leadership: leadership, Regular.ethnicity: ethnicity, Regular.personality: personality, Regular.education: education, Regular.hobby: hobby, Regular.work: work}, synchronize_session=False)


        # Adds a regular user info to the database
        db.session.commit()

        # Success Message Appears
        flash('Feautures saved!','success')

        # Redirect User to Main Page
        return redirect(url_for('dashboard', username=current_user.username))

        # if form entry is invalid, redirected to the same page to fill in required details
    return render_template('about_you.html', form=form)




@app.route('/results',  methods=['GET', 'POST'])
def result():
    """Render the website's result page."""
    return render_template('results.html')

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
