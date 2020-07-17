my_name="이서영"
print(f"my name is {my_name}.") #{}안에서 연산도 가능. ex) my_name.upper()

#리스트 안에 리스트
list_in_list=[1, 2, [3, 4, 5], 6]
print(len(list_in_list))
list_in_list[2][0] #index=2에서의 0번째 (chained index)

#조건문
name = "이서영"
if name == "이서영":
    print("백현을 JONNA 사랑한다.")
else:
    print("오늘부로 입덕한다.")

#ternary operator
name = "이서영"
value = 0 if name == "이서영" else 1