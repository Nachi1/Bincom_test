# Bincom Online test
import statistics
import random

monday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE',
          'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE',
          'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
tuesday = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE',
           'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']
wednesday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE',
             'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']
thursday = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE',
            'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
friday = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED',
          'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

mon = []
tue = []
wed = []
thur = []
fri = []

for F in monday:
    if F not in mon:
        mon.append(F)
for k in tuesday:
    if k not in tue:
        tue.append(k)
for j in wednesday:
    if j not in wed:
        wed.append(j)
for h in thursday:
    if h not in thur:
        thur.append(h)
for g in friday:
    if g not in fri:
        fri.append(g)

# this is to get every color
week = monday + tuesday + wednesday + friday + thursday
week_iteration = []
for i in week:
    if i not in week_iteration:
        week_iteration.append(i)
# print(week_iteration)

# for no 1 question
# getting the average of the colors
list_num_of_colors = week.count('GREEN'), week.count('YELLOW'), week.count('ARSH'), week.count('BROWN'), week.count(
    'BLUE'), \
                     week.count('PINK'), week.count('ORANGE'), week.count('CREAM'), week.count('RED'), week.count(
    'WHITE'), \
                     week.count('BLEW'), week.count('BLACK')


# list_num_of_colors = (10, 5, 1, 6, 30, 5, 9, 2, 9, 16, 1, 1)
def Avg(lst):
    return sum(lst) / len(lst)


lst = [10, 5, 1, 6, 30, 5, 9, 2, 9, 16, 1, 1]
average = Avg(lst)
print(average)

# for no 2 task
green = week.count('BLUE')  # 30 occurrences

# for number 3 task
median_of_list = statistics.median(week)
print(median_of_list)

# for no 4 task
print("Variance of sample set is % s"
      % (statistics.variance(list_num_of_colors)))

# for number 5 task
# probability of getting red color
'''
for p in week:
    if p == 'RED':
        red = [p]
print(red)
'''

# for task number 8
# generating 4 random numbers of binary
temp = format(random.randrange(30), "b")
print(temp)

# for task number 7
count = 0
while count < 3:
    num = int(input('enter a number\n>> '))
    num_list = (2, 3, 6, 1, 21, 8, 55, 3, 7)
    count += 1
    if num in num_list:
        print('you are correct')
        break
    else:
        print('incorrect')
        if count == 1:
            print('try again')
        elif count == 2:
            print('try again')
        elif count == 3:
            print('try again')
        else:
            continue
else:
    print('failed')


# for task number 9
# Program to display the Fibonacci sequence up to n-th term
def fibonacci_sequence(n):
    if n <= 0:
        return 0

    fibo = [0] * (n + 1)
    fibo[1] = 1

    # Initialize result
    sm = fibo[0] + fibo[1]

    # Add remaining terms
    for ai in range(2, n + 1):
        fibo[ai] = fibo[ai - 1] + fibo[ai - 2]
        sm = sm + fibo[ai]

    return sm


print('the sum of the fibonacci numbers is', fibonacci_sequence(50))
