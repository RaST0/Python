
# Дата и время

from datetime import date, time, datetime, timedelta, tzinfo
import locale
from pytz import timezone
import pytz
# Дата
d = date.today()
print(d)
d = date(2050,10,25)
print(d)
print(f"{d.year=}")
print(d.strftime("Год = %Y, Месяц = %m, День = %d"))
print()
# Время
t = time()
print(t)
t = time(20,15,30)
print(t)
print(f"{t.hour=}")
print(t.strftime("Время = %H : %M : %S"))
print()
# Дата и время - Перевод!!
dt = datetime.now()
print(dt)
print(f"Дата = {dt.year}.{dt.month}.{dt.day} {dt.hour}:{dt.minute}:{dt.second}")
print(dt.strftime("%d %B %Y %A"))
print()

# Преобразование из строки в дату и время
x = datetime.strptime("2025/12/02", "%Y/%m/%d")
print(x)
x = datetime.strptime("2025.12.02 14:55", "%Y.%m.%d %H:%M")
print(x)
print()

# Операции с датами
# timedelta() - промежуток времени

t_3h_00m = timedelta(hours=3)
t_2h_15m = timedelta(hours=2, minutes = 15)
t_2w = timedelta(weeks=2)

now = datetime.now()
print(f"Сейчас + 2 часа + 15 минут = ".ljust(30), now + t_2h_15m)
print(f"Сейчас + 2 недели = ".ljust(30), now + t_2w)
print()

print("----------Homework----------\n")
print("1. Дата на русском языке:")
locale.setlocale(locale.LC_ALL, "ru")
print(dt.strftime("%d %B %Y %A"))
print()
print("2. Использование временных зон:")
utc = pytz.utc
eastern = timezone('US/Eastern')
amsterdam = timezone('Europe/Amsterdam')
time = datetime.now()
print("Московское время:")
print(time.strftime("Время = %H:%M:%S"))
time_utc = time.astimezone(utc)
print("Часой пояс - UTC")
print(time_utc.strftime("Время = %H:%M:%S"))
time_eastern = time.astimezone(eastern)
print("Часой пояс - EST")
print(time_eastern.strftime("Время = %H:%M:%S"))
print("Часой пояс - CET")
time_amsterdam = time.astimezone(amsterdam)
print(time_amsterdam.strftime("Время = %H:%M:%S"))