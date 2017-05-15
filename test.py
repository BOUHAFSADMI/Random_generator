s=0
with open("randoms.txt","r") as file:
	for line in file:
		print(line)
		s+=1
print(s)
