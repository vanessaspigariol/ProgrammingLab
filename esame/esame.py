class ExamException(Exception):
    pass


class CSVFile():
    def __init__(self, name):
        self.name = name  #inizializzo nome file
        self.can_read = True  #provo ad aprire file e leggerlo
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except ExamException as e:
            self.can_read = False
            print('errore, file non leggibile: {}'.format(e))

    def get_data(self):
        if not self.can_read:
            print('errore, file non aperto o leggibile')
            return None  #eventuale fine
        else:
            data = []  #lista vuota per salvarci i dati
            my_file = open(self.name,
                           'r')  #riapro il file per non saltare la prima riga
            for line in my_file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip(
                )  #pulisco il carattere da spazi bianchi
                if elements[0] != 'date':
                    data.append(
                        elements
                    )  #aggiungo elementi alla lista escludendo l'intestazione
            my_file.close()
            return data  #ritorno i dati salvati dopo aver processato tutto


class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        #chiamo metodo get_data di CSVFile e alzo eccezioni nel caso il file non esista o non sia leggibile
        string_data = super().get_data()
        if string_data == []:
            raise ExamException('errore, lista csv file vuota')
        if string_data is None:
            raise ExamException(
                'errore, il metodo get_data di csvfile è nullo')

        #creo una lista che possa contenere i valori validi
        numerical_data = []
        for item in string_data:
            if item == []:
                continue
            if item is not list:
                continue
            if len(item) < 2:
                continue  #la lista deve avere almeno due valori (data e numero passeggeri)

            #controllo che i valori siano interi
            date = item[0].split('-')  #separo anno e mese
            try:
                anno = int(date[0])  #anno è un intero
                mese = int(date[1])  #mese è un intero
            except Exception:
                pass
            try:
                passeggero = int(item[1])  #passeggero è un intero
            except Exception:
                pass

            #controllo che i dati siano ordinatiper aggungerli a numerical_data
            if item == string_data[0]:
                prev_anno = anno
                prev_mese = mese
            else:
                if anno < prev_anno:
                    raise ExamException('errore, anni non ordinati')
                if mese <= prev_mese and anno == prev_anno:
                    raise ExamException(
                        'errore, mesi non ordinati o duplicati')
                prev_anno = anno
                prev_mese = mese
            if anno > 0 and mese > 0 and mese <= 12 and passeggero >= 0:
                numerical_data.append(item)
        return numerical_data


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()


def detect_similar_monthly_variations(time_series, years):
    #controllo liste in input
    if time_series == []:
        raise ExamException('errore, lista dati vuota')

    if years == []:
        raise ExamException('errore, lista anni vuota')
    if len(years) != 2:
        raise ExamException('errore, lista anni ha una lunghezza non valida')

    #distinguo e controllo i due anni della lista years
    try:
        anno1 = int(years[0])
    except Exception:
        raise ExamException('errore, primo anno non intero')
    try:
        anno2 = int(years[1])
    except Exception:
        raise ExamException('errore, secondo anno non intero')
    if anno1 < 0 or anno2 < 0:
        raise ExamException('errore, anni non esistenti')
    if anno1 - anno2 != 1 and anno1 - anno2 != -1:
        raise ExamException('errore, anni non consecutivi')

    #creo una lista per i valori ciascun anno
    prima_lista = []
    existence1 = False  #sarà utile per determinare se il primo anno è presente tra i dati
    for element in time_series:
        #trovo tutti i dati corrispondendi ad anno1
        tempo = element[0].split('-')  #divido anno(tempo[0]) e mese(tempo[1])
        if tempo[0] == anno1:
            existence1 = True
            mese = (tempo[1]) - 1
            try:
                #inserisco il numero dei passeggeri(element[1]) nella posizione corrispondente al mese in cui sono stati rilevati
                prima_lista.insert(mese, int(element[1]))
            except:
                raise ExamException(
                    'errore, non è stato possibile aggiungere un valore alla lista del primo anno'
                )
    if existence1 is False:
        raise ExamException('errore, primo anno di years non valido')

    seconda_lista = []  #lista elementi secondo anno
    existence2 = False  #sarà utile per determinare se il primo anno è presente tra i dati
    for element in time_series:
        #trovo tutti i dati corrispondendi ad anno2
        tempo = element[0].split('-')  #divido anno(tempo[0]) e mese(tempo[1])
        if tempo[0] == anno2:
            existence2 = True
            mese = (tempo[1]) - 1
            try:
                #inserisco il numero dei passeggeri (element[1]) nella posizione corrispondente al mese in cui sono stati rilevati i dati
                seconda_lista.insert(mese, int(element[1]))
            except:
                raise ExamException(
                    'errore, non è stato possibile aggiungere un valore alla lista del secondo anno'
                )
    if existence2 is False:
        raise ExamException('errore, secondo anno di years non valido')

    #controllo le due liste ottenute e controllo che abbiano 12 elementi, anche nulli
    if prima_lista == []:
        raise ExamException('errore, lista anno1 vuota')
    if prima_lista is not list:
        raise ExamException('errore, lista anno1 non è una lista')
    if len(prima_lista) != 12:
        for i in enumerate(11):
            if prima_lista[i] is not None:
                pass
            else:
                prima_lista[i] = None
    if seconda_lista == []:
        raise ExamException('errore, lista anno2 vuota')
    if seconda_lista is not list:
        raise ExamException('errore, lista anno2 non è una lista')
    if len(seconda_lista) != 12:
        for i in enumerate(11):
            if seconda_lista[i] is not None:
                pass
            else:
                seconda_lista[i] = None

    #creo liste per salvare le variazioni tra mesi
    variazione1 = []
    for i in prima_lista:
        if i == prima_lista[0]:
            prev_value = i  #gennaio non ha mesi precedenti, quindi non calcolo la differenza
        elif i == None:
            prev_value = i
            variazione1.append(None)
        elif prev_value == None:
            variazione1.append(None)
            prev_value = i
        else:
            differenza = int(i - prev_value)
            prev_value = i
            variazione1.append(int(differenza))
    variazione2 = []  #lista con variazioni tra valori seconda lista
    for i in seconda_lista:
        if i == seconda_lista[0]:
            prev_value = i  #gennaio non ha mesi precedenti, quindi non calcolo la differenza
        elif i == None:
            prev_value = i
            variazione2.append(None)
        elif prev_value == None:
            variazione2.append(None)
            prev_value = i
        else:
            differenza = int(i - prev_value)
            prev_value = i
            variazione2.append(int(differenza))
            
    if variazione1 == []:
        raise ExamException('errore, variazione1 non ha valori numerici')
    if len(variazione1) != 11:
        raise ExamException('errore, lista variazione1 non ha 11 elementi')
    if variazione1 == None:
        raise ExamException('errore, variazione1 non ha valori')
        
    if variazione2 == []:
        raise ExamException('errore, variazione2 non ha valori numerici')
    if len(variazione2) != 11:
        raise ExamException('errore, lista variazione2 non ha 11 elementi')
    if variazione2 == None:
        raise ExamException('errore, variazione2 non ha valori')

    #lista finale confronterà parallelamente le variazioni delle due liste ritornando vero o falso
    lista_finale = []
    for i in enumerate(10):
        if variazione1[i] is None or variazione2[i] is None:
            lista_finale.append(False)
        else:
            differenza = variazione1[i] - variazione2[
                i]  #differenze tra le stesse coppie di mesi in anni consecutivi
        if differenza >= -2 and differenza <= 2:
            lista_finale.append(True)  #simili
        else:
            lista_finale.append(False)  #non simili
    return lista_finale