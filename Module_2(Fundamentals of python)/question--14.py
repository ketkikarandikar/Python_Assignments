# What are negative indexes and why are they used ?

# => The negative indexes are used to start the counting from the end of the string or word.

k = 'Python Programming'

#   P   0   -18
#   y   1   -17
#   t   2   -16
#   h   3   -15
#   o   4   -14
#   n   5   -13
#       6   -12
#   P   7   -11
#   r   8   -10
#   o   9   -9
#   g   10  -8
#   r   11  -7
#   a   12  -6
#   m   13  -5                                      
#   m   14  -4
#   i   15  -3
#   n   16  -2
#   g   17  -1

print(k[:-16:-1])
