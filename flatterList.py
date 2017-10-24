def flatterList(givenList,flatList=[],index=0):
	'''
	Objective			: To flatten a givenList having elements as integers and lists i.e, nested lists.
	Input Parameters		: 
			givenList	: Given list of lists, multiple nesting, which needs to be flatten.
			flatterList	: Default - Blank List, a new flatten list.
			index		: Default - 0, for iterations.
	Return value			: flatList, i.e, flatten list.
	'''
	#Approach			: Checking the type fo element in main list whether it is integer or list.
	#					  If it is an integer, it is appended in flatList else flatterList is called recursively on sublist.

	if len(givenList)==index:
		return flatList
	elif type(givenList[index])==int:
		flatList.append(givenList[index])
		index=index+1
		return flatterList(givenList,flatList,index)
	elif type(givenList[index])==list:
		return flatterList(givenList[index],flatList)

def main():
	'''
	Objective			: To flatten a givenList having elements as integers and lists i.e, nested lists.
	Input Parameters		: None.
	Return value			: None.
	'''
	#Approach			: Invoke flatterList function.

	givenList=[10,20,[30,40,[50,60]],70,[80,90],100]
	print(flatterList(givenList))

if __name__ == '__main__':
	main()
