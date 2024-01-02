with open("/tmp/cars.txt", "w") as file:
    file.writelines(f"There are {num} cars\n" for num in range(50))

with open("/tmp/cars.txt", "r") as file:
    print(file.read())
