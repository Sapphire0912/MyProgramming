class Date:
    def __init__(self, year, month, day):
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.x = 0
        # 檢查格式
        if year >= 0 and 0 < month <= 12:
            self.year = year
            self.month = month
            if 0 < day <= 31:
                self.day = day
                self.months = months
                # 檢查閏年
                if year % 4 == 0:
                    if year % 100 == 0:
                        self.months = months
                    if year % 400 == 0:
                        months[1] = 29
                        self.months = months

                        # debug 時間相減的問題
                        if month <= 2 and day != self.months[1]:
                            self.x = 0
                        else:
                            self.x = 1

                if month == 2 and day > months[1]:
                    raise ValueError("日期格式錯誤")
            else:
                raise ValueError("日期格式錯誤")
        else:
            raise ValueError("日期格式錯誤")

    def __sub__(self, other):
        # T2 > T1
        if self.year < other.year:
            self, other = other, self
        elif self.year == other.year:  # T2(Year) = T1(Year)
            if self.month < other.month:
                self, other = other, self
            elif self.month == other.month:
                if self.day < other.day:
                    self, other = other, self

        days = self.day  # 把天數加上去
        odays = other.day 
        ydif = self.year - other.year  # 兩個時間的年差
        for i in range(ydif):
            days += sum(self.months)   # 年差換成天數
        for i in range(self.month):
            days += self.months[i]  # 月轉換成天
            
        if self.x:
            days += (ydif // 4)  # 處理閏年的日期差
        else:
            days-= 1  
        if other.x:
            odays += (ydif // 4)

        for j in range(other.month):
            odays += other.months[j]
            
        result = days - odays
        return result

    def show(self):
        return (self.year, self.month, self.day)

time2 = Date(2000, 2, 1)
time1 = Date(1999, 12, 25)
print("日期1: ",time1.show())
print("日期2: ", time2.show())

sub = time1.__sub__(time2)
print("時間差: ", sub)