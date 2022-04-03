# ex 1
from typing import List, Any

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

# ex 2
x = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(x)

x = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
x.sort()
print(x)

# ex 3
x = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
x.sort(reverse=True)
print(x)

# ex 4
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
for num in my_list:
    if num % 2 != 0:
        print(num)
# ex 5
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
for i in my_list:
    if i % 3 == 0:
        print(i)



