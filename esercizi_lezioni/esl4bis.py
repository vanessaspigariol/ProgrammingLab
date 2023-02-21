class CSVFile():
    def __init__(self, name):
        self.name=name
    def get_data(self):
        my_file=open(self.name, 'r')
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

