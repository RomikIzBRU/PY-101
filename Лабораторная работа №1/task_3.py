list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2

first_team = list_players[:middle_index]#все что левее центрального индекса
second_team = list_players[middle_index:]#все что правее центрально индекса

print(first_team)
print(second_team)
