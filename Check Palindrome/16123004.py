s = raw_input()

n = len(s)

palin = True
for i in n/2:
	if s[i] != s[-(i+1)]:
		palin = False

if palin:
	print("Palindrome")
else:
	print("Not Palindrome")
