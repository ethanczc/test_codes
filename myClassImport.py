from myClass import*

def main():
	me = Person('ethan','32','yo',height=150)
	me1 = Hobo() # no object attributes to define
	me.call()
	me.sayHeight()
	print(me1.name)
	sumation = Perform_Addition(1,2,3)
	print(sumation.result)

if __name__ == '__main__':
	main()