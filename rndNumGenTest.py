from randomnumbergenerator import generator


def teszt():
    randomNumberList = generator(True, False, False, 100, 999, 10)
    
    for element in randomNumberList:
        print(element)
    print(randomNumberList)


if __name__ == "__main__":
    teszt()
