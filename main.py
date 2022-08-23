# Bincom Online test

monday = ['YELLOW', 'GREEN', 'BROWN', 'BLUE',
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

# this is to get total color in the week
week = monday + tuesday + wednesday + friday + thursday

week_iteration = []
for i in week:
    if i not in week_iteration:
        week_iteration.append(i)
# print(week_iteration)

# for no 1 question
list_num_of_colors = week.count('GREEN'), week.count('YELLOW'), week.count('ARSH'), week.count('BROWN'), week.count(
    'BLUE'), \
                     week.count('PINK'), week.count('ORANGE'), week.count('CREAM'), week.count('RED'), week.count(
    'WHITE'), \
                     week.count('BLEW'), week.count('BLACK')


# getting the average of the colors
total_week = len(week)
length = []
for r in week:
    string_size = len(r)
    length.append(string_size)
    total_size = sum(length)
avg = total_size / total_week
#print(avg)
