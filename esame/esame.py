class ExamException(Exception):
    pass

class CSVFile():
    def __init__(self,name):
        self.name=name #inizializzo nome file
        self.can_read=True #provo ad aprire file e leggerlo
        try:
            my_file=open(self.name,'r')
            my_file.readline()
        except ExamException as e:
            self.can_read=False
            print('errore, file non leggibile: {}'.format(e))
    def get_data(self):
        if not salf.can_read:
            print('errore, file non aperto o leggibile')
            return None #fine
        else:
            data=[] #lista vuota per salvarci i dati
            my_file=open(self.name,'r') #riapro il file per non saltare la prima riga
            for line in my_file:
                elements=line.split(',')
                elements[-1]=elements[-1].strip() #pulisco il carattere da spazi bianchi
                if elements[0]!='date':
                    data.append(elements) #aggiungo elementi alla lista escludendo l'intestazione
            my_file.close()
            return data #ritorno i dati salvati dopo aver processato tutto

class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        string_data=super().get_data() #chiamo metodo get_data di CSVFile
        if string_data==[]:
            raise ExamException('errore, lista csv file vuota')
        numerical_data=[] #creo una lista che possa contenere i valori
        for item in string_data:
            if item is not list:
                raise ExamException('errore, elemento lista non è una lista: manca uno dei due valori')
            if len(item)!=2:
                raise ExamException('errore, lista non contiene due valori')
            date=item[0].split('-') #splitto il primo elemento dela lista per separare anno e mese
            try:
                year=int(date[0])
                month=int(date[1])
            except ValueError:
                raise ExamException('errore, anno o meso sono valori non interi')
            try:
                passenger=int(item[1])
            except ValueError:
                raise ExamException('errore, numero passeggeri non intero')
            if int(year)<1949 or int(year)>1960 or int(month)<=0 or int(month)>12:
                raise ExamException('errore, data non valida')
            else:
                numerical_data.append(item) #aggiungo la lista contenente data e numero passeggeri dopo aver controllato la validità del dato
            return numerical_data
            
