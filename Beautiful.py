from selenium import webdriver
import MySQLdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
db = MySQLdb.connect("localhost","root","","vtu" )
cursor = db.cursor()
driver = webdriver.Chrome(r'''C:\Users\ANURAG\Desktop\chromedriver''') 
a=int(input("Enter the last two digits of Starting USN:"))
b=int(input("Enter the last two digits of Ending Usn:"))
for i in range(a,b):
    target = '1sb15cs0'+str(i)
    print(target)
    driver.get("http://results.vtu.ac.in/cbcs_17/index.php")
    inp_xpath='/html/body/div/div/div/div[3]/div[2]/form/div/div[2]/div[1]/div/input'
    input_box = WebDriverWait(driver,600).until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    input_box.send_keys(target + Keys.ENTER)
    try:
        html=driver.page_source
    except Exception:
        alert=driver.switch_to_alert()
        alert.dismiss()
        continue
    soup=BeautifulSoup(html,"lxml")
    result=soup.find_all('table')
    store=result[1].find_all('td')
    iam=[]
    total=[]
    external=[]
    exampass=[]
    for x in range(2,48,6):
        iam.append(store[x].text)
    for x in range(3,48,6):
        external.append(store[x].text)
    for x in range(4,48,6):
        total.append(store[x].text)
    for x in range(5,48,6):
        exampass.append(store[x].text)
    sql = "INSERT INTO ia VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(target,iam[0],iam[1],iam[2],iam[3],iam[4],iam[5],iam[6],iam[7])
    cursor.execute(sql)
    db.commit()
    sql = "INSERT INTO em VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(target,external[0],external[1],external[2],external[3],external[4],external[5],external[6],external[7])
    cursor.execute(sql)
    db.commit()
    sql = "INSERT INTO tm VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(target,total[0],total[1],total[2],total[3],total[4],total[5],total[6],total[7])
    cursor.execute(sql)
    db.commit()
    sql = "INSERT INTO total VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(target,exampass[0],exampass[1],exampass[2],exampass[3],exampass[4],exampass[5],exampass[6],exampass[7])
    cursor.execute(sql)
    db.commit()
db.close()
