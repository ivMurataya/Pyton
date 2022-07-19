import requests
from bs4 import BeautifulSoup
import lxml

#url = "https://www.amazon.com/dp/B08QN98Y6M/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
url = "https://www.amazon.com.mx/iRobot-Aspirador-i3-Conexi%C3%B3n-Autom%C3%A1tica/dp/B09C15M22D/?_encoding=UTF8&pd_rd_w=Eqgtk&content-id=amzn1.sym.1c5d8e0c-283f-40f4-9793-c02ce22cd040&pf_rd_p=1c5d8e0c-283f-40f4-9793-c02ce22cd040&pf_rd_r=TS905X2QY91VEYQKP38G&pd_rd_wg=sARBF&pd_rd_r=980141c5-31a2-4237-9d85-9bd54c288caf&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
    "Accept-Language":"es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"

}
response = requests.get(url=url,headers=header)
print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup)

heading = soup.find(name="span", class_="a-offscreen")
print(heading.text)
a = heading.text.split("$")[1] # Get the number of the price, with $ Simbol, and removes it
finalPrice =float(a.replace(",", "")) # Remove the comas from the number and conver it to float number
print(finalPrice)

if finalPrice < 18000:
    print("Compralo")