#function to calculate someones health rating blah blah blah

def health_calcualator(age,vegetables_ate,cigars_smoked):
    answer = (100 - age) + (vegetables_ate * 3.5) - (cigars_smoked * 2)
    print(answer)


joes_data = [15,20,5]

ib_data = {14,2,16} #so it also works for sets

health_calcualator(joes_data[0],joes_data[1],joes_data[2])

#unpacking the quicker way
health_calcualator(*ib_data)