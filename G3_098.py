## Fill in the missing numerator or denominator......
import random
from hiperware.outliers.image import *
DEVELOPER_ID = "vaibhav@hiperware.com"
 
QUESTION_CATEGORY = {
            "grade": "Third",
            "subject": "Math",
            "skill_group": "Number Patterns",
            "skill": "Number Patterns"
            }

max_questions = 10

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
			if [j,k,m,n] in listOfCombinations:
				continue
			else:
				listOfCombinations.append([j,k,m,n])
				flag = 1
			
			#print listOfCombinations
		
		generatequestion(j,k,m,n,counter)
		counter+=1

def generatequestion(j,k,m,n,z): 
	builder = Builder(DEVELOPER_ID, QUESTION_CATEGORY)
	questions_text = ["Fill the gap:","Put the correct integer in the gap to make the fractions equal:","Fill in the missing value:"]
	builder.text(""+questions_text[random.randint(0,2)]+"\n", center=True,  color=RED_TEXT_COLOR,font_size=LARGE_FONT_SIZE)
	block_list=[]	   
	block = builder.Block()
	block.text(str(j)+"/"+str(k)+"=" , center=False, color=RED_TEXT_COLOR)
	builder.break_line()
	block.textbox(m,font_size=LARGE_FONT_SIZE)
	block.text("/"+str(n),center=False, color=RED_TEXT_COLOR)
	block_list.append(block)
	print z
	builder.blocks(block_list,center=True)
	builder.save("./output/G3_098", "G3_098- " + str(z))


if __name__ == '__main__':
	main()
