"""
    From given list

    gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00,
    "Television", 1000, "Laptop Case", "Camera Lens"]

    a)create separate lists of strings and numbers.
    
    b)Sort the strings list in ascending order
    
    c)Sort the strings list in descending order
    
    d)Sort the number list from lowest to highest
    
    e)Sort the number list from highest to lowest
"""
gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00,
"Television", 1000, "Laptop Case", "Camera Lens"]
string_list = [] 
number_list = []
for g in gadgets:
    if isinstance(g, str):
        string_list.append(g)
    elif isinstance(g,int) or isinstance(g,float):
        number_list.append(g)
#a) seperate list for strings and numbers
print(string_list,number_list)

#b) sort the strings in ascending order
string_list.sort()
print(string_list)

#c) sort the strings in descending order
string_list.sort(reverse=True)
print(string_list)

#d)sort the numbers in ascending order
number_list.sort()
print(number_list)

#e)sort the numbers in ascending order
number_list.sort(reverse=True)
print(number_list)

