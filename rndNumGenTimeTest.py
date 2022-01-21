from randomnumbergenerator import generator
from random import randint
from timeit import default_timer as timer
from sys import getsizeof

fName = f"jelentes_{randint(100, 999)}.txt"
f = open(f"{fName}", "x")

def timemeasure(amount):
    timeStart = timer()
    randomNumberList = generator(True, False, False, 0, 1000000, amount)
    timeEnd = timer()
    fileSizeStr = f"A legenerált számok mérete: {getsizeof(randomNumberList)}"
    strToWrite = f"{amount} szám legenerálása:\n{timeEnd - timeStart} másodperc\n{fileSizeStr}\n\n"
    strToConsole = f"\n{amount} szám legenerálása:\n{timeEnd - timeStart} másodperc\n\n"
    f.write(strToWrite)
    print(f"{strToConsole}\n")

def userInput():
    howMany = int(input("Hány tesztet szeretnél futtatni: "))
    amountlst = []
    for i in range(howMany):
        amountlst.append(int(input(f"{i+1}. Hány elemből áljon a(z) {i+1}. teszt: ")))
    c = 1
    for amount in amountlst:
        timemeasure(amount)
        c += 1

userInput()
print(f"A jelentés létrehozva az alábbi néven:\n{fName}\n")
