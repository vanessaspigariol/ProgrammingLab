class Model():
    def fit(self,data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self,data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self,data):
        prev_value=None
        valore=[]
        scarti=[]
        n=0
        for item in data:
            if item!=None:
                try:
                    valore.append(float(item))
                    n=n+1
                except Exception:
                    raise Exception('Errore: valore non numerico')
                    valore.append(0)
                    n=n+1
            if item==None:
                valore.append(0)
                n=n+1
            if n>1:
                scarto=(valore[n-1]-valore[n-2])
                scarti.append(scarto)
        if len(scarti)!=0:
            prev_value=sum(scarti)
            prev_value=prev_value/(n-1)
        prediction=valore[n-1]+prev_value
        return prediction


class FitIncrementModel(IncrementModel):
    def predict(self, data):
        for item in data:
            if item < 0:
                raise Exception('Numero minore di zero')
        prediction = 0
        prev_value = data[0]
        for i in range(len(data)):
            prediction = (data[i] - prev_value) + prediction
            prev_value = data[i]
        
        prediction = prediction / (len(data) - 1)
        
    
    def fit(self, data1, data2):
        p1 = predict(data1)
        p2 = predict(data2)
        prediction = (p1 + p2)/2
        prediction = prediction + data2[-1]
        return prediction
    