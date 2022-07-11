print0 = ("###", "# #", "# #", "# #", "###")
print1 = ("  #", "  #", "  #", "  #", "  #")
print2 = ("###", "  #", "###", "#  ", "###")
print3 = ("###", "  #", "###", "  #", "###")
print4 = ("# #", "# #", "###", "  #", "  #")
print5 = ("###", "#  ", "###", "  #", "###")
print6 = ("###", "#  ", "###", "# #", "###")
print7 = ("###", "  #", "  #", "  #", "  #")
print8 = ("###", "# #", "###", "# #", "###")
print9 = ("###", "# #", "###", "  #", "###")

printList = [print0, print1, print2, print3, print4, print5, print6, print7, print8, print9]

def led(numbers):
    inputDigits = [int(x) for x in numbers]
    for i in range(5):
        result = ""
        for j in inputDigits:
            result += printList[j][i] + " "
        print(result, sep="\n")

led(input("Please enter a positive value: "))
