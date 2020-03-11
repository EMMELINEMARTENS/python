# name = input('What is your name?')
from datetime import datetime
from sense_hat import SenseHat
first_name = 'Emmeline'
last_name = 'Martens'

output = 'Hello, {} {}'.format(first_name, last_name) 
print(output)

first_num = input('Enter first number ')
second_num = input('Enter second number ')
print(first_num + second_num)

# birthday_date = input('What is your Birthday (dd/mm/yyyy)?')

# birthday = datetime.strptime(birthday_date, '%d/%m/%Y')
# print(' Birthday: ' + str(birthday))

current_date = datetime.now()
print(str(current_date))





