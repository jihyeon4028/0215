# Exercise1
user_second = input('초단위의 시간 : ')
# print('second 변수의 타입 =', type(user_second))
user_second = int(user_second)
# print('second 변수의 타입 =', type(user_second))
hour = user_second // 3600
result = user_second % 3600
minute = result // 60
second = result % 60
print(user_second, "초는", hour, "시간", minute, "분", second, "초입니다.")