import requests

seq = range(1, 20)

for i in seq:
	file_name = str(i) + '.jpg'
	url = 'https://www.viewpoint.ca/property/cutimagel/202003395/1/' + '?&sd=cutsheet&cch=9b70e150'

	myfile = requests.get(url)
	open('./' + file_name, 'wb').write(myfile.content)