import json

player_1 = {
    'PlauerName': 'Donald Duck',
    'Score': 345,
    'Awards': ['OR', 'NV', 'NY'],
}

player_2 = {
    'PlauerName': 'Mikki Mouse',
    'Score': 355,
    'Awards': ['TX', 'MS', 'BR'],
}

all_players = []
all_players.append(player_1)
all_players.append(player_2)

# ***** SERIALIZE by JSON *****

print(json.dumps(all_players))

# ***** SAVE by JSON *****

try:
    filename = "user_settings.json"
    filewriter = open(filename, mode='w', encoding='utf-8')
except Exception:
    print("Не удалось открыть поток для записи данных в файл.")
else:
    try:
        json.dump(all_players, filewriter)
    except Exception:
        print("Ошибка при сериализации обьекта в JSON.")
    else:
        filewriter.close()
        print("Данные успешно сериализованны в JSON и записаны в файл - " + filename)

# ***** LOAD by JSON *****

try:
    filename = "user_settings.json"
    filereader = open(filename, mode="r", encoding="utf-8")
except Exception:
    print("Не удалось открыть поток для чтения данных из файла.")
else:
    try:
        players = json.load(filereader)
    except Exception:
        print("Ошибка при десериализации обьекта из файла.")
    else:
        filereader.close()
        print("Данные успешно десериализованны из файла, поток для чтения закрыт.")

        for player in players:
            print("\n***** Player *****")
            for key in player:
                print(key, ': ', player[key])
