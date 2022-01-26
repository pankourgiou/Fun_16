from urllib.request import urlopen
page=urlopen("http://vitisport.de/")

#Fetches the code
#of the webpage
content = page.read()

print(content)
