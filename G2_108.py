import sys
import inflect
import random

#sys.path.insert(0,"/home/sagup/Desktop/hiperware_stuff/hiperware/")

#import the Rendering API package
from hiperware.outliers.image import *

# developer ID received from Hiperware
DEVELOPER_ID = "vaibhav@hiperware.com"

# question category (all the fields are required)
QUESTION_CATEGORY = {
    "grade": "Second",
    "subject": "Math",
    "skill_group": "Time",
    "skill": "Time",
	"qid": "G1_108",
	"skill_group_icon" : "G1.5",
	"skill_icon": "G1.5.1",
	"skill_group_weight": 5,
	"skill_weight": 10
}

counter=0
for ques in range(400):
	minutes = random.randint(1,12)
	hours = random.randint(1,12)
	range0fHours = range(1,13)
	range0fHours.remove(hours)
	range0fMinutes = range(0,13)
	range0fMinutes.remove(minutes)
	hours = int(str(hours).zfill(2))
	builder = Builder(DEVELOPER_ID, QUESTION_CATEGORY)
	text_block = builder.Block()
	text_block.text("What time does the clock show?\n")
	builder.block(text_block,center=True)

	#imageBlock = builder.Block()
	builder.clock(hours,minutes*5,size = HUGE_PICTURE_SIZE,center=True)
	#builder.block(imageBlock)
	data_list, correct_list = [], []

	correct_choice = random.randrange(0,4)
	checkbox_data_1 = builder.Block()
	checkbox_data_1.text(str(hours).zfill(2)+":"+str(minutes*5).zfill(2))
	#print(m+n)
	correct_list.append(correct_choice==0)
	checkbox_data_2 = builder.Block()
	choice2 = random.choice(range0fHours)
	choice2Minutes = random.choice(range0fMinutes)
	checkbox_data_2.text(str(choice2).zfill(2)+":"+str(choice2Minutes*5).zfill(2))
	range0fHours.remove(choice2)
	range0fMinutes.remove(choice2Minutes)

	correct_list.append(correct_choice==1) 

	checkbox_data_3 = builder.Block()
	choice3 = random.choice(range0fHours)
	choice3Minutes = random.choice(range0fMinutes)
	checkbox_data_3.text(str(choice3).zfill(2)+":"+str(choice3Minutes*5).zfill(2))
	range0fHours.remove(choice3)
	range0fMinutes.remove(choice3Minutes)
	
	correct_list.append(correct_choice==2)
	checkbox_data_4 = builder.Block()
	choice4 = random.choice(range0fHours)
	choice4Minutes = random.choice(range0fMinutes)
	checkbox_data_4.text(str(choice4).zfill(2)+":"+str(choice4Minutes*5).zfill(2))
	range0fHours.remove(choice4)
	
	range0fMinutes.remove(choice4Minutes)
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
	counter = counter+1
	builder.save("./output/G2_108", "G2_108-"+str(counter))
	