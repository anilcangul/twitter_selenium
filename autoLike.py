from selenium import webdriver
import time
import userinfo
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

path = ".\chromeDriver\chromedriver.exe"  #chromeDriverın dosyadaki adresi
driver = webdriver.Chrome(path)
driver.get("https://twitter.com/login")

wait = WebDriverWait(driver, 600)
driver.maximize_window()

time.sleep(2) #2saniye bekletme

class giris_yap():
    def __init__(self,usurname,password):
        print("init çalıştırıldı.")
        self.username = usurname
        self.password = password


    def giris(self):
        username = driver.find_element_by_name("session[username_or_email]")
        password = driver.find_element_by_name("session[password]")

        username.send_keys(userinfo.username)
        password.send_keys(userinfo.password)
        time.sleep(1)
        giris_butonu = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
        giris_butonu.click()
        time.sleep(2)

G1 = giris_yap(usurname=userinfo,password=userinfo) #Giriş için userinfo dosyasındaki kullanıcı bilgilerini çekip obje yarrattık.
G1.giris()
time.sleep(1)

searchArea = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")


searchArea.send_keys("Keytorc",Keys.ENTER)

time.sleep(2)


"""latest = driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div[2]/div[2]/a/div/span")
latest.click()
time.sleep(2)
""" #Popüler tweetler yerine son tweetleri çekmek için.


def scroll(): #Sayfayı sonuna kadar kaydıran, Scroll özelliği katan javascript kodu.
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(2)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match=True

scroll() #Scroll fonksiyonunu çağırıyoruz.

time.sleep(2)

elements = driver.find_elements_by_xpath("//div[@data-testid='like']")

for element in elements:
    try:
        element.click()
        time.sleep(2)
    except Exception:
        print("Bir sorun oluştu...")




time.sleep(3)

driver.close()
