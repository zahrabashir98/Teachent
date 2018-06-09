#! /usr/bin/env python

from Teachent import app, db
from Teachent.models import Teacher, Student
from flask_script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(Teacher(age="20", konkoorRank="636", madrak="فوق دیپلم", reshte="مهندسی کامپیوتر", \
                           username="shariat", email="arian@yahoo.com", name="آرین", surname="شریعت", \
                           courses="ریاضی", university="علم و صنعت ایران", \
                           number='09128219726', rank='10,10', picLink="../static/img/man.jpg"))
    # teachers.ad("shariat")

    db.session.add(Teacher(age="30", konkoorRank="200", madrak="فوق دکترا", reshte="دندانپزشکی", \
                           username="sharifi", email="sharifi@yahoo.com", name="دکتر", surname="شریفی", \
                           courses="زیست شناسی", university="آکسفورد", \
                           number='09121234567', rank='5,10', picLink="../static/img/man2.jpg"))

    db.session.add(Teacher(age="21", konkoorRank="736", madrak="فوق دیپلم", reshte="مهندسی کامپیوتر", \
                           username="ali", email="alierfanian@yahoo.com", name="علی", surname="عرفانیان", \
                           courses="ریاضی-فیزیک", university="تهران", \
                           number='09384665912', rank='10,10', picLink="../static/img/man3.jpg"))

    db.session.add(Teacher(age="19", konkoorRank="676", madrak="فوق دیپلم", reshte="مهندسی کامپیوتر", \
                           username="qazale", email="qazale@yahoo.com", name="غزاله", surname="بختیاری", \
                           courses="شیمی", university="علم و صنعت ایران", \
                           number='09128212226', rank='10,10', picLink="../static/img/woman2.jpg"))

    db.session.add(Teacher(age="19", konkoorRank="716", madrak="فوق دیپلم", reshte="مهندسی کامپیوتر", \
                           username="Mahsa", email="mahsa@yahoo.com", name="مهسا", surname="انوریان", \
                           courses="ورزش", university="علم و صنعت ایران", \
                           number='09128349726', rank='10,10', picLink="../static/img/woman.jpg"))
    db.session.add(Teacher(age="20", konkoorRank="100016", madrak="فوق دیپلم", reshte="مهندسی کامپیوتر", \
                           username="Zahra", email="zahra@yahoo.com", name="زهرا", surname="بشیر", \
                           courses="هیچی", university="علم و صنعت ایران", \
                           number='09121349726', rank='10,10', picLink="../static/img/woman3.jpg"))

    db.session.add(Student(age='20', username='ariansh.exe', email='arian_fr2@yahoo.com', name='Arian', \
                           surname='Shariat', password='Arjen71'))
    # teachers.ad("sharifi")
    db.session.commit()
    print('Initialized the database')


'''@manager.command
def update():'''


@manager.command
def dropdb():
    if prompt_bool(
            "Are you sure you want to lose all your data"):
        db.drop_all()
        print('Dropped the database')


if __name__ == '__main__':
    manager.run()
