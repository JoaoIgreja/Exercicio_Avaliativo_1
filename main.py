from database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

motoristaDAO = MotoristaDAO(database= Database(database="S202-L2", collection="Motoristas"))

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()