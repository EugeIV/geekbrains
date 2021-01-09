class Data:
    def __init__(self, day_month_year: str):
        self.day_month_year = day_month_year

    @classmethod
    def date_to_date(cls, day_month_year):
        data_list = day_month_year.split('-')
        return int(data_list[0]), int(data_list[1]), int(data_list[2])

    @staticmethod
    def validation(data):
        if 1 <= Data.date_to_date(data)[0] <= 31:
            if 1 < Data.date_to_date(data)[1] <= 12:
                if 0 < Data.date_to_date(data)[2]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


# item = Data("29-12-2020")
# print(item.day_month_year)
# print(Data.date_to_date("29-12-2020"))
print(Data.validation("29-12-2020"))
