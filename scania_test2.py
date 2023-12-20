from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
logs=[]
try:
    chrome_options=Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path=r"C:\Users\heman\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    browser=webdriver.Chrome(service=service,options=chrome_options)
    browser.maximize_window()
    browser.get("https://www.scania.com/")
    WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[1]/div/section/div/div[2]/div")))
    browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[1]/div/section/div/div[2]/div").click()
    WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.LINK_TEXT,"Accept")))
    browser.find_element(By.LINK_TEXT,"Accept").click()
    logs.append("accepted the pop ups.".upper())
    time.sleep(2)
    browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/nav/div/div[3]").click()
    time.sleep(2)
    WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[1]/div/nav/div/div[3]/ul/li/ul/li[3]/a")))
    browser.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/nav/div/div[3]/ul/li/ul/li[3]/a").click()
    logs.append("clicked on scania shop.".upper())
    browser.switch_to.window(browser.window_handles[1])
    try:
        WebDriverWait(browser,7).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[6]/div/div[5]/div[2]")))
        browser.find_element(By.XPATH,"/html/body/div[6]/div/div[5]/div[2]").click()
        logs.append("accepted the scania shop cookies.".upper())
    except:
        pass
    time.sleep(2)
    browser.find_element(By.XPATH,"/html/body/div[2]/div[4]/nav/ul/li[1]").click()
    time.sleep(2)
    logs.append("clicked on gifting section.".upper())
    WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div[4]/nav/ul/li[1]/div/ul/li/ul/li[2]/a")))
    browser.find_element(By.XPATH,"/html/body/div[2]/div[4]/nav/ul/li[1]/div/ul/li/ul/li[2]/a").click()
    logs.append("clicked on gifts for little scania fan.".upper())
    WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/main/div/div[1]/div[4]/ol/li[1]")))
    browser.find_element(By.XPATH,"/html/body/div[2]/main/div/div[1]/div[4]/ol/li[1]").click()
    logs.append("clicked on a truck toy.".upper())
    WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/main/div[2]/div/div[1]/div[5]/form/div/div/div[2]/button")))
    browser.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div/div[1]/div[5]/form/div/div/div[2]/button").click()
    logs.append("clicked on add to cart.".upper())
    time.sleep(7)
    WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/header/div[1]/div/div[5]/a")))
    browser.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/div[5]/a").click()
    logs.append("clicked on final shopping cart.".upper())
    WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/main/div[3]/div/div[2]/div[1]/ul/li[1]/button")))
    browser.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/div[2]/div[1]/ul/li[1]/button").click()
    logs.append("clicked on checkout.".upper())
    slp=3
    time.sleep(slp)
    while "checkout" not in browser.current_url and "shipping" not in browser.current_url:
        time.sleep(slp)
        slp+=2
        if slp>15:
            break
    if r"checkout/#shipping" in browser.current_url:
        logs.append("SUCCESFULLY ADDED THE ITEM IN CART AND LANDED IN SHIPPING PAGE.")
        logs.append("\nCONCLUSION: THE SCANIA SHOP IS FUNCTIONALLY WORKING FINE.")
    else:
        logs.append("UNSUCCESSFULL! The shipping page is not loaded.".upper())
    browser.quit()
except Exception as e:
    logs.append("IN EXCEPTION. ERROR OCCURRED!!! "+str(e))
    browser.quit()
finally:
    def print_logs(lst):
        print("\n")
        for i,j in enumerate(lst):
            if "CONCLUSION" not in j:
                print("{}.  {}".format(i+1,j),end="\n\n")
                #print(".............................................................................")
            else:
                print(j,end="\n\n")
    print_logs(logs)