class ExamException(Exception):
    pass

class Diff():
    def __init__(self,ratio=1):
        self.ratio=ratio
        if self.ratio is None:
            raise ExamException('ratio nullo')
        if type(self.ratio)==0:
            raise ExamException('ratio è 0')
        if type(self.ratio)==str:
            raise ExamException('ratio è stringa')
        try:
            self.ratio=float(self.ratio)
        except ValueError:
            raise ExamException('ratio non è numerico')
        if float(self.ratio)<=0:
            raise ExamException('ratio è negativo')
            
    def compute(self,lista):
        if lista==[]:
            raise ExamException('lista input vuota')
        if type(lista) is not list:
            raise ExamException('lista input non è lista')
        if len(lista)<=1:
            raise ExamException('lunghezza nulla lista input')
        lista_numerica=[]
        for element in lista:
            try:
                lista_numerica.append(float(element))
            except Exception:
                raise ExamException('valore non numerico')
        if lista_numerica==[]:
            raise ExamException('lista input non ha valori numerici')
        if type(lista_numerica) is not list:
            raise ExamException('lista numerica non è lista')
        if len(lista_numerica)==0:
            raise ExamException('lunghezza nulla lista numerica')       
        lista_finale=[]
        if len(lista_numerica)==1:
            return (float(lista_numerica[0]))/self.ratio
        for i in lista_numerica:
            if i==lista_numerica[0]:
                prev_value=i
            else:
                differenza=float(i-prev_value)
                differenza=differenza/self.ratio
                prev_value=i
                if differenza<0:
                    differenza=-differenza               
                lista_finale.append(float(differenza))
        if lista_finale==[]:
            raise ExamException('lista input non ha valori numerici')
        if len(lista_finale)==0:
            raise ExamException('lunghezza nulla lista finale')
        if lista_finale==None:
            raise ExamException('lista finale non ha valori')
        return lista_finale

#diff = Diff()
#result = diff.compute([2,4,8,16])
#print(result)