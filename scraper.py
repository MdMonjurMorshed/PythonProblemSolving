from bs4 import BeautifulSoup
import requests

req=requests.get("https://reportsemitraapp.rajasthan.gov.in/WebSrc/Reports/rpt_search_new_emitra_ksk.jsp")
cont= req.content
bs=BeautifulSoup(cont,'html.parser')
print(bs.prettify())