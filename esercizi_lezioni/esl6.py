class CSVFile():
    def __init__(self, name):
        self.name=name
        if type(self.name)!=str:
            raise Exception('errore: nome file non è stringa')
            
    def get_data(self,start=None,end=None):
        try:
            my_file=open(self.name, 'r')
        except Exception as e:
            print('Errore di questo tipo: {}'.format(e))
        if type(start) or type(end) !=int:
            raise Exception('Errore: valori non numerici')
        if start>end:
            raise Exception('Errore: valori intervallo sballati')
        if end>len(my_file):
            raise Exception('Erore: intervallo troppo grande')
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
    def get_data(self, *args, **kwargs):
        csv_data = super.get_data(*args, **kwargs)
        my_list=[]
        for string_row in csv_data:
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


