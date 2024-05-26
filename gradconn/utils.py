import bcrypt

def hash_password(password):
    """hash password"""
    password_en = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_en, salt)

    return hashed_password.decode('utf-8')

def check_password(password, hashed_password):
    password_bytes = password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)

def check_name(name1, name2):
    return name1 == name2