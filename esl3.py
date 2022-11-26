def sum_csv(my_file):
    values = []
    fun = open(my_file, 'r')
    for line in fun:
        elements = line.split(',')
        if elements[0] != 'Date':
            #date = elements[0]
            value = elements[1]
            values.append(float(value)) #trasforma le stringhe in valori numerici
    if len(values) == 0:
        return None
    else:
        somma = sum(values)

    return somma


print(sum_csv("shampoo_sales.csv"))