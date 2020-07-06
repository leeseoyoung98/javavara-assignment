str1 = input()
str2 = input()
if int(str2[0]) >= len(str1):
    print("The number you gave is too large!")
else:
    my_str1 = str1[:int(str2[0])]
    my_str2 = str1[int(str2[0])+1:]
    print(my_str1 + str2[2] + my_str2)

#성공

