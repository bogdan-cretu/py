sample = input("Please enter your birthday digits with no separation: ")

digit_of_life = 0
for i in sample:
    integ = int(i)
    digit_of_life += integ
str_digit_of_life = str(digit_of_life)
if len(str_digit_of_life) > 0:
    new_digit = 0
    for i in str_digit_of_life:
        int_i = int(i)
        new_digit += int_i
    print(new_digit)
