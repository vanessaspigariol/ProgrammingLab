def sum_csv(file_name):
    somma=[]
    for line in file_name:
        elements=line.split(',')
        if elements[0]!='Date':
            values=elements[1]
            somma.append(values)
    return somma

my_list=open('shampoo_sales.csv', 'r')
risultato=sum_csv(my_list)
print('Il risultato è: {}'.format(risultato))