from basic_database import db,Peoples

all_Peopless = Peoples.query.all()
print(all_Peopless)

first = Peoples.query.get(1)
print(first.name)

filter = Peoples.query.filter_by(name='Rahul')

print(filter.all())


first.age = 30
first.name = 'darsh'

if first:
    db.session.add(first)
    db.session.commit()

second = Peoples.query.get(2)
if second :
    db.session.delete(second)
    db.session.commit()


all_Peopless = Peoples.query.all()
print(all_Peopless)