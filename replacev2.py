# code inspired by https://stackoverflow.com/questions/4746190/find-and-replace-within-a-text-file-using-python
# Thanks to @sarahmcole who wrote this

n = 1
f1=open("search.json", "r")
f2=open("output2.json", "w")

#
f2.write("[\n")
for line in f1:


	addComma=","
	if n==1:
		addComma=""	
	

	n = n+1
	f2.write(line)

f2.write("\n]")
f1.close()
f2.close()
