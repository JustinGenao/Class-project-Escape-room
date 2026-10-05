import time
name = input()
def room1():
    print(f'Open the door and enter the room {name}.')
    time.sleep(1)
    print('As you step inside you will find a riddle you must solve in order to get you passed level 1')
    time.sleep(5)
    print('Riddle goes like this:')
    time.sleep(2)
    print('If you have three apples and you take away two how many do you have?')
    time.sleep(2)
    print('You get 5 seconds to answer the riddle.')
    time.sleep(5)
    
    input('> ')


room1()
