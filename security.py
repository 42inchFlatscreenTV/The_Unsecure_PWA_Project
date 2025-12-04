import bcrypt


def gen_salt():
    salt = bcrypt.gensalt()
    return salt


def hash_password(password):
    salt = gen_salt()
    hash = bcrypt.hashpw(password.encode(), salt)

    return hash, salt
