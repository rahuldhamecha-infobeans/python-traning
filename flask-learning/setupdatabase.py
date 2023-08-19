from basic_database import db, Peoples

db.create_all()

rahul = Peoples('Rahul',27)
vishal = Peoples('Vishal',26)


print(rahul.people_id)
print(vishal.people_id)

db.session.add_all([rahul,vishal])

db.session.commit()

print(rahul.people_id)
print(vishal.people_id)