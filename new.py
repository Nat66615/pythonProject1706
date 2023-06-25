class TransportMech:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def accelerate(self):
        raise NotImplementedError('ВЫ НЕ ГОТОВЫ!')


    def decelerare(self):
        pass

    def stop(self):
        pass

class Car(TransportMech):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def accelerate(self):
        print(f'{self.model} ... {self.fuel_type} ...')