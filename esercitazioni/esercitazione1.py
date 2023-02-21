class ExamException(Exception):
    pass
    
class MovingAverage():
    def __init__(self, l):
        self.l=l
        if type(self.l)==str:
            raise ExamException('errore, lunghezza stringa')
        if type(self.l)==float:
            raise ExamException('errore, lunghezza non intera')
        if type(self.l)!=int:
            raise ExamException('errore, lunghezza non intera')
        if self.l<=0:
            raise ExamException('errore, lugnhezza nulla')
        
    def compute(self,n):
        if n==[]:
            raise ExamException('errore, lista vuota')
        if type(n) is not list:
            raise ExamException('errore, non è una lista')
        if len(n)==0:
            raise ExamException('errore, lista nulla')
        if self.l>len(n):
            raise ExamException('errore, finestra troppo grande')
            
        numeri=[]
        for item in n:
            if type(item) is str or type(item) is bool or type(item) is None:
                raise ExamException('errore, valore in lista non buono')
            else:
                numeri.append(float(item))
                
        if numeri==[]:
            raise ExamException('errore, non sono presenti valori numerici')
        else:
            average_list = []
            for i in range(len(numeri) - self.l + 1):
                tot = 0
                for j in range(i, self.l + i):
                    tot = tot + numeri[j]
                media = tot/self.l
                average_list.append(media)
            return average_list
            

#moving_average = MovingAverage(2)
#result = moving_average.compute([2,4,8,16])
#print(result) 