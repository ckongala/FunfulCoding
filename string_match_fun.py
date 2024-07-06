print("chinni")

all_letters = 'abcdefghijklmnopqrstuvwxyz '

desired_string = 'hello world'

s = ''
for i in desired_string:
    for k in all_letters:
        if i == k:
            s+=k
            print(s)
            break
        print(s + k)
