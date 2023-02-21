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
        if not self.can_read:
            print('errore, file non aperto o leggibile')
            return None # eventuale fine
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
            
time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series=time_series_file.get_data()

def detect_similar_monthly_variations(time_series,years):
    if time_series==[]:
        raise ExamException('errore, lista dati vuota')
    if years is not list:
        raise ExamException('errore, non è presente una lista con gli anni da valutare')
    if years==[]:
        raise ExamException('errore, lista anni vuota')
    if len(years)!=2:
        raise ExamException('errore, lista anni ha una lunghezza non valida')
    try:
        anno1=int(years[0])
    except Exception:
        raise ExamException('errore, primo anno non intero')
    try:
        anno2=int(years[1])
    except Exception:
        raise ExamException('errore, secondo anno non intero')
    if int(anno1)<1949 or int(anno1)>1960 or int(anno2)<1949 or int(anno2)>1960:
        raise ExamException('errore, anni non validi')
    if int(anno1)-int(anno2)!=1 and int(anno1)-int(anno2)!=-1:
        raise ExamException('errore, anni non consecutivi')
        