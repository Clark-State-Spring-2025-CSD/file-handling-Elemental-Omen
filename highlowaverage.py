#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

f=open("numbers.txt")
numbers = f.read().splitlines()
f.close()

total = 0
average = 0
highest = 0 
lowest = 0

for number in numbers:
    total += int(number)
    if int(number) > highest:
        highest = int(number)
    if int(number) < lowest:
        lowest = int(number)
        
average = total / len(numbers)

print(f"There are {len(numbers)} numbers in the file.")
print(f"The total of all the numbers is {total}.")
print(f"The average of all the numbers is {average}.")
print(f"The highest number is {highest}.")
print(f"The lowest number is {lowest}.")
