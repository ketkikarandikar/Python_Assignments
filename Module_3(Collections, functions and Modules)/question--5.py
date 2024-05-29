# How will you compare two lists?

# We can compare the two lists  by using sorting method through which the list is sorted

j = [10, 15, 25, 35, 20, 30]

k = [30, 25, 35, 20, 10, 15]

l = [16, 68, 96, 52, 23, 46]


j_sort = sorted(j)
k_sort = sorted(k)
l_sort = sorted(l)


if j_sort==k_sort:
    print("The list j and k are same.")

else:
    print("The list j and k are different.")

if j_sort==l_sort:
    print("The list j and l are same.")
else:
    print("The list j and l are different.")

if k_sort==l_sort:
    print("The list k and l are same.")
else:
    print("The list k and l are different.")
