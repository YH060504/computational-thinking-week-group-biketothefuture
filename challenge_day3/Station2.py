import datetime

date_obj = datetime.date(2023, 1, 9)

days = ["月曜日", "火曜日", "水曜日",
        "木曜日", "金曜日", "土曜日", "日曜日"]

day_name = days[date_obj.weekday()]

print(day_name)
