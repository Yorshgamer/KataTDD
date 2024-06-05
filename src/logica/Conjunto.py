class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        if len(self.__conjunto) > 0:
            return sum(self.__conjunto) / len(self.__conjunto)
        else:
            return None

    def promedio_ponderado(self, pesos):
        if len(self.__conjunto) == len(pesos):
            suma_ponderada = sum(valor * peso for valor, peso in zip(self.__conjunto, pesos))
            suma_pesos = sum(pesos)
            return suma_ponderada / suma_pesos if suma_pesos != 0 else None
        else:
            return None
