message = 'a'

def greet(name):
    message = 'b'

def send_email():
    global message
    message = 'c'

greet('Mosh')
# send_email('nhan2151@gmail.com')
send_email()

print(message)