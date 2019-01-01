"""Exercise 1: Check if ‘is’ present in str1"""
str1 = "this is a sample DaTaa"
#method 1
if str1.find('is',0,-1) is not -1:
    print("\'is\' is present")
else:
    print("\'is\' is not present")
#method 2
    # if str1.__contains__('is') :
    #     print("\'is\' is present")
    # else:
    #     print("\'is\' is not present")
#method 3

    # if 'is' in str1:
    #     print("\'is\' is present")
    # else:
    #     print("\'is\' is not present")

#print str1 in uppercase
print(str1.upper())


