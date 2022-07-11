#first version
sample = "donut"
compared_to = "Nabucodonosor"


for i in sample:
    result = compared_to.find(i)
    if result == -1:
        print("No")
    elif i == sample[-1]:
        print("Yes")
        break
    elif result != -1:
        continue

    else:
        print("No")
        break

#second version
# sample = input("Please enter sample: ")
# compared_to = input("Enter string to search in: ")

# result = compared_to.find('dog')
# print(result)

# sample_list = []
# compared_to_list = []
#
# lower_sample = sample.lower()
# lower_compare = compared_to.lower()
#
# new_sample = lower_sample.replace(" ", "")
# new_compared_to  = lower_compare.replace(" ", "")
#
#
# for i in new_sample:
#     sample_list.append(i)
# for i in new_compared_to:
#     compared_to_list.append(i)
#
# sample_list.sort()
# compared_to_list.sort()
#
# for i in sample_list:
#     if i == sample_list[-1]:
#         print("Yes")
#     else:
#         if i in compared_to_list:
#             continue
#         else:
#             print("No")
#             break


