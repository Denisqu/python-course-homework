




class Helper:
    @staticmethod
    def get_weekday(number):
        if type(number) is float:
            raise TypeError("Аргумент не является целым числом")
        if number < 0 or number > 7:
            raise ValueError("Аргумент не принадлежит требуемому диапазону")
        map = {
            1: "пн",
            2: "вт",
            3: "ср",
            4: "чт",
            5: "пт",
            6: "сб",
            7: "вск"
        }
        return map[number]

weekday1 = Helper.get_weekday(1)
print(weekday1)
weekday100 = Helper.get_weekday(100)
print(weekday100)