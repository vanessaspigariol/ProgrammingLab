class CSVFile():
    def __init__(self, name):
        self.name=name
        
    def get_data(self):
        file=open(self.name, 'r')
        lista=[]
        for line in file:
            if line == "Date,Sales\n":
                elements=None
            else:
                line=line.strip('\n')
                elements=line.split(',')
                lista.append(elements)
        file.close()
        return lista

#csv_file = CSVFile("shampoo_sales.csv")            # in questo modo istanzi l'oggetto csv_file, passandogli come argomento il nome del file
#data = csv_file.get_data()                                    # chiami il metodo get_data dell'oggetto e salvi l'output nella variabile data
#print(data)                                                          # infine puoi stampare il contenuto della variabile per controllare cosa fa il metodo get_data