import bcrypt

def hash_password(password):
    """hash password"""
    password_en = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_en, salt)

    return hashed_password.decode('utf-8')

def check_password(pwd1, pwd2):
    return pwd1 == pwd2