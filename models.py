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
        for item in data:
        # Logica per la predizione
        ...
        prediction = ...
        return prediction