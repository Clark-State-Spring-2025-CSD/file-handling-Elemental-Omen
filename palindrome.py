#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

f=open("words.txt")
words = f.read().splitlines()
f.close()

palindrome_count = 0

for word in words:
    if word[0]== word[-1]:
        palindrome_count += 1
    
print(f"There are {palindrome_count} palindromes in the file.")
        

