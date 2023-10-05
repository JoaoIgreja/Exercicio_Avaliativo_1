from classes import Passageiro, Corrida, Motorista


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas = []
        while True:
            nome = input("Enter the passenger's name: ")
            documento = input("Enter the passenger's document: ")
            passageiro = Passageiro(nome, documento)

            notaCorrida = int(input("Enter the ride rating: "))
            distancia = float(input("Enter the ride distance: "))
            valor = float(input("Enter the ride value: "))
            corrida = Corrida(notaCorrida, distancia, valor, passageiro)
            corridas.append(corrida)

            aux = input("Do you want to add another ride for this driver? (y/n): ")
            if aux.lower() == 'n':
                break

        notaMotorista = int(input("Enter the driver's rating: "))
        motorista = Motorista(notaMotorista, corridas)
        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)

        print(f'Driver rating: {motorista.notaMotorista}')
        for corrida in motorista.corridas:
            print(f'Ride rating: {corrida.notaCorrida}')
            print(f'Ride distance: {corrida.distancia}')
            print(f'Ride value: {corrida.valor}')
            print(f'Passenger name: {corrida.passageiro.nome}')
            print(f'Passenger document: {corrida.passageiro.documento}')

    def update_motorista(self):
        id = input("Enter the id: ")
        corridas = []
        while True:
            nome = input("Enter the passenger's name: ")
            documento = input("Enter the passenger's document: ")
            passageiro = Passageiro(nome, documento)

            notaCorrida = int(input("Enter the ride rating: "))
            distancia = float(input("Enter the ride distance: "))
            valor = float(input("Enter the ride value: "))
            corrida = Corrida(notaCorrida, distancia, valor, passageiro)
            corridas.append(corrida)

            aux = input("Do you want to add another ride for this driver? (y/n): ")
            if aux.lower() == 'n':
                break

        notaMotorista = int(input("Enter the driver's rating: "))
        motorista = Motorista(notaMotorista, corridas)
        self.motorista_model.update_motorista(id, motorista)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete