####################################################################
####################################################################
####################################################################
####################################################################
###
### 
### Michael Chon
###
###
####################################################################
####################################################################
####################################################################
####################################################################
###
### Coding Challenge
###
### writing course descriptions in a csv file
### using REST API
###
### 



import requests
import json
from bs4 import BeautifulSoup
import csv



if __name__ == "__main__":


	d = open('1234.json', 'r')
	data = json.load(d)
	d.close()

	with open("udemy.csv", 'a') as f:

		#Wrote the header once and toggle comment

		header = f.write('id' + ',' + 'title' + ',' + 'url' + ',' + 'is_paid' + ',' +
			'price' + ',' + 'professor' + ',' + 'description' + ',' + 'num_subscribers' + "\n")	
		

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


####################################################################
### getting description, number of subscribers 
###


			link = 'https://www.udemy.com/api-2.0/courses/' + str(iden) +'?fields[course]=description,num_subscribers'
			response = requests.get(link).content.decode()
			another_data = json.loads(response)


####################################################################
### using BeautifulSoup to parse the description 
###


			before_description = another_data['description']
			soup = BeautifulSoup(before_description,'html.parser')
			description = soup.find_all('p')[0].get_text()
			
			if description:
				description = description.rstrip().replace(',', '')
				description = description.rstrip().replace('\n', '')
			else:
				description = ' '


####################################################################
### writing the rest of attributes in a csv file
###


			num_subscribers = another_data['num_subscribers']
			num_subscribers = str(num_subscribers)

			f.write(iden + ',' + title + ',' + url + ',' + is_paid + ',' + price + ',' + professor + ',' + description + ',' + 
				num_subscribers + "\n")

			










