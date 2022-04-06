
class Date:
    def __init__(self):
        self.year_int = int(input('Ingresa un año: '))
        self.month_int = int(input('Ingresa un mes (número): '))
        self.day_int = int(input('Ingresa un día: '))

    def year(self):
        year_str = str(self.year_int)
        return year_str

    def month(self):
        month_str = ''
        if self.month_int < 10:
            month_str = f'0{str(self.month_int)}'
        else:
            month_str = str(self.month_int)
        return month_str

    def day(self):
        day_str = ''
        if self.day_int < 10:
            day_str = f'0{str(self.day_int)}'
        else:
            day_str = str(self.day_int)
        return day_str
