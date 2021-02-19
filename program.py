import datetime as dt

date_format = '%d.%m.%Y'

class Calculator:
    def __init__(self, limit):
        # class 'Calculator' is defined.
        # Objects of the class take one value - 'limit'
        self.limit = limit
        self.records = []  # empty list 'records' is defined

    def add_record(self, record):
        self.records.append(record)
        # return self.records
        # list 'records' takes object of 'Record' as a value

    def get_today_stats(self):
        now = dt.datetime.now()
        now_format = now.strftime('%d.%m.%Y')
        return sum(record.amount
                   for record in self.records
                   if record.date.strftime('%d.%m.%Y') == now_format)

    def get_week_stats(self):
        now = dt.datetime.now()
        now_format = now.strftime('%d.%m.%Y')
        date_week_ago = now-dt.timedelta(days=7)
        date_week_ago_format = date_week_ago.strftime('%d.%m.%Y')
        return sum(record.amount for record in self.records
                   if record.date >= date_week_ago.date()
                   and record.date <= now.date())


class Record:
    def __init__(self, amount, comment, date=None):
        # class 'Calculator' is defined.
        # Objects of the class take values - 'amount', 'date', 'comment'
        self.amount = amount
        self.comment = comment
        self.date = self.date_correct(date)

    def date_correct(self, date=None):
        if date is None:
            now = dt.datetime.now()
            return(now.date())
        else:
            date_format = '%d.%m.%Y'
            now_moment = dt.datetime.strptime(date, date_format)
            return(now_moment.date())


class CashCalculator(Calculator):
    USD_RATE = 73.89
    EURO_RATE = 89.30
    
    def get_today_cash_remained(self, currency: str):
        today_remainder = self.limit - self.get_today_stats()
        RUB_amount = today_remainder
        USD_amount = round(today_remainder/self.USD_RATE, 2)
        EURO_amount = round(today_remainder/self.EURO_RATE, 2)
        currency_list = {
                         'rub': ['руб', RUB_amount],
                         'usd': ['USD', USD_amount],
                         'eur': ['Euro', EURO_amount]
                         }
        if today_remainder > 0:
            return ('На сегодня осталось {} {}'.format(currency_list[currency][1], currency_list[currency][0]))
        elif today_remainder == 0:
            return 'Денег нет, держись'
        else:
            return ('Денег нет, держись: твой долг - {} {}'.format(abs(currency_list[currency][1]), currency_list[currency][0]))


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_left = self.limit - self.get_today_stats()
        if calories_left > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_left} кКал')
        else:
            return 'Хватит есть!'

