from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


user_id=input('Enter User Id of your Fb Account :')  # Take user id and password as input from the user
password=input('Enter the password :')

print(user_id)
print(password)

cd='C:\\chromedriver.exe'


browser= webdriver.Chrome(cd)
browser.get('https://www.facebook.com/')


user_box = browser.find_element_by_id("email")       # For detecting the user id box
user_box.send_keys(user_id)                                               # Enter the user id in the box

password_box = browser.find_element_by_id("pass")    # For detecting the password box
password_box.send_keys(password)                                          # For detecting the password in the box

login_box = browser.find_element_by_id("u_0_b")      # For detecting the Login button
login_box.click()                                                         # To click on the login box

time.sleep(20)

pro=browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a')
pro.click()

time.sleep(4)
fr=browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div[2]/div[3]/div/div/div/div[1]/div/div/div/div[1]/h2/span/div/div[1]/span/a')
fr.click()

time.sleep(4)

while True:
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	time.sleep(0.1)
	browser.execute_script('window.scrollTo(0,0);')
	time.sleep(0.1)
	try:
		exit_control=browser.find_element_by_xpath("//*[contains(text(), 'More about you')]")
		break
	except:
		continue

ps=browser.page_source
soup=BeautifulSoup(ps,'html.parser')

flist=soup.find('div',{'class':'_3i9'})

friends=[]
for i in flist.findAll('a'):
	friends.append(i.text)



names_list=[]
for name in friends:
    if(name=='FriendFriends'):
        continue
    if('friends' in name):
        continue
    if(name==''):
        continue
    else:
        names_list.append(name)

print(names_list)
