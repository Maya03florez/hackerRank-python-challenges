def is_leap(year):
    # Write your logic here
    # first solution
    # if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    #     return True
    # else:
    #     return False

    # second solution
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    

year = int(input())
print(is_leap(year))