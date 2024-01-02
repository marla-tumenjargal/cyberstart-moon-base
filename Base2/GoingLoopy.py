numbers = []
count = 0
initial = 100

while count < 100:
    numbers.append(initial)
    initial = initial + 2
    count = count + 1

for num in numbers:
    print(num)
