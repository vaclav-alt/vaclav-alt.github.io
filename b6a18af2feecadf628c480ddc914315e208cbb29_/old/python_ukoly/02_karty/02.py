from distutils import util

raw_data = [
"Karel Vopěnka;1654731544681137,10/25,487;iamthecapitannow;t",
"Ekaterina Pogonisheva;3685147993221530,12/22,369;<3pogoftw;f",
"Jana Poláková;5168467833451129,02/19,498;lol;f"
]

victim_data = []

for datastr in raw_data:
    entry = datastr.split(";")
    card_info = entry[1].split(",")
    name = entry[0].split(" ")
    victim = {
        "name" : name[0],
        "surname" : name[1],
        "card_no" : int(card_info[0]),
        "card_exp" : card_info[1],
        "card_that_third_thing" : int(card_info[2]),
        "pwd" : entry[2],
        "2factor" : util.strtobool(entry[3])
    }
    victim_data.append(victim)

for victim in victim_data:
    print(victim)
