import sys
import inflect
import random

#import the Rendering API package
from hiperware.outliers.image import *

# developer ID received from Hiperware
DEVELOPER_ID = "vaibhav@hiperware.com"

# question category
QUESTION_CATEGORY = {
            "grade": "Third",
            "subject": "Math",
            "skill_group": "Multiplication & Division",
            "skill": "Division"
            }

p = inflect.engine()

dict = {'evenly divided among': [['basket', 'box'],['book', 'key', 'lemon', 'lollypop',' cake',' medal', 'pencil',' shell',' strawberry']],
'made money selling':['balloon', 'basket', 'bell', 'burger', 'cake', 'hotdog', 'glasses of lemonade', 'lollypop', 'pencil', 'plant', 'rose', 'strawberry', 't-shirt'],
'A was carrying people': [['If there are people in each'],['train','plane'],['car','row']],

};


girl_names = ["Jill", "Emily", "Liz", "Naomi", "Rachel", "Leilani", "Kate", "Cassidy", "Sarah", "Jenna", "Maria", "Suzie", "Olivia", "Claire", "Lucy", "Jane", "Sydney", "Zoie", "Emma", "Julie","Maya", "Vera", "Sofia", "Clara", "Dona", "Gina", "Yuki", "Akira", "Liu", "Angela", "Amina", "Neha"]
boy_names = ["Luke", "Craig", "John", "Ben", "Mike", "Louis", "Aiden", "Isaiah", "Miles", "Henry", "Theo", "Andrew", "Caleb", "Chris", "James", "Matthew", "Peter", "Paul", "Frank", "Martin","Aamir", "Lucas", "Boris", "Yury", "Mario", "Marco", "Nobu", "Han", "Li", "Carlos", "Salim", "Rishi"]

boy_or_girl = ["girl_names","boy_names"]

his_or_her = ["her","his"]

verbs = ["see","pack","have","see","count","count","count","count","get"]
special_q = "read pages in hours."
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
			x = random.randint(2,10)
			n = random.randint(2,10)
			m = n*x
			if [m,n] in listOfCombinations:
				continue
			elif  m%10 != n%10:
				continue
			else:
				listOfCombinations.append([j,m,n])
				flag = 1
			
			#print listOfCombinations
		
		generatequestion(j,m,n,counter)
		counter+=1

def generatequestion(j,m,n,z):
		# create Builder() class instance (DEVELOPER_ID and QUESTION_CATEGORY are required)
		builder = Builder(DEVELOPER_ID, QUESTION_CATEGORY)
		block = builder.Block()
		sentences = dict.keys()
		r = range(2,50)
		l = random.randint(0,3)
		#print(sentences)
		if l==2 :
			object1 = random.choice(dict.get(sentences[l])[1])
			object2 = random.choice(dict.get(sentences[l])[2])
			#print(object_of_the_question)
			split_sentence = sentences[l].split(" ")
			split_sentence.insert(1,object1)
			split_sentence.insert(4,str(m))
			next_sentence = dict.get(sentences[l])[0][0]
			next_sentence = next_sentence.split(" ")
			next_sentence.insert(3,str(n))
			next_sentence.insert(7,object2)
			sentence1 = " ".join(split_sentence[0:3])
			block.text(sentence1+" "+split_sentence[3])
			block.text(" "+split_sentence[4],color=GREEN_TEXT_COLOR)
			sentence2 = " ".join(split_sentence[5:])
			block.text(" "+sentence2)	
			sentence3 = " ".join(next_sentence[0:2])
			block.text(". "+sentence3+" "+next_sentence[2])
			block.text(" "+next_sentence[3],color=GREEN_TEXT_COLOR)
			sentence4 = " ".join(next_sentence[4:])
			block.text(" "+sentence4)		
			block.text(", how many "+p.plural(object2)+ " are in each "+ object1+"?\n")	
		elif l==0:
			object1 = random.choice(dict.get(sentences[l])[0])
			object2 = random.choice(dict.get(sentences[l])[1])
			person1 = random.choice(eval(boy_or_girl[j]))
			person1_gender = his_or_her[j]
			split_sentence = sentences[l].split(" ")
			split_sentence.insert(2,str(m))
			split_sentence.insert(3," "+p.plural(object2))
			split_sentence.insert(6,str(n))
			split_sentence.insert(7," "+p.plural(object1))
			block.text(person1+" "+split_sentence[0]+" "+split_sentence[1])
			block.text(" "+split_sentence[2],color=GREEN_TEXT_COLOR)
			sentence1 = split_sentence[3]+" "+split_sentence[4]
			block.text(sentence1)
			block.text(" "+split_sentence[5],color=GREEN_TEXT_COLOR)
			sentence2 = " ".join(split_sentence[6:])
			block.text(sentence2)
			block.text(". How many "+p.plural(object2)+ " are there in each "+object1 +"?\n")
		elif l==3:
			person1 = random.choice(eval(boy_or_girl[j]))
			person1_gender = his_or_her[j]
			split_sentence = special_q.split(" ")
			split_sentence.insert(1,str(m))
			split_sentence.insert(4,str(n))
			block.text(person1+" "+split_sentence[0])
			block.text(" "+split_sentence[1]+" ",color=GREEN_TEXT_COLOR)
			sentence1 = split_sentence[2]+" "+split_sentence[3]
			block.text(sentence1)
			block.text(" "+split_sentence[4]+" ",color=GREEN_TEXT_COLOR)
			sentence2 = " ".join(split_sentence[5:])
			block.text(sentence2)
			block.text("How many pages can "+person1+ " read in one hour ?\n")
		else :
			object1 = random.choice(dict.get(sentences[l]))
			person1 = random.choice(eval(boy_or_girl[j]))
			person1_gender = his_or_her[j]
			split_sentence = sentences[l].split(" ")
			split_sentence.insert(1,str(m)+"$")
			#split_sentence.insert(3," "+p.plural(object2))
			split_sentence.insert(4,str(n))
			split_sentence.insert(5," "+p.plural(object1))
			block.text(person1+" "+split_sentence[0]+" ")
			block.text(" "+split_sentence[1]+" ",color=GREEN_TEXT_COLOR)
			sentence1 = split_sentence[2]+" "+split_sentence[3]
			block.text(sentence1)
			block.text(" "+split_sentence[4],color=GREEN_TEXT_COLOR)
			sentence2 = " ".join(split_sentence[5:])
			block.text(sentence2)
			block.text(". How much money did each "+object1+ " cost?\n")
											
		builder.block(block,center = True)
								
		data_list, correct_list = [], []

		correct_choice = random.randrange(0,4)
		
		checkbox_data_1 = builder.Block()
		checkbox_data_1.text(str(m/n))
		#print(m+n)
		r.remove(m/n)

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
		print z
		builder.save("./output/G3_007", "G3_007-"+str(z))
		#print(person1+" "+sentence1+". "+person2+" "+split_sentence[0]+" "+str(n)+" "+p.plural(object_of_the_question)+". How many "+p.plural(object_of_the_question)+ " did they "+ verbs[l]+" all together?")


if __name__ == '__main__':
	main()
