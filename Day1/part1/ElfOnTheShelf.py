from get_input import get_input

input_data = get_input("input.txt")

bucket1 = []
bucket2 = []
# grooming data while transforming strings into ints
for line in input_data:
    bucket1.append(int(line[0:5]))
    bucket2.append(int(line[-5:]))

bucket1.sort()
bucket2.sort()

total_distance = 0
# finding the distance between two numbers and totalling
for x, y in zip(bucket1,bucket2):
    total_distance += abs(y-x)
    # print(x,y)
    
print(total_distance)