''' Profanity/Word Checker App

This script should look for words regardless of the format of the string.
It may fall over at some point, all depends on how many special characters the datasets
actually has.

Regardless, it is just a matter of writing a number of replace() lines and have it fixed.

Please remember to change the filepath to the csv file with the dataset

Change the column names and of course change the output csv file filepath and name

Currently it is using a glob.glob function to get all the csv files that the user would like
to test for specific words.

In order to have a more sustainable code for this particular project, I suggest to add a number
of user input options.

This code will also be used in the Comment_App to help users find the specific words and perhaps
create a sentiment analysis based on the words found.


'''

try:

	import time
	import glob

	import_time = time.time()

	import pandas as pd
	import numpy as np

	import re
	

	print(f'Import needed {time.time() - import_time}s to run')

	function_start = time.time()

	file_list = glob.glob(r'data\*.csv')

	bad_text = pd.read_csv('bad_words_corrected2.csv')

	bad_words_list = bad_text['bad_words'].tolist()

	bad_words = [bad_words_list[i:i + 1] for i in range(0, len(bad_words_list), 1)]

	text_column = input('Please enter the name of the column where the text is: ')

	for csv in file_list:

		csv_text = pd.read_csv(csv, encoding='ISO-8859-1')

		# Split the bad_words_list into one-sized chunks of smaller lists

		'''

			Numpy in1d checks if an element in a 1-dimensional array is present in another array

			max - return a max for a given value

			asarray - I expect it to change the row in crm_text to an array and going word after word

			lambda if of course a inline function which is applied to each row in csv'text']

		'''
		try:

			csv_text['text_list'] = csv_text[text_column].apply(lambda x: x.replace(',','')\
																	  .replace('.','')\
																	  .split())

			list_actual_word = []
			''' 

				Run two loops over the list of bad words and each row which is a list of each individual word inside of that comment from csv

				If found, create a list and append that list to the list_actual_word list

				Then remove all the duplicates by creating a set out of that list which is being appended to list_actual_word

				Out of that set create it back to a list

			'''

			for row in csv_text['text_list']:

				profanit_word = []

				for word in bad_words:

					for i in row:

						if word[0].lower() == i.lower():

							profanit_word.append(word[0])

						else:

							profanit_word.append('no profanity found')

				list_actual_word.append(list(set(profanit_word)))


			'''

				The newly created list, add it as a column and remove all the duplicates at the same time

				If there is no profanity, just leave it as an empty list

				If there is a profanity, leave it as a list with the bad words inside of that text

			'''

			csv_output_name = re.sub(r'[\W]', '', csv)

			csv_output_name = csv_output_name.replace('data', '')

			csv_output_name = csv_output_name.replace('csv', '')

			csv_text['profanity_check'] = list_actual_word

			csv_text['profanity_check'] = csv_text['profanity_check'].apply(lambda row: [i for i in row if i != 'no profanity found'])

			csv_text = crm_text.drop(columns=['text_list'])

			crm_text.to_csv(csv_output_name + '.csv', index=False)

			print(f'It took {time.time() - function_start}s to run the function')

		except KeyError:

			print(f'Column with the name {text_column} not found. please try again')

except KeyboardInterrupt:
	pass
