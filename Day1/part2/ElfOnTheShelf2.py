from get_input import get_input

input_data = get_input("input.txt")

bucket1 = []
bucket2 = []
# grooming data while transforming strings into ints
for line in input_data:
    bucket1.append(int(line[0:5]))
    bucket2.append(int(line[-5:]))

total_score = 0

# Calculating a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
for x in bucket1:
    multiplier = 0
    for y in bucket2:
        if(x==y):
            multiplier += 1
    total_score += x*multiplier

    
print(total_score)