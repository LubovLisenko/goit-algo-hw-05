from _datetime import datetime
import random


# ф-ція яка розраховує кількість днів між заданою датою и поточною
def get_days_from_today(date):
# поточна дата днів
    day_today_int = datetime.today().toordinal()
    #дата яка передається днів
    try:
           current_date_int = datetime.strptime(date,'%Y-%m-%d').date().toordinal()
    except (ValueError, TypeError) as e:
      print(f"You have to input correct data format {e}")
      current_date_int = None
# різніця днів
    days = current_date_int - day_today_int
    return days

# a-ція генерує унікальну кількість значень quantity between min and max
def get_numbers_ticket(min, max, quantity):
    num = set()
    # exxception для параметрів якщо не відповідають умовам діапазону
    try:
        if min<1:
            raise ValueError('Min has to be more than 1')
        if max >1000:
            raise ValueError('Max has to be less 1000')
        if not (min<=quantity<=max):
            raise ValueError('Quantitty has to be between min and max')
        # створення quantity -кількості
        while len(num) < quantity:
            items = random.randint(min, max)
            num.add(items)

        lottery_numbers = sorted(list(num))
        return lottery_numbers
    except ValueError as e:
        print("Mistake in parametr", e)


print(get_days_from_today('2026-10-09'))
print(get_numbers_ticket(1,34,5))
