import random
from json_data import Json

json_file = "participants.json"


class Lottery:
    def register():
        email = input("Escribe tu email para participar: ")
        new_participant = {"email": email}

        try:
            data = Json.read(json_file)
            data.append(new_participant)
            Json.write(json_file, data)
        except:
            Json.write(json_file, [new_participant])

    def totalParticipants():
        try:
            data = Json.read(json_file)
            return len(data)
        except:
            return 0

    def executeLottery(total_winners):
        try:
            data = Json.read(json_file)
            winners = random.sample(data, total_winners)
            return winners
        except:
            return "No hay participantes"


# Lottery.register()

# total = Lottery.totalParticipants()
# print(total)

winners = Lottery.executeLottery(2)
print(winners)
