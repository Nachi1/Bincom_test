# for no 2 task
import statistics
from main import week

color_mode = statistics.mode(week)  # 30 occurrences
# print(color_mode)

# or

# we iterate through the colors to get the number of occurrence
occurrence = []
for x in week:
    a = week.count(x)
    occurrence.append(a)
item = max(occurrence)  # == 30
print(occurrence)  # this gives a list with number of occurrences for each color, according to week list
indeX = occurrence.index(item)
print(indeX)  # this shows the index of the highest occurred in the occurrence list
if indeX == week.index(input('enter color from list').upper()):
    print(True)
