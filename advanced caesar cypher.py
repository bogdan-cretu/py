def caesar(strng):
    control = 0
    while control == 0:
        user_input = input("Please enter a shift value between 1-25: ")
        if int(user_input) not in range(1,26):
            print("The provided number is out of range.")
        else:
            control += 1
            word = ""
            for i in strng:
                inumber = ord(i) + int(user_input)
                if ord(i) in range(65,91):
                    if inumber > 90:
                        inumber -= 26
                        word += chr(inumber)
                    else:
                        word += chr(inumber)

                elif ord(i) in range(97,123):
                    if inumber > 122:
                        inumber -= 26
                        word += chr(inumber)
                    else:
                        word += chr(inumber)
                elif i.isnumeric():
                    word += i

                elif ord(i) == 32:
                    word += i
                else:
                    word += chr(inumber)
            print("Your encripted sentance is",word)

caesar(input("Please enter a sentance: "))

