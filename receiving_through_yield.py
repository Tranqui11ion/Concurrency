# def greet():
#     friend = yield
#     print(f'Hello, {friend}')
#
# g = greet()
# g.send(None) #priming the generator
# g.send('Adam')

from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')

def greet(g):
    yield from g  # same as below code
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')

greeter.send('Hello')

greeter.send('Hello')