def mysplit(string):
    new_list = []
    word = ""
    for i in string:
        word += i
        if i == " ":
            new_list.append(word)
            word = ""
    new_list.append(word)
    new_list = [x.strip(' ') for x in new_list]
    while "" in new_list:
        new_list.remove("")
    return(new_list)


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))