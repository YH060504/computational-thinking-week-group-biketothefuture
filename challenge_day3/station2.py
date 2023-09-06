import datetime


def solution_station_2(date_string):
    days = ["月曜日", "火曜日", "水曜日",
            "木曜日", "金曜日", "土曜日", "日曜日"]

    year, month, day = map(int, date_string.split('-'))
    date_obj = datetime.date(year, month, day)

    return days[date_obj.weekday()]


# Test the function
print(solution_station_2('2024-07-10'))
