import random

def score(candidate, target):
    ''' Score of fit  of candidate compared to target '''
    result = 0
    result_increase = 1
    for index in range(len(candidate)):
        if candidate[index] == target[index]:
            result += result_increase
    return result

def next_gen(gen_old, target):
    result = ""
    score_old = score(gen_old, target)
    for index in range(len(gen_old)):
        result += chr(65 + random.randrange(26) + 32 * random.randrange(2))
    return result

def create_gen(gen_length):
    result = ""
    for index in range(gen_length):
        result += "-"
    return result

def main():
    target = "Hello World"
    gen_new = create_gen(len(target))
    gen_old = create_gen(len(target))
    round = 0
    round_maximum = 10
    while(round < round_maximum):
        round += 1
        gen_new = next_gen(gen_old, target)
        gen_old = gen_new
        print(gen_new + " " + str(score(gen_new, target)))

if __name__ == '__main__':
    print('Hello World Genetic Algorithm')
    main()
