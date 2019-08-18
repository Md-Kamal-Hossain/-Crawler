#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup as soup
from  urllib.request import urlopen as ureq
my_url = 'https://www.flipkart.com/search?q=iphones&otracker=start&as-show=on&as=off'
u_client = ureq(my_url)
page_html = u_client.read()
u_client.close()
Page_soup = soup(page_html,"html.parser")
#containers = Page_soup.findAll("div", {"class":"col _2-gKeQ"})
containers = Page_soup.findAll("div",{"class":"_1UoZlX"})
#print(len(containers))
#print(soup.prettify(containers[0]))
container = containers[0]
phone_name = container.find("div",{"class":"_3wU53n"})
#phone_name = phone_name.text
#print(phone_name)
price = container.find("div",{"class":"_1vC4OE _2rQ-NK"})
price = price.text
#print(price)
try:
    rank = container.find("div",{"class" : "hGSR34 _2beYZw"})
    
except:
    pass
rank = rank#.text
#print(rank)


# In[5]:


#for container in containers:
   # productname =container.find("div",{"class":"_3wU53n"})
    #productname = productname.text
    #price = container.find("div",{"class":"_1vC4OE _2rQ-NK"})
    #price = price.text
    #ratings = container.find("div",{"class" : "hGSR34 _2beYZw"})
    #ratings = ratings.text
    #print(productname)
    #print(price)
   # print(ratings)


# In[6]:


filename = "product.csv"
f = open(filename, "w")
headers =" productname,price,ratings/n"
f.write(headers)
for container in containers:
    productname = container.find("div",{"class":"_3wU53n"})
    productname = productname.text.strip()
    price = container.find("div",{"class":"_1vC4OE _2rQ-NK"})
    price = price.text.strip()
    ratings = container.find("div",{"class" : "hGSR34 _2beYZw"})
    ratings = ratings.text.strip()
    #print(productname)
    #print(price)
    #print(ratings)


# In[2]:


##string parsing
trim_price = ''.join(price.split(','))
rm_rupee = trim_price.split("₹")
add_rs_price = "RS."+ rm_rupee[1]
split_price = add_rs_price.split('E')
final_price = split_price[0]
#rating parse
split_rating = ratings.split(" ★")
final_rating = split_rating[0]
print(productname.replace(",","|") + "," +final_price + "," + final_rating + "\n")
f.write(productname.replace(",","|") + "," +final_price + "," + final_rating + "\n")
f.close()


# In[3]:


filename = "product.csv"
f = open(filename, "w")
headers =" productname,price,ratings/n"
f.write(headers)
for container in containers:
    productname = container.div.img["alt"]
    price = container.find("div",{"class":"col col-5-12 _2o7WAb"})
    price = price.strip()
    ratings = container.find("div",{"class" : "hGSR34 _2beYZw"})
    ratings = ratings.text
    print(productname)
    print(price)
    print(ratings)


# In[ ]:




