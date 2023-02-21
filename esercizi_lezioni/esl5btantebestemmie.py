class CSVFile():
    def __init__(self, name):
        self.name=name
    def get_data(self):
        try:
            my_file=open(self.name, 'r')
        except Exception as e:
            print('Errore di questo tipo: {}'.format(e))
        list=[]
        for line in my_file:
            new_line=line.split(',')
            if new_line[0]!='Date':
                elements=[]
                elements.append(new_line[0].strip())
                elements.append(new_line[1].strip())
                list.append(elements)
        if list==None:
            return None
        else:
            return list
        my_file.close()

class NumericalCSVFile(CSVFile):
    def get_data(self):
        new_list=super().get_data()
        my_list=[]
        for string_row in new_list:
            numerical_row=[]
            for i,element in enumerate(string_row):
                if i==0:
                    numerical_row.append(element)
                else:
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
    
            if len(numerical_row) == len(string_row):
                my_list.append(numerical_row)
        
        return my_list



#file=NumericalCSVFile("shampoo_sales.csv")
#lista=file.get_data_2()
#print(lista)