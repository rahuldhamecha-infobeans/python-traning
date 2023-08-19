from school import Student, Mark,db

rahul = Student('Rahul',1)
vishal = Student('Vishal',2)
sagar = Student('Sagar',3)
sandeep = Student('Sandeep', 4)

db.session.add_all([rahul,vishal,sagar,sandeep])
db.session.commit()
db.session.commit()

for item in list(range(1,4)):
    student = Student.query.filter_by(roll_no=item).first()

    if rahul:
        mark_maths = Mark('Maths', 95, student.id)
        mark_science = Mark('Science', 90, student.id)
        mark_english = Mark('English', 84, student.id)
        db.session.add_all([mark_maths, mark_science, mark_english])
        db.session.commit()

    student = Student.query.filter_by(roll_no=1).first()
    print(student)

    print(student.report_marks())