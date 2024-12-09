from get_input import get_input

input_data = get_input("input.txt")

safe_reports = 0

for line in input_data:
    newLine = line.split()
    newestLine=[int(x) for x in newLine]
    print(newestLine)
    length =  len(newLine)-1

    while length > 0:
        storedNumber = ''
        forward = True
# setting the stage by determining direction and storing the first number
        for x in newestLine:
            if storedNumber == '':
                storedNumber = x
                if newestLine[0] > newestLine[1]:
                    forward = False
                else:
                    forward = True
                continue

# two case statements to check the continuation of ascending or descending number pattern
            if forward == True:
                if x <= storedNumber:
                    length = -1
                    print('bad report')
                    break
            if forward == False:
                if x >= storedNumber:
                    length = -1
                    print('bad report descending')
                    break

#  checking to see if the numbers differ by no more than 3.
            if abs(x-storedNumber) > 3:
                length = -1
                print('bad report, too high/low')
                break

            storedNumber = x
            length -= 1
            # print(length)
            if length == 0 :
                safe_reports += 1
                break
print(safe_reports)