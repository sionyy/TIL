test_status2 = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

lst_test2 = list(test_status2.items())


count2 = 0
cheat2=[]
for i in range(1,len(lst_test2)+1):
    if lst_test2[count2][1] == 'cheating':
        del cheat2[count2]
        coun2=count2+1
    else:
        count2=count2+1

print(cheat2)