favProgLang = ['PHP','Java','VB.NET','C#','Python','Javascript','Ruby']

for f in favProgLang:
    if f is "VB.NET":
        continue
    print(f)    


invalidNumbers = [2,34,13,9,12]

for x in range(0,max(invalidNumbers)):
    if x in invalidNumbers:
        print('skipped')
        continue
    print(x)