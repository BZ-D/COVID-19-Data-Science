import random

door_1 = 'lamb_1'
door_2 = 'lamb_2'
door_3 = 'car'
res = ''
n = int(input('Input the times you want to experiment: '))
count = 0

print('Now host opens another door, and a lamb is behind it. ')
ifChange = input('Now do you want to change to another door? Y/N: ')

for i in range(n):

    choice = random.randint(1, 3)

    if choice == 1:
        res = door_1
        hostChoice = door_2

    elif choice == 2:
        res = door_2
        hostChoice = door_1

    else:
        res = door_3
        tmp = random.randint(1, 2)
        if tmp == 1:
            hostChoice = door_1
        else:
            hostChoice = door_2

    if ifChange == 'Y' or ifChange == 'y':

        if choice == 1 or choice == 2:
            res = door_3

        else:
            tmp = random.randint(1, 2)
            if tmp == 1:
                res = door_1
            else:
                res = door_2

    else:
        pass

    if res == door_3:
        count += 1

print('The final frequency of getting a car is ' + str(count/n))
