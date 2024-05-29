# Write a Python script to sort (ascending and descending) a dictionary by value.

# sample dictionary

s_dict = {("Red", "White"): '2', ("Black", "Lavender", "care free breeze"): '3', ("Brown", "Purple"): '1',}

sorted_dict_asc = dict(sorted(s_dict.items(), key=lambda item: item[1]))   # sort in ascending order

sorted_dict_desc = dict(sorted(s_dict.items(), key=lambda item: item[1], reverse=True))  # sort in descending order

print("Ascending order:", sorted_dict_asc)   
print("Descending order:", sorted_dict_desc)

