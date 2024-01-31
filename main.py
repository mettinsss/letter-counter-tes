times  = 0
sentence = input("Enter sentence: ")
for i in range (0,len(sentence)):
  if sentence[i]=="e" or sentence[i]=="a":
    times = times+1
print("a or e is present",times,"time(s)")