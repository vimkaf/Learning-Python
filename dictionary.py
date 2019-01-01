#A computer dictionary
dictionary = {'HDD':'Hard Disk Drive','SSD':'Solid Storage Device','CPU':'Central Processing Unit','VDU':'Visual Display Unit'}

#lets try the norm way
print(dictionary['HDD'])

for word,meaning in dictionary.items():
    print(word +  "=>" + meaning)