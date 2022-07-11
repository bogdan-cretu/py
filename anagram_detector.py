sample = input("Please insert first text: ")
compared_to = input("Please insert second text: ")

sample_list = []
compared_to_list = []

lower_sample = sample.lower()
lower_compare = compared_to.lower()

new_sample = lower_sample.replace(" ", "")
new_compared_to  = lower_compare.replace(" ", "")

for i in new_sample:
    sample_list.append(i)
for i in new_compared_to:
    compared_to_list.append(i)

sample_list.sort()
compared_to_list.sort()

if len(new_sample) == len(new_compared_to):
    if sample_list == compared_to_list:
        print("Anagram")
    else:
        print("Not anagram")
else:
    print("Not anagram, text length different")

# print(sample_list)
# print(compared_to_list)