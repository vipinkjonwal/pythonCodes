def pigLatinEncryption(string):
	'''
	Objective		: To encrypt a given word into Pig Latin word.
	Input Parameters	: 
		    string      : String entered by user to convert into Pig Latin form.
	Return Values		: pigLatinWord
	'''
	#Approach		: Use string methods and concatenation to convert the given word into Pig Latin form.

	ayString = 'ay'
	tempCharacter = string[0]
	pigLatinWord = string[1:]+tempCharacter+ayString
	return pigLatinWord

def pigLatinDecryption(string):
	'''
	Objective		: To decrypt a given Pig Latin form word into original word.
	Input Parameters	: 
		    string      : Pig Latin form string.
	Return Values		: decryptedWord
	'''
	#Approach		: Use string methods and concatenation to convert the given Pig Latin form into original word.

	tempCharacter=string[-3]
	decryptedWord=tempCharacter+string[:len(string)-3]
	return decryptedWord
	
def main():
	'''
	Objective		: To encrypt and decrypt a given word into Pig Latin word and vice versa respectively.
	Input Parameters	: None.
	Return Values		: None.
	'''
	#Approach		: Invoke pigLatinEncryption and pigLatinDecryption functions.


	string=input("Input a word: ")
	print('Encrypted word is: ',pigLatinEncryption(string),sep="")
	print('Decrypted word is: ',pigLatinDecryption(pigLatinEncryption(string)),sep="")


if __name__ == '__main__':
	main()
