from flask import render_template, request, redirect, url_for, flash
from Teachent import *
from Teachent.models import Teacher, Student
from flask_login import login_required, login_user, logout_user, current_user
from Teachent.forms import LoginForm, StudentSignupForm


class DataHandler():
    def __init__(self):
        pass

    def getDataFromDataBase_ByName(self, namee):
        return Teacher.query.filter_by(name=namee).all()

    def getDataFromDataBase_ByUName(self, username):
        return Teacher.query.filter_by(username=username).first_or_404()

    def getDataFromDataBase_BySurName(self, surnamee):
        return Teacher.query.filter_by(surname=surnamee).all()

    def getDataFromDataBase_ByFullName(self, name, surname):
        return Teacher.query.filter_by(name=name, surname=surname).all()

    def checkUserExists_ByName(self, namee):
        return db.session.query(db.exists().where(Teacher.name == namee)).scalar()

    def checkUserExists_BySurName(self, surnamee):
        return db.session.query(db.exists().where(Teacher.surname == surnamee)).scalar()


'''class RedirectManager():
    def __init__(self):
        pass

    def redirectTo(self, index, users):
        return render_template(index, teachers=users)'''


class SearchHandler():
    def __init__(self):
        pass

    def searchContent(self, content, index):
        datahandler = DataHandler()
        empty = ""
        users = []
        if datahandler.checkUserExists_ByName(content):
            users = datahandler.getDataFromDataBase_ByName(content)

        if datahandler.checkUserExists_BySurName(content):
            users = datahandler.getDataFromDataBase_BySurName(content)

        elif " " in content:

            a = datahandler.checkUserExists_ByName(content.split()[0])
            b = datahandler.checkUserExists_BySurName(content.split()[1])
            if a and b:
                users = datahandler.getDataFromDataBase_ByFullName(content.split()[0], content.split()[1])
        if (len(users) == 0):
            empty = "m"
        return users, empty


class SearchPage:

    @app.route('/', methods=['GET', 'POST'])
    @app.route('/teachers', methods=['GET', 'POST'])
    def search():
        searchHdl = SearchHandler()
        if request.method == "POST":
            content = request.form['searchCon']
            users = searchHdl.searchContent(content, 'index.html')[0]
            empty = searchHdl.searchContent(content, 'index.html')[1]
            return render_template('index.html', teachers=users, empty=empty)

        users = Teacher.query.all()
        return render_template('index.html', teachers=users)


# app.add_url_rule('/teachers', view_func=SearchPage.search)

@login_manager.user_loader
def load_user(userid):
    return Student.query.get(int(userid))

#TODO
class UserLog:
    @app.route('/login', methods=["GET", "POST"])
    def login():

        form = LoginForm()
        if form.validate_on_submit():
            print(form.password.data)
            stu = Student.get_by_username(form.username.data)
            if stu is not None and stu.check_password(form.password.data):
                login_user(stu, form.remember_me.data)
                print("user found. redirecting...")
                flash("Logged in successfully as {}.".format(stu.username))
                return redirect(request.args.get('next') or url_for('search'))

            # flash('Incorrect username or password.')
        return render_template('login.html', form=form)

    # app.add_url_rule('/login.html', view_func=Login.login)
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('search'))

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        form = StudentSignupForm()
        if form.validate_on_submit():
            student = Student(email=form.email.data, \
                              username=form.username.data, \
                              password=form.password.data)
            db.session.add(student)
            db.session.commit()
            login_user(student)
            return redirect(url_for('search'))
        return render_template("signup.html", form=form)


class attendPage():
    @app.route('/attend')
    @login_required
    def attend():
        return render_template('attend.html')


class ProfilePage:

    @app.route('/teacher/<username>')
    def user(username):
        datah = DataHandler()
        user = datah.getDataFromDataBase_ByUName(username)
        return render_template('profile.html', user=user)


# app.add_url_rule('/teacher/<username>', view_func=ProfilePage.user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


app.run(debug=True)
