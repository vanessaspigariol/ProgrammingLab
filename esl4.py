class CSVfile():
    
    def __init__(self, name):
        self.name=name
    
    def get_data(self):
        for lines in (self):
            list=self.split()
            print(list)

    csvfile=CSVfile
    csvfile=open('shampoo_sales.csv', 'r')
    print(CSVfile)
    print(CSVfile.name)
    print(get_data(CSVfile))