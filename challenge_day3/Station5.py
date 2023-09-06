def solution_station_5(name):
    groups = {
        1: ["Charlie", "Andrey", "Akanksha", "Hugo", "Al-fatihi"],
        2: ["Maria", "Celia", "Gur", "Carine", "Sabrina"],
        3: ["Elisa", "Dmitry", "Sari", "Martyna", "Jesper", "Kavin"],
        4: ["Kelt", "Sebastian", "Quanpu", "Ruben", "Sofia"],
        5: ["Kian", "Gonzalo", "Sahir", "Teun", "Tom"],
        6: ["Angeline", "Matas", "Raven", "Caleb", "Paulina", "Angelica"],
        7: ["Mate", "Martyna", "Vincent", "Eryk", "Emma"],
        8: ["Sanne", "Beatris", "Sally", "Alyssa", "Caio", "Hielke"],
        9: ['Atlas', 'Yash', 'Eliana', 'Felix', 'Diana'],
        10: ['Charlie', 'Andrey', 'Akanksha', 'Max', 'Hugo', 'Al-fatihi'],
        11: ['Ioanna', 'Vanessa', 'Ella', 'Alicja', 'Cristian'],
        12: ['Karolina', 'Rachna', 'Luca', 'Alexia', 'Yuyue', 'Jelle']
    }

    for group, names_in_group in groups.items():
        if name in names_in_group:
            return group
        

name_to_find = "Sofia"
result = solution_station_5(name_to_find)
print(result)