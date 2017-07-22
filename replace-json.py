# code inspired by https://stackoverflow.com/questions/4746190/find-and-replace-within-a-text-file-using-python
# Thanks to @sarahmcole who wrote this

n = 1
f1=open("search.json", "r")
f2=open("output.json", "w")

#
f2.write("{")
for line in f1:

#  line = line.replace('"tweet"', '"tweet' + str(n) + '"')
	addComma=","
	if n==1:
		addComma=""	
	
	line = addComma+'"tweet' + str(n) + '":'+line
	n = n+1
	f2.write(line)

f2.write("}")
f1.close()
f2.close()
