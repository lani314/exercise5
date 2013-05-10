# Creates a list of 0 26 times
# So, counter = [0, 0, 0, etc...]
counter = [0]*26

# Loop through text and retrieve values

for i in lower_text:	
	# Make values ASCII values and set them to variable
	intValue = ord(i)

	#test if character is a letter from a-z (97-122)
if intValue >= 97 and intValue <= 122:

	#subtract 97 to determine the position in the list
	#now each letter coordinates to position in a list
# it is NOT yet in list but is now represented by integers that parallel list (0-25)
# so, a = 0, b = 1, etc.
indexNum = intValue - 97

# now, we want to determine how many times they come up!
# so, count = counter[number here]
# this means we place the LETTER in 
# so, for e(4) for example... count = counter[4]
# THIS MEANS WE EXTRACT THE 4TH ELEMENT FROM THE LIST
		count = counter[indexNum]
		# NOW, WE REPLACE THE 0 (ORIGINAL VALUE) WITH 1 IN LIST POSITION
		counter[indexNum] = count + 1
		#This loop CONTINUES for all letters in lower_text


#print count to screen in alphabetical order
# goes through beginning of list, and continues on
for i in counter:
	print i