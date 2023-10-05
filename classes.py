class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento
            
class Corrida:
    def __init__(self, notaCorrida: int, distancia: float, valor: float, passageiro: Passageiro):
        self.notaCorrida = notaCorrida
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro
        
class Motorista:
    def __init__(self, notaMotorista: int, corridas: tuple):
        self.notaMotorista = notaMotorista
        self.corridas = corridas