from collections import Counter

names = ["Joe","Daniel","Seyi","Kelvin","Muhammed","Hakimi","Segun","Ashly","Seyi"]
list_of_names = Counter(names)
for name, count in list_of_names.items():
    print(f"{name} {count}")