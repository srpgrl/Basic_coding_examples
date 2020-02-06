print(""""
************************
User Login Program
**********************""")

sys_username='serap'
sys_password="123456"
max_entry=3

while True:
    username=input('Please enter user name: ')
    password=input('Please enter password: ')
    if (sys_username != username and sys_password == password):
        print('Incorrect username')
        max_entry-=1

    elif (sys_username == username and sys_password != password):
        print('Incorrect passwprd')
        max_entry-=1

    elif (sys_username != username and sys_password != password):
        print('Incorrect username and password.')
        max_entry -= 1

    else:
        print('Successful Login....')

    if max_entry==0:
        print('Your right to login is over.....')
        break



