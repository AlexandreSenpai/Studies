'''Generating infinite numbers'''

def infinite() -> int:
    num = 0

    while True:
        yield num
        num += 1

# If you want to get the "next" value from a generator, use next() function.

GENERATOR = infinite()

print(next(GENERATOR)) # 0
print(next(GENERATOR)) # 1
print(next(GENERATOR)) # 2

# Commonly used for bash test purposes

'''Generating infinite commands'''

# For example, imagine that you're building a personal assistant and you have to generate a bunch of voice commands but you dont want to allocate any memory for it.

def generate_commands() -> str:
    while True:
        try:
            command = input(': ') # Imagine that you receive a microphone input right here.

            yield command
        except Exception as err:
            print('inaudible voice.') # Simulating a loss of voice recognition.
            print(err)
    
def do_something(command: str): print(command)

for command in generate_commands():
    do_something(command)

''' OUTPUT
    <- comando1
    -> comando1
    <- comando2
    -> comando2
'''