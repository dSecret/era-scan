from lxml import html
import json
from selenium import webdriver
import requests
import time,os,sys

os.environ["MOZ_HEADLESS"] = "1"


url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'

def get_captcha():
    print("Enter the captcha")
    return input()


def main():
    browser = webdriver.Firefox()
    browser.get(url)
    def find(text):
        return browser.find_element_by_xpath(text)


    dial = find('//*[@id="form_rcdl:tf_dlNO"]')
    dob = find('//*[@id="form_rcdl:tf_dob_input"]')
    captcha = find('//*[@id="form_rcdl:j_idt34:CaptchaID"]')
    imgelem = find('//*[@id="form_rcdl:j_idt34:j_idt39"]')
    submit = find('//*[@id="form_rcdl:j_idt44"]')

    with open('captcha.png','wb') as tmp:
        img =requests.get(imgelem.get_attribute("src"))
        tmp.write(img.content)

    dial.send_keys("DL-0420110149646")
    dob.send_keys("09-02-1976")

    capValue = get_captcha()
    captcha.send_keys(capValue)

    submit.click()
    #time.sleep(3)
    while True:
        try:
            status = find('/html/body/form/div[1]/div[3]/div[2]/span/div/div/div/div/div/table[1]/tbody/tr[1]/td[2]/span').text
        except Exception as e:
            pass
        else:
            break
        try:
            captcha_err = find('/html/body/form/div[1]/div[3]/div[1]/div/div[2]/div[1]/div')
        except Exception as e:
            pass
        else:
            print("In valid captcha")
            #sys.exit()
            browser.close()
            main()
        try:
            details_err = find('/html/body/div[3]/div[1]/span')
        except Exception as e:
            pass
        else:
            print("No details")
            #sys.exit()
            browser.close()
            main()

    name = find('/html/body/form/div[1]/div[3]/div[2]/span/div/div/div/div/div/table[1]/tbody/tr[2]/td[2]').text
    doi = find('/html/body/form/div[1]/div[3]/div[2]/span/div/div/div/div/div/table[1]/tbody/tr[3]/td[2]').text
    lta = find('/html/body/form/div[1]/div[3]/div[2]/span/div/div/div/div/div/table[1]/tbody/tr[4]/td[2]').text

    print(status,name,doi,lta)

main()
