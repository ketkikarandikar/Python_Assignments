# Write a Python program to count the occurrences of each word in a given sentence ?

# For printing the paragraph or sentence
print()

paragraph = input("* Enter a Paragraph  = *")   # to get input of paragraph or sentence from user


words = paragraph.split()   # To split the words and get the count of each word in the sentence or paragraph

d = {}     # Dictionary to store the words

for word in words:    # to count the occurences of words
    if word in d:
         d[word]  += 1
    else:
         d[word] = 1
         print("Word occurences:")
        
    for i, j in d.items():
        print(f"'{i}': {j}") 
