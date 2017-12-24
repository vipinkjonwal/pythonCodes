def emailSyntaxCheck(emailAddress):
    flag = 0
    while True:

        if not '@' in emailAddress:
            flag = -1
            print('ERROR: Absence of \'@\'')
            break

        elif emailAddress[1] == '.' or emailAddress[-1] == '.':
            print('ERROR: Email Address CAN\'T start/end with a \'.\' ')
            flag = -1
            break

        elif not emailAddress[-4] == '.' or emailAddress[-3] == '.':
            flag = -1
            print('ERROR: Uncategorised Extension.')
            break

        elif '..' in emailAddress:
            flag = -1
            print('.. NOT allowed.')
            break

        else:
            return True

    if flag == -1:
        return False

emailAddress = 'vipin.mca17.du@gmail.com'
boolValue = emailSyntaxCheck(emailAddress)

if boolValue == True:
    print(emailAddress,'is syntactically valid.')
else:
    print(emailAddress,'is NOT syntactically valid.')


