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
    #waiting for the pop up to accept the location
    WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[1]/div/section/div/div[2]/div")))
    browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[1]/div/section/div/div[2]/div").click()
    #waiting for the pop up to accept cookies
    WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.LINK_TEXT,"Accept")))
    browser.find_element(By.LINK_TEXT,"Accept").click()
    logs.append("accepted the pop ups.".upper())
    #Test-1 : checking carrer page is working fine by applying to the job
    browser.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/nav/div/div[2]/ul/li[6]").click() #click on career
    WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div/div[4]/div/div/div/div[2]/ul/li[1]/article/sly/a[1]")))
    article=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div/div[4]/div/div/div/div[2]/ul/li[1]/article/sly/a[1]")
    article_name=""
    article_name=article.text.strip()
    if article_name.split("\n")[0].upper()=="AVAILABLE POSITIONS":
        article.click()
        logs.append("CLICKED ON THE ARTICLE: {}.".format(article_name.split("\n")[0].upper()))
        WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/section/section/div[2]/div[3]/div[1]/button")))
        browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/section/section/div[2]/div[3]/div[1]").click()
        time.sleep(1.5)
        employment_type=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/section/section/div[2]/div[3]/div[1]/ul/li[3]/a")
        employment_type.click()#clicked temporary employment type
        browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/section/section/div[2]/div[3]/div[2]").click()
        job_category=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/section/section/div[2]/div[3]/div[2]/ul/li[4]/a")
        job_category.click()#clicked IT job category
        time.sleep(5)
        WebDriverWait(browser,10).until(EC.visibility_of_all_elements_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/section/ul[@class='joblisting']/li/a")))
        job_results=browser.find_elements(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/div/section/ul[@class='joblisting']/li/a")
        job_links=[i.get_attribute("href") for i in job_results]
        if len(job_results)==0 or len(job_links)==0:
            logs.append("NO JOBS AVAILABLE. MAYBE JOB LINKS ARE NOT EXTRACTED PROPERLY.")
        else:
            try:
                for i in job_links:
                    if "lang=en" in i:
                        browser.execute_script("window.open('{}')".format(i))
                        browser.switch_to.window(browser.window_handles[1])
                        WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div/div/div/section/div[3]/div[3]/div[2]/div[6]/a")))
                        browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div/div/div/section/div[3]/div[3]/div[2]/div[6]/a").click()
                        time.sleep(4)
                        msg=browser.find_element(By.XPATH,"/html/body/div/div").text.strip()
                        #testing if the apply button has loaded the page and whether the page is working fine or not.
                        if "not permitted to submit an online application" in msg or "inte tillåtet att skicka in ansökan online för" in msg:
                            logs.append("INTERNALLY NOT PERMITTED TO SUBMIT AN ONLINE APPLICATION.SO, CHECKING WHETHER DIRECT LINK IS WORKING OR NOT.")
                            browser.find_element(By.XPATH,"/html/body/div/div/p/a").click()
                            WebDriverWait(browser,15).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/main/div[2]")))
                            browser.find_element(By.XPATH,"/html/body/div/main/div[2]/p[2]/a").click()
                            logs.append("opened using direct link as the internal link is not working.".upper())
                            new_msg=browser.find_element(By.XPATH,"/html/body/div/div[2]/div[3]/div/div[1]/div/div[2]/h1").text.strip()
                            if "Developers to Scania" in new_msg:
                                logs.append("The direct link is working.".upper())
                                logs.append("\nCONCLUSION: THE CAREER PAGE IS FUNCTIONALLY WORKING FINE.")
                            else:
                                logs.append("even the direct link is not working.".upper())
                        else:
                            logs.append("INTERNALLY, JOB APPLICATION IS ACCEPTING.")
                        browser.close()
            except:
                logs.append("career page has some issues.".upper())
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