import os #screen clearing

#set up values for error checking
num_entities = False

os.system('clear')
#print out version, name, etc
print("""VHDL2Pyboard v1.0\nDesigned to run on Pyboard 1.1\n\nNOTE: This \
program is intended to run with a particular VHDL testbench style.""")
#entity specifications
print("""Entities should be of this format:\nentity x of y is\n\t\
port map(ports;\n\tports;\n\tports);\nend entity;\nMultiple ports may be \
declared in each line as long as they are of the same type. The user is \
prompted for pin mappings relative to the testbench port mappings.""")
#architecture specifications
print("""\nArchitectures should use signal assignments and wait for \
statements to provide \nstimulus to pins. Assert statements should be used \
to check signals. The unit \nunder test (UUT) is ignored in the python file \
the input and output pins are \naddressed directly.""")

#open vhdl file to translate
rd_filename = input('\nFile to translate: ')
rd = open(rd_filename, 'r')

#create python file
wr_filename = input('File to write to: ')
wr = open(wr_filename, 'w')

#read through entire file
for line in rd:
	line = readline()

	#ignore library and use statements
	stripline = line.strip()
	if stripline.startswith('library') or line.startswith('use'):
		continue
	
	#prompt user for mappings when entity is reached
	elif stripline.startswith('entity'):
		if num_entities > 1:
			print('error: multiple entities found within file')
			exit()
		else:
			line = readline()

#close files
close(rd)
close(wr)
