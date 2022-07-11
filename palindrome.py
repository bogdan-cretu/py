sample = "1a23a1"


lower_sample = sample.lower()
new_sample = lower_sample.replace(" ", "")
reverse_sample = new_sample[::-1]
if new_sample == reverse_sample:
    print("Is palindrome")
else:
    print("Is not palindrome")