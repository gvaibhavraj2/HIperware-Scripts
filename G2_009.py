import sys
import inflect
import random

#import the Rendering API package
from hiperware.outliers.image import *

# developer ID received from Hiperware
DEVELOPER_ID = "vaibhav@hiperware.com"

# question category
QUESTION_CATEGORY = {
            "grade": "Second",
            "subject": "Math",
            "skill_group": "Word Problems",
            "skill": "Applying addition"
            }

p = inflect.engine()

dict = {'counted at school': ['book', 'clock', 'computer', 'hat', 'pencil', 'phone', 'teacher'],
'got for birthday': ['balloon', 'book', 'box', 'lollypop', 'truck', 't-shirt'],
'had at family picnic': ['basket', 'burger', 'slice of cake', 'hotdog', 'glass of lemonade', 'chunk of pineapple', 'strawberry'],
'packed for trip': ['book', 'camera', 'suitcase', 'tent', 't-shirt'],
'saw at the store': ['bed', 'bike', 'box', 'broom', 'clock', 'computer', 'drum', 'hat', 'lamp'], 
'counted at the beach': ['balloon', 'basket', 'boat', 'bucket', 'butterfly', 'camera', 'cloud', 'dolphin', 'duck', 'fish', 'hotdog', 'shell', 'umbrella'],
'saw at the zoo': ['bird', 'butterfly', 'duck', 'fish', 'owl', 'turtle'],
'counted on the way to school': ['bike', 'plane', 'train', 'truck'],
'counted in the garden': ['bird', 'butterfly', 'mushroom', 'plant', 'rose', 'snail']};

girl_names = ["Jill", "Emily", "Liz", "Naomi", "Rachel", "Leilani", "Kate", "Cassidy", "Sarah", "Jenna", "Maria", "Suzie", "Olivia", "Claire", "Lucy", "Jane", "Sydney", "Zoie", "Emma", "Julie","Maya", "Vera", "Sofia", "Clara", "Dona", "Gina", "Yuki", "Akira", "Liu", "Angela", "Amina", "Neha"]
boy_names = ["Luke", "Craig", "John", "Ben", "Mike", "Louis", "Aiden", "Isaiah", "Miles", "Henry", "Theo", "Andrew", "Caleb", "Chris", "James", "Matthew", "Peter", "Paul", "Frank", "Martin","Aamir", "Lucas", "Boris", "Yury", "Mario", "Marco", "Nobu", "Han", "Li", "Carlos", "Salim", "Rishi"]

questions = [
				[
					[girl_names,boy_names],['counted'], ['book', 'clock', 'computer', 'hat', 'pencil', 'phone', 'teacher'],['at school. '],[girl_names,boy_names],['counted'],['. How many'],['did they count together?']
					],
	        	[
	        		[girl_names,boy_names],['saw'], ['bottle', 'shoppingcart'],['at the store. '],[girl_names,boy_names],['saw'],['. How many'],['did they see together?']
	        		],
	           	[
	           		[girl_names,boy_names],['scored'], ['in a videogame and'],[girl_names,boy_names],['scored'],['points. How many points did they count together?']
	           		],
	           	[
	           		[girl_names,boy_names],['has'],['red'], ['bell', 'pencil'],['and'],['yellow'],['. How many'],['does'],['have in total?']
	           		],
	           	[
	           		['At the aquarium, there are'],['fish in the arctic tank, and'], ['fish in the tropical tank. How many fish are there in total?']
	           		],
	           	#[
	           	#	[girl_names,boy_names],['and'],[girl_names,boy_names],['collect'], ['picture', 'medal', 'book', 'candy', 'keys', 'bells', 'shells', 'erasers', 'stickers', 'pennies', 'lego', 'star', 'lolly'],['. If'],['has'],['and'],['has'][', how many'],['do they have together?']
	           	#	],
	           	[
	           		["Mr. J's class read"],["books and Ms. T's class read"], ["books. How many books did the two classes read together?"]
	           		],
	           	[
	           		['To get ready for her party on'],[', Sarah got'],['balloon', 'lollypop', 'glasses of lemonade', 'chunks of pineapple', 'strawberry', 'hotdog', 'burger',  'icecream', 'bread'],['on'],['and then'],['on'],['. How many'],['did Sarah have in total for her party?']
	           		],
	           	[
					[girl_names,boy_names],['counted'], ['car', 'bike', 'house', 'trees'],['on the way to school. '],[girl_names,boy_names],['counted'],['. How many'],['did they see together?']
					],	
				[
					[girl_names,boy_names],['counted'], ['beach-ball', 'beach-chair'],['at the beach. '],[girl_names,boy_names],['counted'],['. How many'],['did they count together?']
					],	
	       	]	


boy_or_girl = ["girl_names","boy_names"]

his_or_her = ["her","his"]

verbs = ["see","pack","have","see","count","count","count","count","get"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

max_questions = 400

listOfCombinations = []
#currentCombination = []

def main():
	counter = 1
	for i in range(max_questions):
		flag = 0
		while flag == 0:	
			j = random.randint(0,1)
			k = random.randint(0,1)
			m = random.randrange(10,18)
			n = random.randrange(2,21-m)
			l = random.randint(0,8)
			#print j,k,m,n,l
			qnum = random.choice([0,1,3,4,5,6,7,8])
	      		h_s = random.randint(0,1)
			if [m,n,l,qnum,h_s] in listOfCombinations:
				continue
			else:
				listOfCombinations.append([m,n,l,qnum,h_s])
				flag = 1
			
			#print listOfCombinations
		
		generatequestion(j,k,m,n,l,qnum,h_s,counter)
		counter+=1

def generatequestion(j,k,m,n,l,qnum,h_s,z):
	builder = Builder(DEVELOPER_ID, QUESTION_CATEGORY)
	r = range(12,81)
	block = builder.Block()
	person1 = random.choice(eval(boy_or_girl[j]))
	person2 = random.choice(eval(boy_or_girl[k]))
	while person1 == person2:
		person2 = random.choice(eval(boy_or_girl[k]))
	person1_gender,person2_gender = his_or_her[j],his_or_her[k]
	q =  questions[qnum]
	if qnum==4 or qnum==5:
		sentence1 = q[0][0]+" "
		block.text(sentence1)
		x = str(m)
		y = str(n)
		block.text(x,color=GREEN_TEXT_COLOR)
		sentence2 = " "+q[1][0]+" "
		block.text(sentence2)
		block.text(y,color=GREEN_TEXT_COLOR)
		sentence3 = " "+q[2][0]+" "
		block.text(sentence3)
		if qnum==4:
		# create blocks list
			objectToBeDrawn = "fish1"
		else:
			objectToBeDrawn = "book"
	elif qnum==6:
		
		d1 = random.choice(days);
		sentence1 = q[0][0]+" "+d1+" "+q[1][0]+" "
		block.text(sentence1)
		x = str(m)
		y = str(n)
		block.text(x,color=GREEN_TEXT_COLOR)
		obj1= random.choice(q[2])
		obj = p.plural(obj1)
		
		d2 = random.choice(days)
		while d1==d2:
			d2 = random.choice(days)
		d3 = random.choice(days)
		while d3==d1 or d2==d1:
			d3 = random.choice(days)
		sentence2 = " "+obj+" "+q[3][0]+" "+d2+" "+q[4][0]+" "
		block.text(sentence2)
		block.text(y,color=GREEN_TEXT_COLOR)
		sentence3 = " "+obj+" "+q[5][0]+" "+d3+" "+q[6][0]+" "+obj+" "+q[7][0]
		block.text(sentence3)
		if obj1!= 'glasses of lemonade' and obj1!= 'chunks of pineapple' and obj1!= 'slice of cake':
			# create blocks list
			objectToBeDrawn = obj1
		else:
			objectToBeDrawn = obj1.split(" ")[2]
	elif qnum==1 or qnum==0 or qnum==8 or qnum==7:
		person1 = random.choice(eval(boy_or_girl[j]))
		person2 = random.choice(eval(boy_or_girl[k]))
		while person1 == person2:
			person2 = random.choice(eval(boy_or_girl[k]))
		sentence1 = person1+" "+q[1][0]+" "
		n1 =str(m)
		block.text(sentence1)
		block.text(n1,color=GREEN_TEXT_COLOR)
		obj1= random.choice(q[2])
		sentence2 = " "+p.plural(obj1)+" "+q[3][0]+" "+person2 +" "+q[5][0]+" "
		block.text(sentence2)
		block.text(str(n),color=GREEN_TEXT_COLOR)
		sentence3 = " "+q[6][0]+" "+p.plural(obj1)+" "+q[7][0]
		block.text(sentence3)	
		if obj1=='bottle':
			objectToBeDrawn = "bottle1"	
		elif obj1=='shoppingcart':
			objectToBeDrawn = "shopping_cart"	
		elif obj1=='trees':
			objectToBeDrawn = "little-tree"	
		else:
			objectToBeDrawn = obj1	
	elif qnum==2:
		person1 = random.choice(eval(boy_or_girl[j]))
		person2 = random.choice(eval(boy_or_girl[k]))
		while person1 == person2:
			person2 = random.choice(eval(boy_or_girl[k]))
		sentence1 = person1+" "+q[1][0]+" "
		n1 =str(m)
		block.text(sentence1)
		block.text(n1,color=GREEN_TEXT_COLOR)
		#obj1= random.choice(q[2])
		sentence2 = " "+q[2][0]+" "+person2 +" "+q[4][0]+" "
		block.text(sentence2)
		block.text(str(n),color=GREEN_TEXT_COLOR)
		sentence3 = " "+q[5][0]+" "
		block.text(sentence3)
	elif qnum==3:
		person1 = random.choice(eval(boy_or_girl[j]))
		sentence1 = person1+" "+q[1][0]+" "
		n1 =str(m)
		block.text(sentence1)
		block.text(n1,color=GREEN_TEXT_COLOR)
		obj1= random.choice(q[3])
		sentence2 = " "+q[3][0]+" "+q[4][0]+" "
		block.text(sentence2)
		block.text(str(n),color=GREEN_TEXT_COLOR)
		sentence3 = " "+q[5][0]+" "+p.plural(obj1)+" "+q[6][0]+" "+p.plural(obj1)+" "+q[7][0]+" "+person1+" "+q[8][0]
		block.text(sentence3)	
		if obj1=='bottle':
			objectToBeDrawn = "bottle1"	
		elif obj1=='shoppingcart':
			objectToBeDrawn = "shopping_cart"	
		else:
			objectToBeDrawn = obj1					
	builder.block(block,center = True)

		# create blocks list
	blocksImageke = []

		# 1st block
	blockImageka = builder.Block()
	blockImageka.grid(objectToBeDrawn, m/7+1, 7, num=m, size=SMALLEST_PICTURE_SIZE)
	blocksImageke.append(blockImageka)

		# 2nd block
	blockImageka = builder.Block()
	blockImageka.text(" + ", font_size=LARGE_FONT_SIZE)
	blocksImageke.append(blockImageka)

	# 3rd block
	blockImageka = builder.Block()
	blockImageka.grid(objectToBeDrawn, n/7+1, 7, num=n, size=SMALLEST_PICTURE_SIZE)
	blocksImageke.append(blockImageka)

		# draw all the blocks at once
	blockTextKa = builder.Block()
	blockTextKa.text(" =  ?")
	blocksImageke.append(blockTextKa)

	builder.blocks(blocksImageke,center=True)
							
	data_list, correct_list = [], []

	correct_choice = random.randrange(0,4)
		
	checkbox_data_1 = builder.Block()
	checkbox_data_1.text(str(m+n))
		#print(m+n)
	r.remove(m+n)

	correct_list.append(correct_choice==0)

	checkbox_data_2 = builder.Block()
	choice2 = random.choice(r)
	checkbox_data_2.text(str(choice2))
	r.remove(choice2)	

	correct_list.append(correct_choice==1) 


	checkbox_data_3 = builder.Block()
	choice3 = random.choice(r)
	checkbox_data_3.text(str(choice3))
	r.remove(choice3)

	correct_list.append(correct_choice==2)

	checkbox_data_4 = builder.Block()
	choice4 = random.choice(r)
	checkbox_data_4.text(str(choice4))
	r.remove(choice4)

	correct_list.append(correct_choice==3)

	if correct_choice==0:
		data_list.append(checkbox_data_1)
		data_list.append(checkbox_data_2)
		data_list.append(checkbox_data_3)
		data_list.append(checkbox_data_4)
	elif correct_choice==1:
		data_list.append(checkbox_data_2)
		data_list.append(checkbox_data_1)
		data_list.append(checkbox_data_3)
		data_list.append(checkbox_data_4)
	elif correct_choice==2:
		data_list.append(checkbox_data_3)
		data_list.append(checkbox_data_2)
		data_list.append(checkbox_data_1)
		data_list.append(checkbox_data_4)
	else:
		data_list.append(checkbox_data_4)
		data_list.append(checkbox_data_3)
		data_list.append(checkbox_data_2)
		data_list.append(checkbox_data_1)
	# draw all the checkboxes
	builder.checkboxes(data_list, correct_list, cols=1)
	builder.save("./output/G2_009", "G2_009-"+str(z))
	#print(person1+" "+sentence1+". "+person2+" "+split_sentence[0]+" "+str(n)+" "+p.plural(object_of_the_question)+". How many "+p.plural(object_of_the_question)+ " did they "+ verbs[l]+" all together?")

if __name__ == '__main__':
	main()