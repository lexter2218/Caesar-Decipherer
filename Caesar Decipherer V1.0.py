from os import system
		
def decipher(given, given_gaps):
	new_sentence = ""
	for char in given:
		if ord(char.upper()) in range(65,91):
			if char.upper() == char:
				first = 65
			elif char.lower() == char:
				first = 97

			new_char = first + ((ord(char) - first + given_gaps) % 26)
		else:
			new_char = ord(char)

		new_sentence += chr(new_char)

	return new_sentence

if __name__ == '__main__':
	sentence = ""
	list_sentences = []
	while True:
		if sentence == "":
			print("Welcome to Caesar Decipherer\n")
			sentence_action = input("Choose an action:\n1 - One line\n2 - Multiple Lines\n\n>> ")

			system("cls")
			print("What do you want to translate?")
			if int(sentence_action) == 1:
				list_sentences.append(input("\n>> "))
			elif int(sentence_action) == 2:
				while True:
					sentence = input("\n>> ")
					if sentence != "":
						list_sentences.append(sentence)
					else:
						break

		action = input("\nChoose an action:\n1 - Brute Force\n2 - Enter a key number\n\n>> ")
		if int(action) == 1:
			x, y, z = 1, 26, "Brute Force"
		elif int(action) == 2:
			x = y = int(input("\nKey Number: "))
			z = "Key = " + str(x)

		system("cls")
		print("Original Sentence/Word:\n")
		for sentence in list_sentences:
			print(sentence)
		print("\n\n" + z, "\n")
		while x <= y:
			for sentence in list_sentences:
				print("(" + str(x) + ")", decipher(sentence, x))
			print("\n")
			x += 1

		action = input("\nDo you want to change the sentence? (Y/N)\n\n>> ")
		if action.upper() == "Y":
			sentence = ""
			system("cls")