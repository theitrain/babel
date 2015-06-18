import codecs
import sys

# Check for arguments
commandArgs = len(sys.argv)

if commandArgs < 2:
	print "Expected 1 argument, received "
	print (commandArgs - 1)
	sys.exit()
else:
	readName = sys.argv[1] + ".xlsx"
	fileName = "./output" + sys.argv[1] + ".amp"

	from xlrd import open_workbook
	wb = open_workbook(readName)

	target = codecs.open(fileName, 'w', 'utf8')

	sheet = wb.sheet_by_index(0)

	# open ampscript tags
	target.write( '\n%%[\n')

	for col in range(sheet.ncols):

		# We want to ignore the first (0) column
		if col > 0:

			# Get the language code
			lang = sheet.cell(0,col).value

			# For the first row, set the language
			if col == 1:
				target.write( 'IF @localeLang == "englishUS" THEN\n')
			elif lang == "es_AR":
				target.write( 'ELSEIF @localeLang == "es" AND @locale == "es_AR" THEN\n')
			elif lang == "es_ES":
				target.write( 'ELSEIF @localeLang == "es" AND @locale == "es" THEN\n')
			elif lang == "es_MX" or lang == "es_LX":
				target.write( 'ELSEIF @localeLang == "es" THEN\n')

			else:
				target.write( 'ELSEIF @localeLang == "' + sheet.cell(0,col).value + '" THEN\n')


			for row in range(sheet.nrows):

				# All other rows, set the value of the cell to the corresponding value from the first (0) column
				if row > 0:
		 			# Assign it to an ampscript variable
		 			variableName = sheet.cell(row, 0).value

		 			# Escape any quotes in the value ("Traveler's Choice" causes all types of issues)
		 			variableValue = sheet.cell(row,col).value.replace('\"', '"""')

			 		target.write( '\t Set @' + variableName + ' = "' + variableValue.encode('utf8').decode('utf8') +'"\n')


 	# ELSE statement (default to English - first column)
	target.write( 'ELSE\n')

	for row in range(sheet.nrows):

		if row > 0:
			# All other rows, set the value of the cell to the corresponding value from the first (0) column
		 	# Assign it to an ampscript variable
		 	variableName = sheet.cell(row, 0).value

		 	# Escape any quotes in the value ("Traveler's Choice" causes all types of issues)
		 	variableValue = sheet.cell(row,1).value.replace('\"', '"""')		

			target.write( '\t Set @' + variableName + ' = "' + variableValue +'"\n')

	target.write( 'ENDIF')

	# close ampscript tags
	target.write( '\n]%%')