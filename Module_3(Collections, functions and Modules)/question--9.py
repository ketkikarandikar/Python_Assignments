# Write a Python function that takes two lists and returns true if they have at least one common member.

# defination to check if the two elements are same or not.

def check_list(l1, l2):
    set_1 = set(l1)

    for number in l2:
        if number in set_1:
            print("Some numbers are same : ")
            return True
    return False

l1 = [10,20,25,20,25,"Ketki","Red"]

l2 = [10,20,25,30,35,40,45,20,30,25]

print(check_list(l1,l2))