class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    
    def __init__(self,name):
        #inizializzo nome
        self.name=name 
            
    def get_data(self):
        
        ##CONTROLLO NOME
        if self.name is None:
            raise ExamException('Errore: nome file non inserito in input!')

        #provo ad aprire il file
        try:
            my_file=open(self.name, 'r')
            my_file.readline()
            #chiudo il file
            my_file.close()
        except Exception:
            raise ExamException('Errore: non è stato possibile aprire o leggere il file!')

        ##SALVATAGGIO DATI VALIDI
        lista=[]
        
        #riapro il file
        my_file=open(self.name, 'r')

        #leggo il file linea per linea
        for line in my_file:
            
            #pulizia carattere dall'ultimo elemento e split sulla virgola
            elements=line.strip("\n").split(",")
            
            #elements[0]=data anno-mese
            #elements[1]=passeggeri

            #se NON sto processando l'intestazione
            if elements[0].strip() == 'date':
                continue

            #variabile ausiliara per fare un check su anni e mesi
            tempo=elements[0].split('-') 
            
            #tempo[0]=anni
            #tempo[1]=mesi
            #elements[1]=passeggeri

            try:
                tempo[0] = int(tempo[0])
                tempo[1] = int(tempo[1])
                elements[1]=int(elements[1])
            except Exception:
                continue
            
                            
            #valori negativi
            if int(elements[1])<=0:
                continue

            lista.append(elements)
        
        #chiudo il file
        my_file.close()

        ##CONTROLLO ORDINE E DUPLICAZIONE
        numerical_data=[]
        
        for item in lista:
            if item == []:
                continue

            #la lista deve avere almeno due valori (data e numero passeggeri)
            if len(item) < 2:
                continue  

            #trasformo i dati in intero e assegno il valore a delle variabili più chiare, utili per il prossimo controllo
            date = item[0].split('-')  #separo anno e mese
            try:
                anno = int(date[0])  
                mese = int(date[1])  
                passeggero = int(item[1])
            except Exception:
                continue
                        

            #controllo che i dati siano ordinati per aggungerli a numerical_data
            #altrimenti alzo un'eccezione
            if item == lista[0]:
                prev_anno = anno
                prev_mese = mese
            else:
                if anno < prev_anno:
                    raise ExamException('Errore, anni non ordinati!')
                    continue
                if anno == prev_anno and mese <= prev_mese:
                    raise ExamException('Errore, mesi non ordinati o duplicati!')
                    continue
                prev_anno = anno
                prev_mese = mese
            if anno > 0 and mese > 0 and mese <= 12 and passeggero > 0:
                numerical_data.append(item)

        return numerical_data
        


#time_series_file = CSVTimeSeriesFile(name='data.csv')
#time_series = time_series_file.get_data()
#print(time_series)



def compute_avg_monthly_difference(time_series, first_year, last_year):

    ##CONTROLLI DATI INPUT
    if not time_series:
        raise ExamException('Errore, lista time_series vuota!')
    
    try:
        anno_inizio = int(first_year)
        anno_fine = int(last_year)
    except Exception:
        raise ExamException('Errore, non è stato possibile convertire gli anni in input in interi!')

    if anno_inizio > anno_fine:
        raise ExamException('Errore, anno inizio maggiore di anno fine!')
        
    #anno inizio nella lista
    found_inizio = False 
    for el in time_series:
        #variabile temporanea per capire se gli anni in input sono presenti nella lista
        tempAnno = int(el[0].split("-")[0])
        if  tempAnno == anno_inizio:
            #se trovo l'anno nella lista allora esco dal ciclo
            found_inizio = True 
            break

    if not found_inizio:
        raise ExamException('Errore, anno inizio non nella lista!')

    #anno fine nella lista
    found_fine = False
    for el in time_series:
        #variabile temporanea per capire se gli anni in input sono presenti nella lista 
        tempAnno = int(el[0].split("-")[0])
        if  tempAnno == anno_fine:
            #se trovo l'anno nella lista allora esco dal ciclo
            found_fine = True 
            break

    if not found_fine:
        raise ExamException('Errore! Anno fine non nella lista!')
        

    
    ##INIZIO PRIMA PARTE
    #creo una lista('listaanni') che conterrà un numero di liste pari al numero di anni presi in esame
    #ogni sotto-lista('annata') conterrà il numero di passeggeri nella posizione corrispondente al mese in cui sono stati rilevati
    listaanni=[]

    #inizializzo il primo anno da considerare
    prev_anno=anno_inizio

    #riempio con 12 zeri la lista che userò per il primo anno
    annata=[]
    for i in range(12):
        annata.append(0)

    #nel ciclo for sostituisco gli zeri con il numero di passeggeri nella posizione corrispondente al mese-1 in cui sono stati rilevati, se sono stati rilevati
    for element in time_series:
        tempo = element[0].split('-')
        try:
            anno = int(tempo[0])
            mese = int(tempo[1])-1
            passeggero = int(element[1])
        except Exception:
            continue
        
        #restiamo nell'arco di tempo determinato dagli anni presi in input
        #anno>anno_fine+1 per non escludere l'estremo
        if anno < anno_inizio or anno > anno_fine:
            continue
        
        #casi da considerare:
        
        #1:sono al primo anno o ad un anno già "salvato"(dopo il caso #2)
        if anno==prev_anno:
            annata[mese]=passeggero
            
        #2:anno diverso dal precedente
        #assumiamo di avere almeno una misurazione all’anno
        #quindi se anno!=prev_anno, anno==prev_anno+1
        #->inizializzo il nuovo anno a prev_anno
        #->salvo la lista appena creata e ne creo una nuova per il nuovo anno
            
        elif anno==prev_anno+1:
            prev_anno=anno
            listaanni.append(annata)
            annata=[]
            for i in range(12):
                annata.append(0)
            annata[mese]=passeggero
        
    listaanni.append(annata)
    #print(listaanni)

    ##FINE PRIMA PARTE:
    #lista 'listaanni' di 12 elementi per ogni anno, dove l’elemento all’indice i corrisponde al numero di passeggeri per il mese i+1 in quell’anno
    

    ##INIZIO SECONDA PARTE
    #ora posso iniziare a calcolare le medie, che saranno salvate nella lista 'medie'
    medie=[]
    
    #conto quante liste sono presenti nella lista 'totale'
    numero_anni=len(listaanni)
    divisore=numero_anni-1
    
    #ciclo for sui 12 mesi
    #counter salva l'indice delle sotto-liste
    for i in range(12):
        som=0 
        media=0
        counter=numero_anni-1        
        
        #eslcudo la prima sotto-lista perchè non ha valori precedenti da sottrarre
        while counter>0:
            
            #elemento in posizione 'i' della sotto-lista numero 'counter' o 'counter-1' presente nella lista 'totale'            
            try:
                primo=int(listaanni[counter][i])
                secondo=int(listaanni[counter-1][i])
            except Exception:
                #se non riesco a trasformare in intero dei dati, vado avanti e riduco di uno il divisore
                counter-=1
                divisore-=1
                continue #continua con la prossima iterazione del ciclo while

            #intervallo di due anni, per il mese con la misurazione mancante verrà tornato come valore finale 0
            if numero_anni==2 and (primo==0 or secondo==0):
                media=0
                break #interruzione ciclo while
                
            #intervallo di più di due anni, calcoliamo la differenza media tra le misurazioni di quel mese per gli altri anni, ignorando la misurazione mancante            
            elif numero_anni>2:
                if secondo==0:
                    counter-=1
                    continue #continua con la prossima iterazione del ciclo while
                elif primo==0:
                    #poichè 'secondo' diventerà 'primo',
                    #'divisore' cambia solo ora altrimenti si ridurrebbe due volte per uno stesso 0
                    divisore-=1
                    counter-=1
                    continue #continua con la prossima iterazione del ciclo while
            diff=primo-secondo
            som+=diff
            counter-=1

            #intervallo di più di due anni e per un mese abbiamo meno di due misurazioni, verrà tornato 0 come valore finale per quel mese
        if numero_anni>2 and divisore<2:
            media=0
        
        else:
            media=som/divisore
                
        medie.append(media)   
        
    ##FINE SECONDA PARTE
    return medie
    


#aa=compute_avg_monthly_difference(time_series, "1949", "1951")
#print(aa)