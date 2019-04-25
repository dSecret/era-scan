from lxml import html
from lxml import etree
import requests
import json

url ='https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml'
cookies={
	"JSESSIONID":"8D676FE9A1E54DF7CDA353BB861CDBD5",
	"has_js":"1"
}
jar = requests.cookies.RequestsCookieJar()  
jar.set('JSESSIONID', '8D676FE9A1E54DF7CDA353BB861CDBD5', domain='parivahan.gov.in', path="/rcdlstatus/vahan")  
jar.set('has_js', '1', domain='parivahan.gov.in', path='/')

payload ={
	"form_rcdl":"form_rcdl",
	"form_rcdl:j_idt34:CaptchaID":"h3pxm",
	"form_rcdl:j_idt44":"form_rcdl:j_idt44",
	"form_rcdl:tf_dlNO":"DL-0420110149646",
	"form_rcdl:tf_dob_input":"09-02-1976",
	"javax.faces.ViewState":"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",
	"javax.faces.partial.ajax":"true",
	"javax.faces.partial.execute":"@all",
	"javax.faces.partial.render:form_rcdl":"pnl_show form_rcdl:pg_show form_rcdl:rcdl_pnl",
	"javax.faces.source":"form_rcdl:j_idt44"
}
headers = {
	# "Accept":"application/xml, text/xml, */*; q=0.01",
	# "Origin":"https://parivahan.gov.in",
	# "X-Requested-With":"XMLHttpRequest",
	# "Faces-Request":"partial/ajax",
	"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
	"Content-Type":"application/x-www-form-urlencoded"
}
page = requests.post(url,cookies=cookies,data=payload,headers=headers)
print(page.headers,"\n")
print(page.content)




# page = requests.get(url)

# baseUrl = 'https://parivahan.gov.in'
# tree = html.fromstring(page.content)

# captchaimg = tree.xpath('//*[@id="form_rcdl:j_idt35:j_idt40"]')
# key1=tree.xpath('//*[@id="j_id1:javax.faces.ViewState:0"]')
# # print(len(key1[0].get('value')))
# # #print(len(captchaimg))
# src = captchaimg[0].get('src')
# with open('captcha.png','wb') as tmp:
#     img = requests.get(baseUrl+src)
#     tmp.write(img.content)
# sessionid=page.cookies.get("JSESSIONID")
# print(sessionid)
# posturl="https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml"

# key=key1[0].get('value')
# curr="dl"
# print(len(key),"\n\n")
# with open('params.json','r') as raw:
#     params = json.load(raw)
# #print(params)
# def xhr():
#     params[curr]["javax.faces.ViewState"]=key
#     fillcap = requests.post(posturl,cookies=page.cookies,data=params[curr])
#     tree = etree.fromstring(fillcap.content)
#     newtoken=tree.xpath("//update[@id='j_id1:javax.faces.ViewState:0'][1]")
#     return newtoken[0].text

# key = xhr()
# print(len(key))
# # # print(len(key))
# curr ="dob"
# key = xhr()
# print(len(key))

# print("Enter your captcha")
# captchaVal = input()

# curr = "captcha"
# params[curr]["form_rcdl:j_idt35:CaptchaID"]=captchaVal
# key = xhr()

# print(len(key))
# cur = "submit"
# params[curr]["form_rcdl:j_idt35:CaptchaID"]= captchaVal
# print(params[curr]["form_rcdl:j_idt35:CaptchaID"])
# # print(key)
# resp = requests.post(posturl,cookies=page.cookies,data=params[curr])
# # tree = html.fromstring(resp.content)
# print(resp.content)
# # newtoken=tree.xpath("//update[@id='j_id1:javax.faces.ViewState:0'][1]")
# # print(newtoken[0].text,len(newtoken[0].text),"\n\n")
