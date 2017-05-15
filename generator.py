import random
import string

str={"abcdefghijk",}
for _ in range(0,3000):
	str.add(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))

file = open("randoms.txt","w")
for item in str:
	file.writelines("email-address+" + item + "@gmail.com\n")




