def sum_csv(my_file):
    values=[]
    fun=open('my_file', 'r')
    for lines in fun:
        elements=line.split(',')
        if elements[0] != 'Date':
            date=elements[0]
            value=elements[1]
            values.append(value)
    for value in values:
        somma=somma+value
    return somma