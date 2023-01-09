# Создайте текстовый файл.
# Запишите в него 10 рандомных значений.
# После прочтите этот файл, определите все возможные комбинации и запишите их в другой файл.
# Для нового файла вычислите медиану и среднее значение.

import random
import itertools
import statistics

with open("random.txt","w") as f:
    l_ = [random.randint(1, 99) for x in range(10)]
    for i in l_:
        f.write(str(i)+"\n")

with open("random.txt","r") as f:
    l_2 = f.readlines()
    l_2 = [x.rstrip() for x in l_2]
    l_3 = itertools.combinations(l_2,3)
    l_3 = [x for x in l_3]

with open("random_new.txt","w") as f:
    for b in l_3:
        f.write(str(b) + "\n")

l_4 =[]
for n_1 in l_3:
    for n_2 in n_1:
        l_4.append(int(n_2))


print("median:  ",statistics.median((l_4)))
print("maen:  ",statistics.mean(l_4))

