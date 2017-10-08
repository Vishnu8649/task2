#chap3- problem 9
import re
def validate(S):
    '''
    Checks whether a phone number is
    valid or not

    '''
    if re.match('^[0-9]{10}$',S):
        print 'Valid mobile Number'
    else:
        print 'Not a valid mobile number'
    
validate('9846579333')
validate('966632522')
validate('09532233123')
