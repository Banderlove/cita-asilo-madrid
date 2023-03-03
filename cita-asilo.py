from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import winsound

frequency = 2500
duration = 10000


cycle_cita = True

while cycle_cita == True:
     browser = webdriver.Chrome()
     
     chrome_options = Options()
     
     chrome_options.add_experimental_option("detach", True)
     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
     chrome_options.add_experimental_option("useAutomationExtension", False)
     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
     chrome_options.add_argument("--ignore-certificate-errors")
     chrome_options.add_argument("--ignore-ssl-errors")
     chrome_options.add_argument("--disable-gpu")
    
     browser.implicitly_wait(30)
     browser.maximize_window()
     browser.base_url = "https://www.google.com/"
     browser.verificationErrors = []
     browser.accept_next_alert = True
     browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
     browser.get("https://icp.administracionelectronica.gob.es/icpplus/index.html")
     
     
     #1.  Accept Cookies.
     print("#1.Accept Cookies")
     cookie_kill = WebDriverWait(browser, 10).until(
              EC.presence_of_element_located(
               (By.XPATH, "/html/body/div[2]/span/a[1]")))
     
     cookie_kill.click()     
     
     #2.  Select Province.
     print("#2.Select Province")
     time.sleep(0.2)
     provincebox = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
             (By.ID, "form")))

     provincebox.click()
     
     province = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
             (By.XPATH, '//*[@id="form"]/option[34]')))  #Provincia: Madrid
     
     province.click()
     
     time.sleep(0.2)
     accept = WebDriverWait(browser, 10).until(
          EC.presence_of_element_located(
           (By.XPATH, "/html/body/div[1]/div/main/div/div/section/div[2]/form/div[3]/input[1]")))  #Trámite: ASILO - PRIMERA CITA-provincia de Madrid
     accept.click()
     
     #3.  Select operation.
     print("#3.Select Operation")
     time.sleep(2)
     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     
     time.sleep(0.2)
     appointment_type = WebDriverWait(browser, 10).until(
               EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/main/div/div/section/div[2]/form[1]/div[3]/div[1]/div[2]/div/fieldset/div[2]/select/option[3]")))
                
     appointment_type.click()
     
     time.sleep(0.2)
     accept = WebDriverWait(browser, 10).until(
          EC.presence_of_element_located(
           (By.XPATH, "/html/body/div[1]/div[2]/main/div/div/section/div[2]/form[1]/div[4]/input[1]")))
                
     accept.click()
     
     #4.  Skip instructions.
     print("#4.Skip Instructions")
     time.sleep(2)
     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     
     time.sleep(0.2)
     enter = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
         (By.XPATH, "/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div/div[2]/input[1]")))
         
     enter.click()
     
     #5.  Fill personal info.
     print("#5.Fill Personal Info")
     time.sleep(2)
     passport_option = WebDriverWait(browser, 10).until(
                  EC.presence_of_element_located(
                   (By.XPATH, "/html/body/div[1]/div/main/div/div/section/div[2]/form/div/div/div[1]/div[2]/div/div/div[1]/fieldset/ul/li[3]/input")))
                   
     passport_option.click()
     
     passportbox = WebDriverWait(browser, 10).until(
             EC.presence_of_element_located(
              (By.XPATH, "/html/body/div[1]/div/main/div/div/section/div[2]/form/div/div/div[1]/div[2]/div/div/div[2]/input")))
     
     passportbox.click()
     passportbox.send_keys("PASSPORT")  #Sustituye "PASSPORT" por tu número de pasaporte,tiene que llevar comillas "",ejemplo: "185201478"
     
     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     
     time.sleep(0.2)
     namebox = WebDriverWait(browser, 10).until(
          EC.presence_of_element_located(
           (By.XPATH, "/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div/div/div[1]/div[3]/div/div/div/div/input[1]")))
     
     namebox.click()
     namebox.send_keys("NAME LASTNAME LASTNAME")  #Sustituye "NAME" por tu nombre y apellidos que aparezcan en tu pasaporte,tiene que llevar comillas "",ejemplo: "ALBERTO TORRES RUIZ"
     
     yearbox = WebDriverWait(browser, 10).until(
          EC.presence_of_element_located(
           (By.XPATH, "/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div/div/div[1]/div[4]/div/div/div/div/input[1]")))
     
     yearbox.click()
     yearbox.send_keys("YEAR")  #Sustituye "YEAR" por tu fecha de nacimiento que aparezca en tu pasaporte,tiene que llevar comillas "",ejemplo: "1986"
     
     countrybox = WebDriverWait(browser, 10).until(
          EC.presence_of_element_located(
           (By.ID, "txtPaisNac")))

     countrybox.click()
     
     country = WebDriverWait(browser, 10).until(
          EC.presence_of_element_located(
           (By.XPATH, "//option[@value='248']")))  #Sustituye el valor "248 por el país de tu nacionalidad: revisa el archivo nacionalidades.txt y sustituye el valor 248 por el código de tu país
           
     country.click()

     time.sleep(0.2)
     accept = WebDriverWait(browser, 10).until(
             EC.presence_of_element_located(
              (By.XPATH, "/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div/div/div[2]/input[1]")))
              
     accept.click()
     
     #6.  Searching for Appointment.
     print("#6.Searching for Appointment")
     time.sleep(0.2)
     request_appointment = WebDriverWait(browser, 10).until(
                 EC.presence_of_element_located(
                  (By.XPATH, "/html/body/div[1]/div/main/div/div/section/div[2]/form/div/div/div[2]/input[1]")))
                  
     request_appointment.click()
     
     txt = "En este momento no hay citas disponibles"
     page_source = browser.page_source
     
     #7.  No appointments aviable.
     if txt in browser.page_source:
        print("#No appointments aviable,retry in 3 minutes")
        browser.close()
        time.sleep(180)
     else: #8.  Appointment aviable
          print("#Hey, there are appointments aviable")
          winsound.Beep(frequency, duration)  #CUANDO ENCUENTRA CITAS DISPONIBLES,EMITE UN PÍTIDO MUY FUERTE
          cycle_cita = False
          time.sleep(600)
          print("Bot Shutdown")
          browser.close()
          break