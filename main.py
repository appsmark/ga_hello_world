import random

def create():
    round = 0
    round_maximum = 10
    while(round < round_maximum):
        round += 1
        print('Hello World')
        output = ""
        for index in range(11):
            output += chr(65 + random.randrange(26) + 32 * random.randrange(2))
        print(output)

if __name__ == '__main__':
    print('GA Hello World')
    create()
