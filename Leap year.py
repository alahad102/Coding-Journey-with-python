def is_leap(year):
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 == 0:
               leap = True
               return leap
            else:
                leap = False
                return leap
        else:
            leap = True
            return leap

    else:
        leap = False
        return leap

year = int(input())
print(is_leap(year))