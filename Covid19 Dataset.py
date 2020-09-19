### Covid19 Dataset Creator

from selenium import webdriver
import time
import pandas as pd
import os

browser = webdriver.Chrome("C:\\chromedriver.exe")

browser.get("https://www.worldometers.info/coronavirus/")
time.sleep(15)

df = pd.DataFrame(columns=['Rank', 'Country', 'Total Cases', 'New Cases', 'Deaths', 'New Deaths', 'Recovered', 'Active Cases', 'Critical'])
print(df)

for i in browser.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody/tr'): # tr for each of country
    td_list=i.find_elements_by_tag_name('td') # tag name retrieve each piece of info for a country
    row=[]
    for td in td_list:
        row.append(td.text) # creating row ie each country data
    data = {}
    for j in range(len(df.columns)):
        data[df.columns[j]] = row[j]
    df = df.append(data, ignore_index=True)

df = df.iloc[1:]
print(df)

base_path = 'D:\\CovidDataset'
path = os.path.join(base_path,'Covid_Dataset_.csv')
df.to_csv(path)
print("The dataset has been at the location: " + path)
browser.quit()
