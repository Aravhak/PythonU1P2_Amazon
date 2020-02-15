import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.in/dp/B06WWR2GZF/ref=s9_acsd_hps_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=73XNTRDZCES0GH9S774K&pf_rd_t=101&pf_rd_p=77d51b00-296a-4c1c-ae6c-01e450f8492f&pf_rd_i=20659894031'

headers = {"User_Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
def check_price():
    
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id= "productTitle").get_text()
    price = soup.find(id= "priceblock_ourprice").get_text()

    converted_price = (price[3:8])
    print(title.strip())
    scovPrice = converted_price.split(",")
    #print (scovPrice)
    price_final = scovPrice
    FinalPrice = float(price_final[0]+price_final[1])
    print (FinalPrice)
    



    if(FinalPrice < 4000.0):
        send_mail()
   # print(title.strip())
    #print(converted_price)
 

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('aravhak@gmail.com', 'PASSWORD')
    
    subject = 'The Price of the Playstation Controller dropped!'
    body= 'check this amazon link! https://www.amazon.in/dp/B06WWR2GZF/ref=s9_acsd_hps_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=73XNTRDZCES0GH9S774K&pf_rd_t=101&pf_rd_p=77d51b00-296a-4c1c-ae6c-01e450f8492f&pf_rd_i=20659894031'

    msg = f"Subject; {subject}\n\n{body}"

    server.sendmail(
        'aravhak@gmail.com',
        'haka@asbindia.org',
        msg
    )
        
    print("Email sent")

    server.quit()



while(True):
    check_price()
    time.sleep(86400)