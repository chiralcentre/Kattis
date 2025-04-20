from sys import stdin,stdout

def parse_date(release_date):
    return tuple(map(int,release_date.split("-")))

sort_mappings = {"nafn": 0, "id": 1,
                 "flokkur": 2, "dagsetning": 3}
# match every type and their subtype to a unique number in the order
type_mappings = {"Skrimsli-Venjulegt": 0, "Skrimsli-Ahrifa": 1, "Skrimsli-Bodunar": 2,
                 "Skrimsli-Samruna": 3, "Skrimsli-Samstillt": 4, "Skrimsli-Thaeo": 5,
                 "Skrimsli-Penduls": 6, "Skrimsli-Tengis": 7, "Galdur-Venjulegur": 8,
                 "Galdur-Bunadar": 9, "Galdur-Svida": 10, "Galdur-Samfelldur": 11,
                 "Galdur-Bodunar": 12, "Galdur-Hradur": 13, "Gildra-Venjuleg": 14,
                 "Gildra-Samfelld": 15, "Gildra-Mot": 16, "Annad": 17}

n = int(stdin.readline())
cards = []
for i in range(n):
    name,ID,t,release_date = stdin.readline().split(", ")
    cards.append((name, int(ID), type_mappings[t.replace(" ","")], parse_date(release_date)))
    
a,b,c,d = map(lambda x: sort_mappings[x], stdin.readline().split())
cards = sorted(cards, key = lambda x: (x[a],x[b],x[c],x[d]))
for card in cards:
    stdout.write(f"{card[0]}\n")
