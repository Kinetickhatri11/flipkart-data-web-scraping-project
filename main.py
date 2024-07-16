import requests
import pandas as pd
from bs4 import BeautifulSoup

product_name = []
prices = []
description = []
ratings = []

for i in range(2, 12):
    url = f"https://www.flipkart.com/search?q=mobiles+under+15000+5g&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_8_na_na_na&as-pos=3&as-type=RECENT&suggestionId=mobiles+under+15000+5g&requestId=50b6cd08-756e-45cc-9980-7b9bb35351f8&as-searchtext=mobiles+under+15000+5g&page={i}"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    section = soup.find("div", class_="DOjaWF gdgoEp")

    if section is not None:
        # Finding the product name
        productName = section.find_all("div", class_="KzDlHZ")
        for product in productName:
            name = product.text
            product_name.append(name)

        # Finding the price of the product
        price = section.find_all("div", class_="Nx9bqj _4b5DiR")
        for priceDivTag in price:
            priceOfProduct = priceDivTag.text
            prices.append(priceOfProduct)

        # Finding the description of the product
        desc = section.find_all("ul", class_="G4BRas")
        for details in desc:
            productDesc = details.text
            description.append(productDesc)

        # Finding the rating of the product
        rate = section.find_all("div", class_="XQDdHH")
        for ratingDiv in rate:
            ratingProduct = ratingDiv.text
            ratings.append(ratingProduct)

# Check the lengths of all lists
print(f"Product names: {len(product_name)}")
print(f"Prices: {len(prices)}")
print(f"Descriptions: {len(description)}")
print(f"Ratings: {len(ratings)}")

# Ensure all lists have the same length
max_length = max(len(product_name), len(prices), len(description), len(ratings))

while len(product_name) < max_length:
    product_name.append(None)
while len(prices) < max_length:
    prices.append(None)
while len(description) < max_length:
    description.append(None)
while len(ratings) < max_length:
    ratings.append(None)

# Create DataFrame
df = pd.DataFrame({
    "Product Name": product_name,
    "Prices": prices,
    "Descriptions": description,
    "Ratings": ratings
})

df.to_csv("C:/Users/Yash/Desktop/web scrapping/flipkart-Data.csv")
