from selenium import webdriver
import pandas as pd
import re
import numpy as np
import time

l=[]
d={}
driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.get('https://www.google.com/search?tbm=lcl&sxsrf=ACYBGNRyi7xSDXXvbwb8AOwSq6IeqEFuYg%3A1577286200358&ei=OHoDXvS4FfzUz7sP2fOHgAs&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&gs_l=psy-ab.3...115997.117662.0.118183.14.10.0.0.0.0.265.934.0j1j3.4.0....0...1c.1.64.psy-ab..14.0.0....0.me5XDTIKUfI#rlfi=hd:;si:6525563808228574618,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.193008799999998,82.1357799],[25.2469923,77.06354499999999]]')
time.sleep(3)
ppl=[]
item=driver.find_elements_by_css_selector('div.lubh-bar')
for i in item:
            ht=i.get_attribute('style')
            num_ht=re.sub('[^0-9]', '', ht)
            print(num_ht)
            ppl.append(num_ht)           
ppl=np.array(ppl).astype(np.float)

ortho=driver.find_element_by_class_name("SPZz6b")
d["Ortho-Specialist Name"]=(ortho.text)
ratings=driver.find_element_by_class_name("Ob2kfd").find_element_by_class_name("rtng")
d["Ratings"]=(ratings.text)
add=driver.find_element_by_class_name("LrzXr")
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:13])
d["Tuesday"]=np.sum(ppl[13:26])
d["Wednesday"]=np.sum(ppl[26:39])
d["Thursday"]=np.sum(ppl[39:52])
d["Friday"]=np.sum(ppl[52:65])
d["Saturday"]=np.sum(ppl[65:78])
d["Sunday"]=np.sum(ppl[78:81])
l.append(d)
print(l)

d={}
driver.get('https://www.google.com/search?tbm=lcl&sxsrf=ACYBGNRyi7xSDXXvbwb8AOwSq6IeqEFuYg%3A1577286200358&ei=OHoDXvS4FfzUz7sP2fOHgAs&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&gs_l=psy-ab.3...115997.117662.0.118183.14.10.0.0.0.0.265.934.0j1j3.4.0....0...1c.1.64.psy-ab..14.0.0....0.me5XDTIKUfI#rlfi=hd:;si:13408246488232597399,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.193008799999998,82.1357799],[25.2469923,77.06354499999999]]')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:12])
d["Tuesday"]=np.sum(ppl[12:24])
d["Wednesday"]=np.sum(ppl[24:36])
d["Thursday"]=np.sum(ppl[36:48])
d["Friday"]=np.sum(ppl[48:60])
d["Saturday"]=np.sum(ppl[60:72])
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&sxsrf=ACYBGNRyi7xSDXXvbwb8AOwSq6IeqEFuYg%3A1577286200358&ei=OHoDXvS4FfzUz7sP2fOHgAs&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&gs_l=psy-ab.3...115997.117662.0.118183.14.10.0.0.0.0.265.934.0j1j3.4.0....0...1c.1.64.psy-ab..14.0.0....0.me5XDTIKUfI#rlfi=hd:;si:16252382225179329233,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.193008799999998,82.1357799],[25.2469923,77.06354499999999]]')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:3])
d["Tuesday"]=np.sum(ppl[3:6])
d["Wednesday"]=np.sum(ppl[6:9])
d["Thursday"]=np.sum(ppl[9:12])
d["Friday"]=np.sum(ppl[12:15])
d["Saturday"]=np.sum(ppl[15:19])
d["Sunday"]=np.sum(ppl[19:23])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&sxsrf=ACYBGNRyi7xSDXXvbwb8AOwSq6IeqEFuYg%3A1577286200358&ei=OHoDXvS4FfzUz7sP2fOHgAs&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&gs_l=psy-ab.3...115997.117662.0.118183.14.10.0.0.0.0.265.934.0j1j3.4.0....0...1c.1.64.psy-ab..14.0.0....0.me5XDTIKUfI#rlfi=hd:;si:8220351765094597413,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.193008799999998,82.1357799],[25.2469923,77.06354499999999]]')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:8])
d["Tuesday"]=np.sum(ppl[8:16])
d["Wednesday"]=np.sum(ppl[16:24])
d["Thursday"]=np.sum(ppl[24:32])
d["Friday"]=np.sum(ppl[32:40])
d["Saturday"]=np.sum(ppl[40:47])
d["Sunday"]=np.sum(ppl[47:50])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&sxsrf=ACYBGNRyi7xSDXXvbwb8AOwSq6IeqEFuYg%3A1577286200358&ei=OHoDXvS4FfzUz7sP2fOHgAs&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&gs_l=psy-ab.3...115997.117662.0.118183.14.10.0.0.0.0.265.934.0j1j3.4.0....0...1c.1.64.psy-ab..14.0.0....0.me5XDTIKUfI#rlfi=hd:;si:200098603890527670,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.193008799999998,82.1357799],[25.2469923,77.06354499999999]]')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:8])
d["Tuesday"]=np.sum(ppl[8:16])
d["Wednesday"]=np.sum(ppl[16:24])
d["Thursday"]=np.sum(ppl[24:32])
d["Friday"]=np.sum(ppl[32:40])
d["Saturday"]=np.sum(ppl[40:48])
d["Sunday"]=np.sum(ppl[48:56])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&sxsrf=ACYBGNRyi7xSDXXvbwb8AOwSq6IeqEFuYg%3A1577286200358&ei=OHoDXvS4FfzUz7sP2fOHgAs&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&gs_l=psy-ab.3...115997.117662.0.118183.14.10.0.0.0.0.265.934.0j1j3.4.0....0...1c.1.64.psy-ab..14.0.0....0.me5XDTIKUfI#rlfi=hd:;si:9886610303229544371,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.193008799999998,82.1357799],[25.2469923,77.06354499999999]]')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:8])
d["Tuesday"]=np.sum(ppl[8:16])
d["Wednesday"]=np.sum(ppl[16:24])
d["Thursday"]=np.sum(ppl[24:32])
d["Friday"]=np.sum(ppl[32:40])
d["Saturday"]=np.sum(ppl[40:48])
d["Sunday"]=np.sum(ppl[48:54])
l.append(d)

d={}
driver.get('https://www.google.com/search?tbm=lcl&sxsrf=ACYBGNRyi7xSDXXvbwb8AOwSq6IeqEFuYg%3A1577286200358&ei=OHoDXvS4FfzUz7sP2fOHgAs&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&gs_l=psy-ab.3...115997.117662.0.118183.14.10.0.0.0.0.265.934.0j1j3.4.0....0...1c.1.64.psy-ab..14.0.0....0.me5XDTIKUfI#rlfi=hd:;si:6617879763029544111,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzSO2H7IPxqoCACFp-CjFvcnRobyBzcGVjaWFsaXN0IGluIHV0dGFyIHByYWRlc2ggYmFzZWQgb24gdmlzaXRzEAAQARACEAMQBBAFEAYQBxgAGAEYAxgEIjFvcnRobyBzcGVjaWFsaXN0IGluIHV0dGFyIHByYWRlc2ggYmFzZWQgb24gdmlzaXRz;mv:[[29.2034627,83.3362193],[25.085390999999998,76.9924222]];start:20')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:9])
d["Tuesday"]=np.sum(ppl[9:18])
d["Wednesday"]=np.sum(ppl[18:27])
d["Thursday"]=np.sum(ppl[27:36])
d["Friday"]=np.sum(ppl[36:45])
d["Saturday"]=np.sum(ppl[45:54])
d["Sunday"]=np.sum(ppl[54:63])
l.append(d)


d={}
driver.get('https://www.google.com/search?tbm=lcl&sxsrf=ACYBGNRyi7xSDXXvbwb8AOwSq6IeqEFuYg%3A1577286200358&ei=OHoDXvS4FfzUz7sP2fOHgAs&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&oq=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&gs_l=psy-ab.3...115997.117662.0.118183.14.10.0.0.0.0.265.934.0j1j3.4.0....0...1c.1.64.psy-ab..14.0.0....0.me5XDTIKUfI#rlfi=hd:;si:5317694778498507992,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzSKm9tobMq4CACFp-CjFvcnRobyBzcGVjaWFsaXN0IGluIHV0dGFyIHByYWRlc2ggYmFzZWQgb24gdmlzaXRzEAAQARACEAMQBBAFEAYQBxgAGAEYAxgEIjFvcnRobyBzcGVjaWFsaXN0IGluIHV0dGFyIHByYWRlc2ggYmFzZWQgb24gdmlzaXRz;mv:[[29.2034627,83.3362193],[25.085390999999998,76.9924222]];start:20')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:13])
d["Tuesday"]=np.sum(ppl[13:28])
d["Wednesday"]=np.sum(ppl[28:40])
d["Thursday"]=np.sum(ppl[40:54])
d["Friday"]=np.sum(ppl[54:67])
d["Saturday"]=np.sum(ppl[67:79])
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?sa=X&biw=1002&bih=722&sxsrf=ACYBGNSXHYUvO9l4PV7z-qF6OSAxFsfpIw:1577292384259&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&npsic=0&rflfq=1&rlha=0&rllag=28632801,77359922,2014&tbm=lcl&ved=2ahUKEwjR3pSCoNHmAhXrILcAHRJ4DzIQjGp6BAgKEE4&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:5006960691101431168,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.2034627,83.3362193],[25.085390999999998,76.9924222]];start:20')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:6])
d["Tuesday"]=np.sum(ppl[6:12])
d["Wednesday"]=np.sum(ppl[12:19])
d["Thursday"]=np.sum(ppl[19:25])
d["Friday"]=np.sum(ppl[25:31])
d["Saturday"]=np.sum(ppl[31:37])
d["Sunday"]=np.sum(ppl[37:43])
l.append(d)

d={}
driver.get('https://www.google.com/search?sa=X&biw=1002&bih=722&sxsrf=ACYBGNSXHYUvO9l4PV7z-qF6OSAxFsfpIw:1577292384259&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&npsic=0&rflfq=1&rlha=0&rllag=28632801,77359922,2014&tbm=lcl&ved=2ahUKEwjR3pSCoNHmAhXrILcAHRJ4DzIQjGp6BAgKEE4&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:14180435733779092589,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.2034627,83.3362193],[25.085390999999998,76.9924222]];start:20')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:5])
d["Tuesday"]=np.sum(ppl[5:10])
d["Wednesday"]=np.sum(ppl[10:15])
d["Thursday"]=np.sum(ppl[15:20])
d["Friday"]=np.sum(ppl[20:25])
d["Saturday"]=np.sum(ppl[25:30])
d["Sunday"]=0
l.append(d)


d={}
driver.get('https://www.google.com/search?sa=X&biw=1002&bih=722&sxsrf=ACYBGNSXHYUvO9l4PV7z-qF6OSAxFsfpIw:1577292384259&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&npsic=0&rflfq=1&rlha=0&rllag=28632801,77359922,2014&tbm=lcl&ved=2ahUKEwjR3pSCoNHmAhXrILcAHRJ4DzIQjGp6BAgKEE4&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:7348112883433184550,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.2034627,83.3362193],[25.085390999999998,76.9924222]];start:20')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:6])
d["Tuesday"]=np.sum(ppl[6:12])
d["Wednesday"]=np.sum(ppl[12:19])
d["Thursday"]=np.sum(ppl[19:25])
d["Friday"]=np.sum(ppl[25:31])
d["Saturday"]=np.sum(ppl[31:37])
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?sa=X&biw=1002&bih=722&sxsrf=ACYBGNSXHYUvO9l4PV7z-qF6OSAxFsfpIw:1577292384259&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&npsic=0&rflfq=1&rlha=0&rllag=28632801,77359922,2014&tbm=lcl&ved=2ahUKEwjR3pSCoNHmAhXrILcAHRJ4DzIQjGp6BAgKEE4&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:14408144680204682107,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.2034627,83.3362193],[25.085390999999998,76.9924222]];start:20')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:6])
d["Tuesday"]=np.sum(ppl[6:12])
d["Wednesday"]=np.sum(ppl[12:19])
d["Thursday"]=np.sum(ppl[19:25])
d["Friday"]=np.sum(ppl[25:31])
d["Saturday"]=np.sum(ppl[31:33])
d["Sunday"]=np.sum(ppl[33:39])
l.append(d)

d={}
driver.get('https://www.google.com/search?sa=X&biw=1002&bih=722&sxsrf=ACYBGNSXHYUvO9l4PV7z-qF6OSAxFsfpIw:1577292384259&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&npsic=0&rflfq=1&rlha=0&rllag=28632801,77359922,2014&tbm=lcl&ved=2ahUKEwjR3pSCoNHmAhXrILcAHRJ4DzIQjGp6BAgKEE4&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:16092805102936926721,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.2034627,83.3362193],[25.085390999999998,76.9924222]];start:20')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:6])
d["Tuesday"]=np.sum(ppl[6:12])
d["Wednesday"]=np.sum(ppl[12:19])
d["Thursday"]=np.sum(ppl[19:25])
d["Friday"]=np.sum(ppl[25:31])
d["Saturday"]=np.sum(ppl[31:37])
d["Sunday"]=0
l.append(d)

d={}
driver.get('https://www.google.com/search?sa=X&biw=1002&bih=722&sxsrf=ACYBGNSXHYUvO9l4PV7z-qF6OSAxFsfpIw:1577292384259&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&npsic=0&rflfq=1&rlha=0&rllag=28632801,77359922,2014&tbm=lcl&ved=2ahUKEwjR3pSCoNHmAhXrILcAHRJ4DzIQjGp6BAgKEE4&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:7257948700513881673,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.2034627,83.3362193],[25.085390999999998,76.9924222]];start:20')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:9])
d["Tuesday"]=np.sum(ppl[9:18])
d["Wednesday"]=np.sum(ppl[18:27])
d["Thursday"]=np.sum(ppl[27:36])
d["Friday"]=np.sum(ppl[36:45])
d["Saturday"]=np.sum(ppl[45:54])
d["Sunday"]=0
l.append(d)


d={}
driver.get('https://www.google.com/search?sa=X&biw=1002&bih=722&sxsrf=ACYBGNSXHYUvO9l4PV7z-qF6OSAxFsfpIw:1577292384259&q=ortho+specialist+in+Uttar+Pradesh+Based+on+visits&npsic=0&rflfq=1&rlha=0&rllag=28632801,77359922,2014&tbm=lcl&ved=2ahUKEwjR3pSCoNHmAhXrILcAHRJ4DzIQjGp6BAgKEE4&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m4!1u16!2m2!16m1!1e1!1m4!1u16!2m2!16m1!1e2!2m1!1e2!2m1!1e3!2m1!1e16!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:6723074238088024724,l,CjFvcnRobyBzcGVjaWFsaXN0IGluIFV0dGFyIFByYWRlc2ggQmFzZWQgb24gdmlzaXRzWmYKMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHMiMW9ydGhvIHNwZWNpYWxpc3QgaW4gdXR0YXIgcHJhZGVzaCBiYXNlZCBvbiB2aXNpdHM;mv:[[29.2034627,83.3362193],[25.085390999999998,76.9924222]];start:20')
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
d["Address"]=(add.text)
d["Monday"]=np.sum(ppl[:7])
d["Tuesday"]=np.sum(ppl[7:14])
d["Wednesday"]=np.sum(ppl[14:21])
d["Thursday"]=np.sum(ppl[21:28])
d["Friday"]=np.sum(ppl[28:35])
d["Saturday"]=np.sum(ppl[35:41])
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
d["Address"]=(add.text)
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
d["Address"]=(add.text)
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
d["Address"]=(add.text)
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
df.to_csv("Scrapped_data.csv")