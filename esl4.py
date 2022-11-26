class CSVfile():
    
    def __init__(self, name):
        self.name=name
    csvfile=CSVfile(shampoo_sales.csv)
    csvfile=open('shampoo_sales.csv', 'r')
    print(csvfile.name)
    
    def get_data(self):
        elements=[]
        my_file=open(self.name, 'r')
        for line in my_file:
            if line != 'Date, Sales\n':
                elements.append(line)
        my_file.close()

    csv_file = CSVFile("shampoo_sales.csv") #istanzi l'oggetto csv_file, passandogli come argomento il nome del file
    data = csv_file.get_data() # chiami il metodo get_data dell'oggetto e salvi l'output nella variabile data
    print(data) # infine puoi stampare il contenuto della variabile per controllare cosa fa il metodo get_data