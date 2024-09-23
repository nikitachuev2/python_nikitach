
# Запрашиваем у пользователя день, месяц и год рождения
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))

# Определяем квартал года, в котором родился пользователь
if month <= 3:
    print("Вы родились в первом квартале")
elif month <= 6:
    print("Вы родились во втором квартале")
elif month <= 9:
    print("Вы родились в третьем квартале")
else:
    print("Вы родились в четвертом квартале")

# Определяем, был ли год рождения пользователя високосным
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Вы родились в високосном году")
else:
    print("Вы не родились в високосном году")

# Определяем, сколько дней прошло с даты рождения
import datetime as dt
current_date = dt.date.today()
birth_date = dt.date(year, month, day)

# Вычисляем количество дней, прошедших с даты рождения
if current_date.year == birth_date.year:
    days_since_birth = (current_date - birth_date).days
elif current_date.year == birth_date.year + 1:
    if birth_date.month == 12 and birth_date.day == 31:
        days_since_birth = 365
    else:
        days_since_birth = (dt.date(current_date.year, 1, 1) - birth_date).days + (current_date - dt.date(current_date.year, 1, 1)).days
else:
    years_passed = current_date.year - birth_date.year
    days_in_years = years_passed * 365.25
    days_in_current_year = (current_date - dt.date(current_date.year, 1, 1)).days
    days_since_birth = int(days_in_years + days_in_current_year)

print("С даты вашего рождения прошло", days_since_birth, "дней.")
