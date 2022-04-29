import re

def email_parse(email_address):
    if re.search(r'\@', email_address) is None:
        print('Email address in wrong, please restart')
    else:
        pattern = re.split('@', email_address)
        if re.search(r'\.', pattern[1]) is None:
            print('Email address in wrong, please restart')
        else:
            res_dct = dict({'username': pattern[0], 'domain': pattern[1]})
            print(res_dct)

email_parse(input('Please enter email address: '))
