from bs4 import BeautifulSoup

with open("Supreme_causelist.html", "r", encoding="utf8") as f:
    html_doc = f.read()
    f.close()
    
soup = BeautifulSoup(html_doc, "html.parser")

t1 = soup.find("div", {'align':'center'})


'''
for table in tables:
    tr_names = table.find_all("table",{'class':'mobview'})
    for tr_name in tr_names:
        th_names = tr_name.find_all("tr")
        for each in tr_names:
            thh_names = each.find_all("th")
            for thh_name in thh_names:
                #print(thh_name)
                data = thh_name.find_all("th")
                for each in data:
                    data1 = each.get("center")
                    l.append(data1)
'''

t2 = t1.find("table", {'class':'mobview'})
t3 = t2.find_all("tr")
#print(t3)
Links_pdf = []

for link in t2.find_all('a'):
    address = "https://main.sci.gov.in"
    data = str(link.get('href'))
    data1 = address + data
    Links_pdf.append(data1)
    #print(data1)

l_headers = []

for each in t3:
    th = each.find_all("th")
    #print(th)
    for each1 in th:
        center = each1.find_all("center")
        #print(str(center))
        for each2 in center:
            l_headers.append(each2.text)
    
print(l_headers)
#print(tables)
#print(thh_names)
#print(Links_pdf)
'''
dict ={
    'date_of_hearing':''
    'pdf_link': ''
    'description': ''
}
'''

l_pdf_name = []

for each in t3:
    td = each.find_all("td")
    #print(th)
    for each1 in td:
        center = each1.find_all("center")
        #print(str(center))
        for each2 in center:
            if (each2.text != ""):
             l_pdf_name.append(each2.text)



print(l_pdf_name)