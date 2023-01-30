num=int(input('년도를 입력하세요:'))



if num%400 == 0:
        print('윤년입니다')
elif num%4 == 0 and num%100 != 0:
    print('윤년')  
else:
    print('윤년이아닙니다')
