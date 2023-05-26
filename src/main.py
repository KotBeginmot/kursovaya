import json
from typing import TextIO


def tranzact_execute(LINK):
    """Функция получает данные из файла и переводим на python"""
    with open(LINK, encoding='utf-8') as file:
        list_json = json.loads(file.read())
    return list_json


def five_operations(tmp_list):
    """Функция выводит последние 5 EXECUTED операций"""
    if tmp_list == []:
        return "operation list"
    date_list = []
    for dicts in tmp_list:
        if "state" not in dicts.keys():
            continue
        elif dicts["state"] == "EXECUTED":
            date_list.append(dicts["date"])
    date_list.sort(reverse=True)
    return date_list[:5]



def main(LINK):
    if LINK == []:
        return "empty list"
    tmp_list = tranzact_execute(LINK)
    ready_list = five_operations(tmp_list)
    for date in ready_list:
        for dicts in tmp_list:
            if "date" not in dicts.keys():
                continue
            if date == dicts["date"]:
                date = date[5:10].replace('-', '.') + '.' + date[:4]
                if "from" not in dicts.keys():
                    number_card = "non card"
                else:
                    number_card = " ".join(dicts["from"].split()[:-1] + [
                        dicts["from"].split()[-1][:4] + " " + dicts["from"].split()[-1][4:6] + "**" + "****" +
                        dicts["from"].split()[-1][-4:]])

                print(f"{date} {dicts['description']}\n"
                      f"{number_card} -> {dicts['to'][:4]} **{dicts['to'][-4:]}\n"
                      f"{dicts['operationAmount']['amount']} {dicts['operationAmount']['currency']['name']}\n")
    return "main complited"

if __name__ == "__main__":
    LINK = "..\operations.json"
    main(LINK)
