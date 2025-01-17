f1 = open("files/diary.txt", "r")
print(f1.read())
f1.close()

f2 = open("files/diary.txt", "w")
print(f2.write(" Hola JC "))
f2.close()