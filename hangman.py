

# # print(random.random())
# # print(random.randint(1,200))
# # print(random.randrange(1,200,3))
# # print(random.uniform(1.0,2.5))


import random
from sys import exit

words=['rings' , 'obesity' , 'right' , 'whisper' , 'paper' , 'made' , 'unlock' , 'creator' , 'excuse' , 'chess' , 'berry' , 'partner' ]
word=random.choice(words)

# You can uncomment below line if you want to know which is the correct word at start
# print("Correct word is %s" % word)

list2=[""]*len(word)
counter=0
c=0
def hang():
	ab = input("Enter a letter you think will be there in a word(you got 3 extra chance for wrong prediction): ")
	
	# Stores result of prediction
	result = False

	if ab in word:
		result = True

		# Store indexes of all occurences of letter ab
		list1=[]

		# Finding all the occureces of letter ab
		for i in range(len(word)):
			if(ab == word[i]):
				list1.append(i)
			# else:
			# 	pass
		
		if len(list1)>1:
			global c
			c=len(list1)
		for j in range(len(list1)):
			d=list1[j]

			# Inserting letter ab at index d. Note that it does not replaces previous letter in list2
			# I think you want ot replace. So do:
			list2[d] = ab
			# list2.insert(d,ab)
		
		print(str1.join(list2))
	else:
		global counter
		counter+=1
	
	# What the use of again providing 3 chances to predict correct letter.
	# As you are already calling hang() equal to number of letters in the word at the bottom
	
	# else:
	# 	print("Wrong choice..enter a word one more time: ")
	# 	global counterrehehrhierhiehtehfheterehtrhwrefhrofeforofortjifsndkforhfdnngeojiwreonnkfdbdfhiinmaafdhimasnhi oarihae whats ruiyyiour nanme
	# 	while counter<3:
	# 		res=hang()
	# 		counter=counter + 1
	# 	else:
	# 		print("you lose")
	# 		exit()

	return result

print("Correct word is %s" % word)

res = False
win=0
for j in range(len(word)+3):
	res=hang()
	if(res == True):
		win+=1
		if c>1:
			if win==len(word)-1:
				print("you win the game")
				exit()
		elif win==len(word):
			print ("you win the game")
			exit() 
	elif counter == 3:
		print ("you loose the game")
		exit()
	# if res=='false':
	# 	print("Wrong choice..enter a word one more time: ")
	# 	while counter<3:
	# 		res=hang()
	# 		counter=counter + 1
	# 	print("\nLoser!!! Get Lost.")
	# 	print("Correcst word is %s" % word)

 #if(res == True):
#	print("Your prediction is correct.")
#	exit(0)
