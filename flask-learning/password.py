from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash,check_password_hash

# bcrypt = Bcrypt()
#
# password = 'Admin@123'
#
# hased = bcrypt.generate_password_hash(password=password)
#
# print(hased)
#
# check = bcrypt.check_password_hash(hased,'Admin@123')
#
# print(check)

hashed = generate_password_hash('Admin@123')
print(hashed)

check = check_password_hash(hashed,'Admin@123')
print(check)