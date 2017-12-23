import re

'''
A password will be considered valid if it's length is more than 8, must contain small cases,
capital cases letter, a number, and a special character.
'''

def validatePassword(password):
    flag = 0
    while 1:
        if len(password) < 8:
            flag = -1
            break

        elif not re.search("[a-z]",password):
            flag = -1
            break

        elif not re.search("[A-Z]",password):
            flag = -1
            break

        elif not re.search("[0-9]", password):
            flag = -1
            break

        elif not re.search("[`~!@#$%^&*_]", password):
            flag = -1
            break

        else:
            return True

    if flag == -1:
        return False



