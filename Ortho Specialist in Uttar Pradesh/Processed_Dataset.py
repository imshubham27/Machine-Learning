from selenium import webdriver
import pandas as pd
import re
import numpy as np
import time

places_list=['Ghaziabad','Kanpur','Varanasi','Lucknow','Noida','Prayagraj','Agra','Bareilly']
l=[]
d={}
driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:13408246488232597399;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
print((add.text).find(places_list[0]))
d["Monday"]=np.sum(ppl[:12])
print(np.sum(ppl[:12]))
d["Tuesday"]=np.sum(ppl[12:23])
d["Wednesday"]=np.sum(ppl[23:37])
d["Thursday"]=np.sum(ppl[37:51])
d["Friday"]=np.sum(ppl[51:65])
d["Saturday"]=np.sum(ppl[65:78])
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:8892258373656540660;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:7])
d["Tuesday"]=np.sum(ppl[7:14])
d["Wednesday"]=np.sum(ppl[14:21])
d["Thursday"]=np.sum(ppl[21:28])
d["Friday"]=np.sum(ppl[28:35])
d["Saturday"]=np.sum(ppl[35:41])
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:7257948700513881673;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:9])
d["Tuesday"]=np.sum(ppl[9:18])
d["Wednesday"]=np.sum(ppl[18:27])
d["Thursday"]=np.sum(ppl[27:36])
d["Friday"]=np.sum(ppl[36:45])
d["Saturday"]=np.sum(ppl[45:54])
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:6525563808228574618;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:13])
d["Tuesday"]=np.sum(ppl[13:26])
d["Wednesday"]=np.sum(ppl[26:39])
d["Thursday"]=np.sum(ppl[39:52])
d["Friday"]=np.sum(ppl[52:65])
d["Saturday"]=np.sum(ppl[65:77])
d["Sunday"]=np.sum(ppl[77:82])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:8220351765094597413;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:7])
d["Tuesday"]=np.sum(ppl[7:14])
d["Wednesday"]=np.sum(ppl[14:21])
d["Thursday"]=np.sum(ppl[21:28])
d["Friday"]=np.sum(ppl[28:35])
d["Saturday"]=np.sum(ppl[35:42])
d["Sunday"]=np.sum(ppl[42:49])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:16252382225179329233;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:3])
d["Tuesday"]=np.sum(ppl[3:6])
d["Wednesday"]=np.sum(ppl[6:9])
d["Thursday"]=np.sum(ppl[9:12])
d["Friday"]=np.sum(ppl[12:15])
d["Saturday"]=np.sum(ppl[15:19])
d["Sunday"]=np.sum(ppl[19:23])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:3324089035634323458;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:14])
d["Tuesday"]=np.sum(ppl[14:29])
d["Wednesday"]=np.sum(ppl[29:45])
d["Thursday"]=np.sum(ppl[45:60])
d["Friday"]=np.sum(ppl[60:73])
d["Saturday"]=np.sum(ppl[73:87])
d["Sunday"]=np.sum(ppl[87:103])
l.append(d)


d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:3488011560021414240;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:7])
d["Tuesday"]=np.sum(ppl[7:14])
d["Wednesday"]=np.sum(ppl[14:21])
d["Thursday"]=np.sum(ppl[21:26])
d["Friday"]=np.sum(ppl[26:31])
d["Saturday"]=np.sum(ppl[31:36])
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:2531011108605098125;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:10])
d["Tuesday"]=np.sum(ppl[10:19])
d["Wednesday"]=np.sum(ppl[19:29])
d["Thursday"]=np.sum(ppl[29:37])
d["Friday"]=np.sum(ppl[37:45])
d["Saturday"]=0
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:14408144680204682107;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:6])
d["Tuesday"]=np.sum(ppl[6:12])
d["Wednesday"]=np.sum(ppl[12:18])
d["Thursday"]=np.sum(ppl[18:24])
d["Friday"]=np.sum(ppl[24:30])
d["Saturday"]=np.sum(ppl[30:32])
d["Sunday"]=np.sum(ppl[32:38])
l.append(d)


d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:2308886579239910683;mv:!1m2!1d30.246072599999998!2d83.3360771!2m2!1d25.0263754!2d76.9949341')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:5])
d["Tuesday"]=np.sum(ppl[5:13])
d["Wednesday"]=np.sum(ppl[13:21])
d["Thursday"]=np.sum(ppl[21:29])
d["Friday"]=np.sum(ppl[29:37])
d["Saturday"]=np.sum(ppl[37:42])
d["Sunday"]=np.sum(ppl[42:47])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=1zu6XP-PKM-QwgPakIZ4&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...0.0.0.51160.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.7ckubR7pdHs#rlfi=hd:;si:5317694778498507992;mv:!1m2!1d29.040361599999997!2d83.31609259999999!2m2!1d25.091983799999998!2d76.97544429999999;start:20')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:13])
d["Tuesday"]=np.sum(ppl[13:29])
d["Wednesday"]=np.sum(ppl[29:45])
d["Thursday"]=np.sum(ppl[45:51])
d["Friday"]=np.sum(ppl[51:73])
d["Saturday"]=np.sum(ppl[73:94])
d["Sunday"]=np.sum(ppl[94:118])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:256443137894461394;mv:!1m2!1d29.2018913!2d83.32353239999999!2m2!1d25.082840599999997!2d76.9750232;start:20')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:7])
d["Tuesday"]=np.sum(ppl[7:14])
d["Wednesday"]=np.sum(ppl[14:21])
d["Thursday"]=np.sum(ppl[21:28])
d["Friday"]=np.sum(ppl[28:35])
d["Saturday"]=np.sum(ppl[35:42])
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:12079158429058948304;mv:!1m2!1d29.2018913!2d83.32353239999999!2m2!1d25.082840599999997!2d76.9750232;start:20')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:12])
d["Tuesday"]=np.sum(ppl[12:24])
d["Wednesday"]=np.sum(ppl[24:36])
d["Thursday"]=np.sum(ppl[36:48])
d["Friday"]=np.sum(ppl[48:60])
d["Saturday"]=np.sum(ppl[60:72])
d["Sunday"]=np.sum(ppl[72:84])
l.append(d)


d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:12634343961495901149;mv:!1m2!1d29.2018913!2d83.32353239999999!2m2!1d25.082840599999997!2d76.9750232;start:20')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:7])
d["Tuesday"]=np.sum(ppl[7:14])
d["Wednesday"]=np.sum(ppl[14:21])
d["Thursday"]=0
d["Friday"]=np.sum(ppl[21:28])
d["Saturday"]=0
d["Sunday"]=0
l.append(d)


d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:12360641349145647060;mv:!1m2!1d29.2018913!2d83.32353239999999!2m2!1d25.082840599999997!2d76.9750232;start:20')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:23])
d["Tuesday"]=np.sum(ppl[23:47])
d["Wednesday"]=np.sum(ppl[47:71])
d["Thursday"]=np.sum(ppl[71:95])
d["Friday"]=np.sum(ppl[95:118])
d["Saturday"]=np.sum(ppl[118:142])
d["Sunday"]=np.sum(ppl[142:175])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:3600836356389040479,l,CkBvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzIHRvIHRoaXMgcGxhY2UuSNaKwr_ogICACFpBCj9vcnRobyBzcGVjaWFsaXN0IGluIHV0dGFyIHByYWRlc2ggYmFzZWQgb24gdmlzaXRzIHRvIHRoaXMgcGxhY2ViCwm4P_p1Px9-ARAC;mv:!1m2!1d29.2018913!2d83.32353239999999!2m2!1d25.082840599999997!2d76.9750232;start:20')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:12])
d["Tuesday"]=np.sum(ppl[12:24])
d["Wednesday"]=np.sum(ppl[24:36])
d["Thursday"]=np.sum(ppl[36:48])
d["Friday"]=np.sum(ppl[48:60])
d["Saturday"]=np.sum(ppl[60:72])
d["Sunday"]=np.sum(ppl[72:77])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&ei=X6i5XLqSC8vyvgTQ97bQBg&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits+to+this+place.&gs_l=psy-ab.12...175077.175077.0.176536.1.1.0.0.0.0.467.467.4-1.1.0....0...1c.1.64.psy-ab..0.0.0....0.wqEhdg0skFQ#rlfi=hd:;si:90251809702661162;mv:!1m2!1d29.2018913!2d83.32353239999999!2m2!1d25.082840599999997!2d76.9750232;start:20')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
for i in places_list:
    if i in add.text:
        break
d["Address"]=i
d["Monday"]=np.sum(ppl[:12])
d["Tuesday"]=np.sum(ppl[12:24])
d["Wednesday"]=np.sum(ppl[24:36])
d["Thursday"]=0
d["Friday"]=np.sum(ppl[48:60])
d["Saturday"]=np.sum(ppl[60:72])
d["Sunday"]=np.sum(ppl[72:77])
l.append(d)


df=pd.DataFrame(l)
print(df)
df.to_csv("Processed_Dataset.csv")