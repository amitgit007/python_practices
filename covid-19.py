from plyer import notification
import requests
from bs4 import BeautifulSoup
def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="E:/python/practice/corona.ico",
        timeout=30
    )
def getdata(url):
    r=requests.get(url)
    return r.text


if __name__ == '__main__':
    notifyme("Amit","Lets fight COVID-19")
    myhtmldata=getdata('https://www.mohfw.gov.in/')
    soup= BeautifulSoup(myhtmldata, 'html.parser')
    #print(soup.prettify())
    mydatastr=""
    for tr in soup.find_all( 'tbody' )[9].find_all('tr')[0:27]:
        mydatastr =tr.get_text()
        mydatastr1 = mydatastr[1:]
        #print(mydatastr1)
        state_list=mydatastr1.split("\n")
        title="Displaying"
        msg=f" State :-"+ state_list[1] +"\n" + "total number of Indian cases:"+ state_list[2]+"\n" + "total number of foreign cases:"+ state_list[3]+"\n" + "total number of Cured:"+ state_list[4]+"\n" + "total number of Death:"+ state_list[5]
        states= ["Maharashtra", "Kerala"]
        if state_list[1] in states:
            print(msg)
            notifyme(title,msg)
