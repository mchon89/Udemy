# ----------------------------------------------
# fixed udemy.py 
# ----------------------------------------------


import requests
import json
from bs4 import BeautifulSoup
import csv


if __name__ == "__main__":

# ----------------------------------------------
# loading json file  
# ----------------------------------------------

	d = open('1234.json', 'r')
	data = json.load(d)
	d.close()

# ----------------------------------------------
# writing header and other attributes 
# ----------------------------------------------

	with open("udemy1.csv", 'a') as f:

		# header = f.write('id' + ',' + 'title' + ',' + 'url' + ',' + 'is_paid' + ',' +
		# 	'price' + ',' + 'professor' + ',' + 'description' + ',' + 'num_subscribers' + "\n")

		for i in range(len(data['results'])):

			iden = data['results'][i]['id']
			iden = str(iden)

			is_paid = data['results'][i]['is_paid']
			is_paid = str(is_paid)

			title = data['results'][i]['title']
			title = title.strip().replace(',', '')

			url = data['results'][i]['url']
			price = data['results'][i]['price']

			professor = data['results'][i]['visible_instructors'][0]['title']
			professor = professor.strip().replace(',', '')

# ----------------------------------------------
# getting description, number of subscribers 
# ----------------------------------------------

			link = 'https://www.udemy.com/api-2.0/courses/' + str(iden) +'?fields[course]=description,num_subscribers'
			response = requests.get(link).content.decode()
			another_data = json.loads(response)
			description = str(another_data['description'])
			description = description.rstrip().replace(',', '')
			description = description.rstrip().replace('\n', '')
			num_subscribers = str(another_data['num_subscribers'])

# ----------------------------------------------
# writing the rest of attributes in a csv file
# ----------------------------------------------

			f.write(iden + ',' + title + ',' + url + ',' + is_paid + ',' 
				+ price + ',' + professor + ',' + description + ',' + num_subscribers + "\n")

			










