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
	"qid": "G1_109",
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
	block_list=[]
	block = builder.Block()
	builder.text("Fill in the blanks:\n",center=True,  color=RED_TEXT_COLOR,font_size=LARGE_FONT_SIZE)
	builder.block(block,center=True)
	if minutes>6:
		builder.clock(hours+.5,minutes*5,size = HUGE_PICTURE_SIZE,center=True)
	else:
		builder.clock(hours,minutes*5,size = HUGE_PICTURE_SIZE,center=True)	
	minutes = str(minutes*5).zfill(2)
	hours = str(hours).zfill(2)
	#imageBlock = builder.Block()
	print hours,minutes
	block.textbox(hours[0],font_size=LARGE_FONT_SIZE)
	block.textbox(hours[1],font_size=LARGE_FONT_SIZE)
	block.text(" : ", center=False, color=RED_TEXT_COLOR)
	block.textbox(minutes[0],font_size=LARGE_FONT_SIZE)
	block.textbox(minutes[1],font_size=LARGE_FONT_SIZE)
	block_list.append(block)
	builder.blocks(block_list,center=True)
	counter = counter+1
	builder.save("./output/G2_109", "G2_109-"+str(counter))
	