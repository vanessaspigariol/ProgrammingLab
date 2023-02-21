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
            return None #eventuale fine
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
        string_data=super().get_data() #chiamo metodo get_data di CSVFile, che ritorna una lista di liste
        if string_data==[]:
            raise ExamException('errore, lista csv file vuota')
        numerical_data=[] #creo una lista che possa contenere i valori validi
        for item in string_data:
            if item is not list:
                raise ExamException('errore, elemento lista non è una lista: manca uno dei due valori')
            if len(item)<=2:
                raise ExamException('errore, lista non contiene due valori') #la lista deve avere almeno due valori (data e numero passeggeri)
            date=item[0].split('-') #splitto il primo elemento dela lista(la data) per separare anno e mese
            try:
                date[0]=int(date[0])
                date[1]=int(date[1])
            except ValueError:
                pass
            try:
                item[1]=int(item[1]) #passeggeri
            except ValueError:
                pass
            if item==string_data[0]:
                prev_anno=int(date[0])
                prev_mese=int(date[1])
            else:
                if date[0]<prev_anno:
                    raise ExamException('errore, anni non ordinati')
                if date[1]<=prev_mese and date[0]==prev_anno:
                    raise ExamException('errore, mesi non ordinati o duplicati')
                prev_anno=int(date[0])
                prev_mese=int(date[1])
            if int(date[0])>0 and int(date[1])>0 and int(date[1])<=12 and int(item[1])>=0:
                numerical_data.append(item) #aggiungo la lista contenente data e numero passeggeri dopo aver controllato la validità del dato (anno e passeggeri maggiore di 0, mese tra 0 e 12)
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
    if anno1<0 or anno2<0:
        raise ExamException('errore, anni non esistenti')
    if anno1-anno2!=1 and anno1-anno2!=-1:
        raise ExamException('errore, anni non consecutivi')
    prima_lista=[] #lista elementi primo anno
    for element in time_series:
        #trovo tutti i dati corrispondendi ad anno1
        tempo=element[0].split('-') #divido anno e mese
        if tempo[0]==anno1:
            mese=(tempo[1])-1
            try:
                prima_lista.insert(mese, int(element[1])) #inserisco il numero dei passeggeri nella posizione corrispondente al mese in cui sono stati rilevati i dati
            except:
                raise ExamException('errore, non è stato possibile aggiungere un valore alla lista del primo anno')
    seconda_lista=[] #lista elementi secondo anno
    for element in time_series:
        #trovo tutti i dati corrispondendi ad anno2
        tempo=element[0].split('-') #divido anno e meso
        if tempo[0]==anno2:
            mese=(tempo[1])-1
            try:
                seconda_lista.insert(mese, int(element[1])) #inserisco il numero dei passeggeri nella posizione corrispondente al mese in cui sono stati rilevati i dati
            except:
                raise ExamException('errore, non è stato possibile aggiungere un valore alla lista del secondo anno')
    if prima_lista==[]:
        raise ExamException('errore, lista anno1 vuota')
    if prima_lista is not list:
        raise ExamException('errore, lista anno1 non è una lista')
    if len(prima_lista)!=12:
        for i in enumerate(12):
            if prima_lista[i] is None:
                prima_lista.insert(i-1, None) #la lista deve avere 12 valori in modo da poter confrontare tutti i mesi
    if seconda_lista==[]:
        raise ExamException('errore, lista anno2 vuota')
    if seconda_lista is not list:
        raise ExamException('errore, lista anno2 non è una lista')
    if len(seconda_lista)!=12:
        for i in enumerate(12):
            if seconda_lista[i] is None:
                seconda_lista.insert(i-1, None) #la lista deve avere 12 valori in modo da poter confrontare tutti i mesi
    variazione1=[] #lista con variazioni tra valori prima lista
    for i in prima_lista:
            if i==prima_lista[0]:
                prev_value=i #gennaio non ha mesi precedenti, quindi non calcolo la differenza
            elif i==None:
                differenza=None
                prev_value=i
                variazione1.append(int(differenza))
            else:
                differenza=int(i-prev_value)
                prev_value=i
                variazione1.append(int(differenza))
    variazione2=[] #lista con variazioni tra valori seconda lista
    for i in seconda_lista:
            if i==seconda_lista[0]:
                prev_value=i #gennaio non ha mesi precedenti, quindi non calcolo la differenza
            elif i==None:
                differenza=None
                prev_value=i
                variazione2.append(int(differenza))
            else:
                differenza=int(i-prev_value)
                prev_value=i
                variazione2.append(int(differenza))
    if variazione1==[]:
            raise ExamException('errore, variazione1 non ha valori numerici')
    if len(variazione1)!=11:
        raise ExamException('errore, lista variazione1 non ha 11 elementi')
    if variazione1==None:
        raise ExamException('errore, variazione1 non ha valori')
    if variazione2==[]:
            raise ExamException('errore, variazione2 non ha valori numerici')
    if len(variazione2)!=11:
        raise ExamException('errore, lista variazione2 non ha 11 elementi')
    if variazione2==None:
        raise ExamException('errore, variazione2 non ha valori')
    lista_finale=[]
    for i in enumerate(10):
        if variazione1[i] is None or variazione2[i] is None:
            lista_finale.append(False)
        else:
            differenza=variazione1[i]-variazione2[i] #differenze tra le stesse coppie di mesi in anni consecutivi
        if type(differenza)>=-2 and type(differenza)<=2:
            lista_finale.append(True)
        else:
            lista_finale.append(False)
    return lista_finale 