class CSVfile():
    def __init__(self, name):
        self.name=name

    def get_data(self):
        my_file=open(self.name, 'r')
        data=[]
        for line in my_file:
            if line == 'Date,Sales\n':
                elements=None
            else:
                elements=line.split(',')
                data.append(elements)
        
        my_file.close()
        print (data)

#my_file=CSVfile("shampoo_sales.csv") 
#my_file.get_data()
