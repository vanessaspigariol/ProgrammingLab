class CSVfile():
    
    def __init__(self, name):
        self.name=name
    
    def get_data(self):
        for lines in (self):
            list=self.split()
            print(list)

csvfile=CSVfile(shampoo_sales.csv)
csvfile=open('shampoo_sales.csv', 'r')
print(csvfile.name)
data=csvfile.get_data()
print(data)