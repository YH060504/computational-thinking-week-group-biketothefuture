import datetime


def solution_station_2(year, month, day):
    days = ["月曜日", "火曜日", "水曜日",
            "木曜日", "金曜日", "土曜日", "日曜日"]

    date_obj = datetime.date(year, month, day)

    return days[date_obj.weekday()]


print(solution_station_2(2023, 3, 26))
