class Model():
    def fit(self, data):
    # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
    # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        prev_value = None
        somma_differenze= 0
        passaggi=0
        for item in data:
            if (prev_value==None):
                prev_value=item
            else:
                differenza= item - float(prev_value)
                prev_value=item
                somma_differenze= somma_differenze+differenza
                passaggi=passaggi+1
        
        try:
            media=somma_differenze/passaggi
            
        except ZeroDivisionError as e:
            print('Non ho potuto calcolare la media perchè passaggi valeva: {}'.format(e))

        prediction = item+media
        return prediction