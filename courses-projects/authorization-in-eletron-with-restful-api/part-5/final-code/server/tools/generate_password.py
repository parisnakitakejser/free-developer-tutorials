
from passlib.hash import pbkdf2_sha512

print(pbkdf2_sha512.hash('123456'))