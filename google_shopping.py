from bs4 import BeautifulSoup
import requests


def price_crawler():
    url = 'https://www.google.com/search?q=bose+soundlink+mini+2&client=safari&rls=en&source=lnms&tbm=shop&sa=X&ved=0ahUKEwjCiqmdt-nWAhWHz4MKHVFiCzIQ_AUICigB&biw=1397&bih=794'
    page_source = requests.get(url)
    plain_text = page_source.text
    soup = BeautifulSoup(plain_text, "lxml")

    prices = []

    # print(soup.prettify())

    for div in soup.find_all('div', {'class': '_OA'}):

        for b in div('b'):
            price = b.get_text().split("$")

            # print (div)
            print (float(price[1]))
            prices.append(float(price[1]))

    # sum = 0
    # for indvPrice in prices:
    #     sum = sum + indvPrice

    average = sum(prices) / len(prices)

    print ("AVERAGE PRICE: $" + str(average))


price_crawler()
