## Fill in the missing numerator or denominator......
import random
from hiperware.outliers.image import *
DEVELOPER_ID = "vaibhav@hiperware.com"
 
QUESTION_CATEGORY = {
            "grade": "Third",
            "subject": "Math",
            "skill_group": "Fractions",
            "skill": "Comparing Fractions: Part2"
            }

max_questions = 400

listOfCombinations = []

def main():
	counter = 1
	for i in range(max_questions):
		flag = 0
		while flag == 0:
			x = random.randint(1,10)	
			j = random.randint(1,20)
			k = random.randint(1,20)
			while j*x>20 or k*x>20:
				x = random.randint(1,10)	
				j = random.randint(1,20)
				k = random.randint(1,20)
			m = j*x
			n = k*x;
			j,n = random.sample([j,n],2)
		        k,m = random.sample([k,m],2)
			if [j,k,m,n] in listOfCombinations:
				continue
			elif j==m or k==n:
				continue
			else:
				listOfCombinations.append([j,k,m,n])
				flag = 1
			
			#print listOfCombinations
		
		generatequestion(j,k,m,n,counter)
		counter+=1

def generatequestion(j,k,m,n,z): 
	builder = Builder(DEVELOPER_ID, QUESTION_CATEGORY)
	questions_text = ["Fill the blank:","Fill in a number which completes the fraction:","Complete the fraction:"]
	builder.text(""+questions_text[random.randint(0,2)]+"\n", center=True,  color=RED_TEXT_COLOR,font_size=LARGE_FONT_SIZE)
	builder.break_line()
	block_list=[]	   
	block = builder.Block()
	v = random.randint(0,3)
	if v==0:
		block.textbox(j,font_size=LARGE_FONT_SIZE)
		block.text("/", center=False, color=RED_TEXT_COLOR)
		block.text(str(k), center=False, color=GREEN_TEXT_COLOR)
		block.text(" = ", center=False, color=RED_TEXT_COLOR)
		builder.break_line()
		block.text(str(m),center=False, color=GREEN_TEXT_COLOR)
		block.text("/",center=False, color=RED_TEXT_COLOR)
		block.text(str(n),center=False, color =GREEN_TEXT_COLOR)
	elif v==1:
		block.text(str(j), center=False, color=GREEN_TEXT_COLOR)
		block.text("/", center=False, color=RED_TEXT_COLOR)
		block.textbox(k, font_size=LARGE_FONT_SIZE)
		block.text(" = ", center=False, color=RED_TEXT_COLOR)
		builder.break_line()
		block.text(str(m),center=False, color=GREEN_TEXT_COLOR)
		block.text("/",center=False, color=RED_TEXT_COLOR)
		block.text(str(n),center=False, color =GREEN_TEXT_COLOR)
	elif v==2:
		block.text(str(j), center=False, color=GREEN_TEXT_COLOR)
		block.text("/", center=False, color=RED_TEXT_COLOR)
		block.text(str(k), center=False, color=GREEN_TEXT_COLOR)
		block.text(" = ", center=False, color=RED_TEXT_COLOR)
		builder.break_line()
		block.textbox(m,font_size=LARGE_FONT_SIZE)
		block.text("/",center=False, color=RED_TEXT_COLOR)
		block.text(str(n),center=False, color =GREEN_TEXT_COLOR)
	else:
		block.text(str(j), center=False, color=GREEN_TEXT_COLOR)
		block.text("/", center=False, color=RED_TEXT_COLOR)
		block.text(str(k), center=False, color=GREEN_TEXT_COLOR)
		block.text(" = ", center=False, color=RED_TEXT_COLOR)
		builder.break_line()
		block.text(str(m),center=False, color=GREEN_TEXT_COLOR)
		block.text("/",center=False, color=RED_TEXT_COLOR)
		block.textbox(n,font_size=LARGE_FONT_SIZE)
	block_list.append(block)
	print z
	builder.blocks(block_list,center=True)
	builder.save("./output/G3_098", "G3_098-" + str(z))


if __name__ == '__main__':
	main()
