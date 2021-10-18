import datetime
from itertools import permutations, product #библиотека для комбинирования элементов

#определяем компоненты, из которых будет состоять пароль
specials = ['!','@','#','$','.','*','^','?'] #спецсимволы

#месяца и времена года
words = ["April", "Atdhfkm", "August", "Autumn", "Besna", "Becna", "B.km", "Ctynz,hm", "December", "Dtcyf", "Fduecn", "February", "Fghtkm", "January", "Jctym", "Jrnz,hm", "July", "June", "Ktnj", "Leto", "Ltrf,hm", "March", "May", "November", "October", "Ocen", "Osen" "Pbvf", "September", "Spring", "Summer", "Vesna", "Vecna", "Vfhn", "Winter", "Yjz,hm", "Zima", "Zydfhm", "3ima"]
# года с 2010 по текущий + 2 в форматах YYYY и YY
now = datetime.datetime.now()
years = list(range(2010,now.year+2))+list(range(10,int(str(now.year)[2:])+2))

#открываем файл для сохранения паролей
f_o = open("calendar_passwords.txt", "w") 

#генерируем список специальных символов от 0 до 3 элементов
special_array=[]
for i in range(0,4):
    for subset in product(specials,repeat=i):
        special_array.append(''.join(subset))

#собираем компоненты в пароль
for word in words:
    for year in years:
        for special in special_array:
            for password in permutations([word, str(year), special], 3):
                f_o.write(''.join(password)+"\r\n")

#закрываем файл
f_o.close()
