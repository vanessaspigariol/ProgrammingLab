class CSVFile():
    def __init__(self, name):
        self.name=name
        
    def get_data(self):
        try:
            file=open(self.name, 'r')
        except Exception:
            print('Errore')
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