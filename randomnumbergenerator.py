#Made by Levente Bajnóczi
#2022.01.18 (yyyy.mm.dd)

from audioop import minmax
import random


#Set up the default values for the variables
def setupVars():
    returnNumbers = False #If you use this script standalone it's a constant, otherwise modifiable
    writeToFile = False #If true the output will be written to a file, otherwise it will be printed to the console
    showOutput = True #When writeToFile is True, prints the generated numbers to the console
    minNum = 0 #Determines the minimum number that can be generated
    maxNum = 100 #Determines the maximum number that can be generated
    amount = 10 #This amount of random numbers will be generated
    userInputs(returnNumbers, writeToFile, showOutput, minNum, maxNum, amount)


#Here we take inputs from the user to satisfy their preference
def userInputs(returnNumbers, writeToFile, showOutput, minNum, maxNum, amount):
    print("RANDOM SZAM GENERATOR")
    print("Csak egesz szamokat adj meg minden esetben.")
    print("Az alapbeallitasok zarojelben lathatoak.")
    print("Ha nem kivanod modositani akkor hagyd uresen es nyomj entert")
    minNumtmp = str(input(f"A legkisebb generalhato szam ({minNum}): "))
    maxNumtmp = str(input(f"A legnagyobb generalhato szam ({maxNum}): "))
    amounttmp = str(input(f"Ennyi szam legyen generalva ({amount}): "))
    print("______________________________________________________")
    print("A kovetkezo kerdesekre csak '0' vagy '1' valaszt adjon")
    print("0 - Nem, 1 - Igen")
    writeToFiletmp = str(input(f"Szeretned egy fajlba elmenteni a random generalt elemeket? ({writeToFile}): "))
    showOutputtmp = str(input(f"Szeretned ha a generalt szamok megjelenitesre kerulnenek? ({showOutput}): "))
    print("\n\r")

    if minNumtmp == "":
        del minNumtmp
    else:
        try:
            minNum = int(minNumtmp)
            del minNumtmp
        except:
            userError()
    if maxNumtmp == "":
        del maxNumtmp
    else:
        try:
            maxNum = int(maxNumtmp)
            del maxNumtmp
        except:
            userError()
    if amounttmp == "":
        del amounttmp
    else:
        try:
            amount = int(amounttmp)
            del amounttmp
        except:
            userError()
    if writeToFiletmp == "":
        del writeToFiletmp
    else:
        if writeToFiletmp == "0":
            writeToFile = False
            del writeToFiletmp
        elif writeToFiletmp == "1":
            writeToFile = True
            del writeToFiletmp
        else:
            userError()
    if showOutputtmp == "":
        del showOutputtmp
    else:
        if showOutputtmp == "0":
            showOutput = False
            del showOutputtmp
        elif showOutputtmp == "1":
            showOutput = True
            del showOutput
        else:
            userError()

    generator(returnNumbers, writeToFile, showOutput, minNum, maxNum, amount)


#This function will be called when the user typed in some data that is inaccurate
#Therefor the script will exit
def userError():
    print("\n\rValami hiba tortent.")
    print("Nyomj entert a kilepeshez...")
    input()




#This function will generate the numbers
def generator(returnNumbers, writeToFile, showOutput, minNum, maxNum, amount):
    generatedNumbers = [] #Define a list if user wants to return the generated values. If not, then delete it later.

    if returnNumbers == True:
        for i in range(amount):
            generatedNumbers.append(random.randint(minNum, maxNum))
        return generatedNumbers
    elif writeToFile == True:
        fName = f"randomnumber_{random.randint(1000, 9999)}.txt"
        f = open(fName, "x")
        if showOutput == False:
            for i in range(amount):
                f.write(f"{random.randint(minNum, maxNum)}\n\r")
            print("\n\r|_______________________|")
            print("| A generalt fajl neve: | ")
            print(f"| {fName} |")
            print("|_______________________|")
        else:
            for i in range(amount):
                tmp = random.randint(minNum, maxNum)
                print(tmp)
                f.write(f"{tmp}\n\r")
            print("\n\r|_______________________|")
            print("| A generalt fajl neve: | ")
            print(f"| {fName} |")
            print("|_______________________|")
    else:
        for i in range(amount):
            print(random.randint(minNum, maxNum))
        print("\n\rA kilepeshez nyomj entert...")
        input()
    


if __name__ == '__main__':
    setupVars()
