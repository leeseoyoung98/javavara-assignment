def is_leap(year):
    answer = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                answer = True
            else:
                answer = False
        else:
                answer = True
    else: 
                answer = False
    return answer
   
year = int(input())
print(is_leap(year))
#성공