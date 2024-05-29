# What is the purpose continue statement in python?

# => Continue statement skips the given number and continues the loop

n = int(input("Enter number"))

for i in range(1,n+1):
    if i == 6:
        continue                 # continue statement

    print(i)
