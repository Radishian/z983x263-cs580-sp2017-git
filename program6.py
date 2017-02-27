# program6.py

# Description: This program reads zip codes from a file and produces
#	bar codes for each zip code. The zip codes come from a file
#	specified by the user and the output file comes from a file specified
#	by the user. This program also can read bar codes and convert
#	them back into readable zip codes. The program prompts the
#	user for whether he or she wishes to encode zip codes or
#	decode bar codes.

# Author: Caleb Rettig
# StudentID: z983x263

def main():
	# determine whether user would like to encode
	#	or decode zip codes
	valid_input = False

	while not valid_input:
		encode = input("Would you like to encode zip codes? [Y/N]: ")

		if encode == "Y" or encode == "y":
			valid_input = True
			valid_infile = False

			while not valid_infile:
				infile_name = input("What is the name of the zip code file?: ")

				try:
					infile = open(infile_name, "r")
					valid_infile = True
				except IOError:
					print("Sorry, that file cannot be found.")

			outfile_name = input("What is the name of the output bar code file?: ")
			outfile = open(outfile_name, "w")

			encode_zip(infile, outfile)

		elif encode == "N" or encode == "n":
			decode = input("Would you like to decode bar codes? [Y/N]: ")

			if decode == "Y" or decode == "y":
				valid_input = True
				valid_infile = False

				while not valid_infile:
					infile_name = input("What is the name of the bar code file?: ")

					try:
						infile = open(infile_name, "r")
						valid_infile = True
					except IOError:
						print("Sorry, that file cannot be found.")

				outfile_name = input("What is the name of the output zip code file?: ")
				outfile = open(outfile_name, "w")

				decode_bar(infile, outfile)

			elif decode == "N" or decode == "n":
				valid_input = True
				print("Then this program does not provide the functionality you desire.")
				exit()

			else:
				print("Sorry, that is not valid input. I do not understand. Try again.")
		else:
			print("Sorry, that is not valid input. I do not understand. Try again.")

def encode_zip(infile, outfile):
	key = ["!!...", "...!!", "..!.!", "..!!.", ".!..!", ".!.!.", ".!!..", "!...!", "!..!.", "!.!.."]

	for line in infile:
		total = 0
		checksum = 0
		lineout = ["!"]
		for i in line:
			if ord(i) <= ord("9") and ord(i) >= ord("0"):
				index = ord(i) - ord("0")
				total = total + index
				lineout.append(key[index])
		while (checksum + total) % 10 > 0:
			checksum = checksum + 1
		lineout.append(key[checksum])
		lineout.append("!\n")
		lineout = ''.join(lineout)
		outfile.write(lineout)

def decode_bar(infile, outfile):
	key = ["!!...", "...!!", "..!.!", "..!!.", ".!..!", ".!.!.", ".!!..", "!...!", "!..!.", "!.!.."]

	for line in infile:
		lineout = []
		raw_output = []
		line = line[1:-2]

		count = range((len(line) // 5) - 1)
		for i in count:
			sequence = line[5 * i:5 * i + 5]

			lineout.append(str(key.index(sequence)))
			raw_output.append(key.index(sequence))
			if i == 4 and len(count) > 5:
				lineout.append("-")
			elif i == 8 and len(count) > 9:
				lineout.append("+")


		total = 0
		for i in raw_output:
			total = total + i;

		if (total + key.index(line[-5:])) % 10 != 0:
			print("There was an error converting from the bar code to zip code")

		lineout.append("\n")
		lineout = ''.join(lineout)
		outfile.write(lineout)

main()
