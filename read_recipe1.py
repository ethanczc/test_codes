from tkinter import*

'''
User creates a recipe txt file with parameters and values in the same location as the source code.
The user can then use the source code to load the recipe file with the all the desired parameters.
There is no need to edit the source code, and there is no need to respecify all parameters when
the user needs to close the application and re-open again.
'''

root = Tk()
root.title('read recipe program')
root.geometry('')

file_Label = Label(root,text='File').grid(row=0,column=0)
file_Entry=Entry(root,)
file_Entry.grid(row=0,column=1)

recipeContent = ''
def GetRecipe():
	global recipeContent
	recipeName = file_Entry.get()
	try:
		file = open(recipeName,'r')
	except:
		recipeFileName_Display.config(text='recipe not found')
	else:
		recipeContent = file.readlines()
		recipeFileName_Display.config(text=recipeName)
		Read_Recipe()

recipeLoad_Button = Button(root,text='Load recipe',command=GetRecipe)
recipeLoad_Button.grid(row=1,column=0,columnspan=2)

recipeFileLoaded_Label = Label(root,text='Recipe Loaded:').grid(row=2,column=0)

recipeFileName_Display = Label(root,text='none')
recipeFileName_Display.grid(row=2,column=1)

recipeName_Label = Label(root,text='Recipe name:').grid(row=3,column=0)
recipeName_Display = Label(root,text='')
recipeName_Display.grid(row=3,column=1)

def Read_Recipe():
	global recipeContent
	for line in range(0,len(recipeContent)):
		thisLine = recipeContent[line][:-1]
		thisLine = thisLine.split(' ')
		parameter = thisLine[0]
		value = thisLine[1]
		if parameter == 'recipeName':
			GetRecipeName(value)
		if parameter == 'timeStart':
			GetTimeStart(value)
		if parameter == 'pwmValue':
			GetPwmValue(value)
		if parameter == 'EC':
			GetECValue(value)
		if parameter == 'waterTankVolume':
			GetWaterTankVolume(value)

def GetRecipeName(name):
	recipeName = name
	recipeName_Display.config(text=recipeName)
	print (recipeName)

pwm = 200
def GetPwmValue(pwmValue):
	global pwm
	pwm = pwmValue
	print (pwm)

timeStart = []
def GetTimeStart(time):
	global timeStart
	time_List = time.split(',')
	timeStart = time_List
	print (timeStart)

ec = 0.1
def GetECValue(EC):
	global ec
	ec = EC
	print (ec)

waterTankVolume = 1
def GetWaterTankVolume(volume):
	global waterTankVolume
	waterTankVolume = volume
	print(waterTankVolume)

def main():
	root.mainloop()

if __name__ == '__main__':
	main()
