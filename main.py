class MyError(Exception):
    def __init__(self, text):
        self.txt = text


f = open('text.txt')
mas = []
for line in f:
    mas = [int(x) for x in line.split()]
    for i in range(len(mas)):
        try:
            if mas[i] % 2 == 0:
                raise MyError("You have even number")
        except MyError:
            mas[i] = -1
print(mas)
f.close()

