from pymongo import MongoClient
from bson.objectid import ObjectId
from classes import Motorista, Corrida, Passageiro


class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista):
        try:
            corridas = self._parse_corridas(motorista.corridas)
            motorista_dict = {
                "notaMotorista": motorista.notaMotorista,
                "corridas": corridas,
            }
            res = self.db.collection.insert_one(motorista_dict)
            print(f"Motorista created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista_by_id(self, motorista_id):
        try:
            motorista_dict = self.db.collection.find_one({"_id": ObjectId(motorista_id)})
            if not motorista_dict:
                print(f"Motorista not found with id: {motorista_id}")
                return None

            notas = motorista_dict["notaMotorista"]
            corridas = self._parse_corridas_dict(motorista_dict["corridas"])
            motorista = Motorista(notas, corridas)
            print(f"Motorista found: {motorista_dict}")
            return motorista
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, motorista_id, motorista):
        try:
            corridas = self._parse_corridas(motorista.corridas)
            motorista_dict = {
                "notaMotorista": motorista.notaMotorista,
                "corridas": corridas,
            }
            res = self.db.collection.update_one(
                {"_id": ObjectId(motorista_id)}, {"$set": motorista_dict}
            )
            if res.modified_count == 0:
                print(f"Motorista not found with id: {motorista_id}")
            else:
                print(f"Motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, motorista_id):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(motorista_id)})
            if res.deleted_count == 0:
                print(f"Motorista not found with id: {motorista_id}")
            else:
                print(f"Motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None

    def _parse_corridas(self, corridas):
        return [
            {
                "notaCorrida": corrida.notaCorrida,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro": {
                    "nome": corrida.passageiro.nome,
                    "documento": corrida.passageiro.documento,
                },
            }
            for corrida in corridas
        ]

    def _parse_corridas_dict(self, corridas_dict):
        return [
            Corrida(
                corridas_dict["notaCorrida"],
                corridas_dict["distancia"],
            )
        ]