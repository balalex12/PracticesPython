#AUTHOR: BY BALALEX12

import requests

def convert_currency():    
    base = input("Enter the base currency: ")
    amount = float(input("Enter the amount: "))
    currency = input("Enter the currency you want to convert: ")

    """
    The following URL is the path that will lead to the Financial API.

    After the ?access_key you must put the key that grants said API, in my case it is a free 
    key where I can only consult rates based on the Euro.
    
    Then &base= goes the base currency you enter and then the symbols the currency you want to convert to.

    """
    url="http://data.fixer.io/api/latest?access_key=c40f7e0a278380b67256a0e748766e98&base="+base+"&symbols="+currency
    
    #Request gets the value that results when making the request or not, representing the response by 200 if it has been achieved.
    res = requests.get(url)
    if res.status_code != 200:        
        raise Exception("ERROR: API request unsuccessful.")
    else:
        #If the request could be made then the response is obtained the JSON object from the URL query.
        data = res.json()
        try:
            #You get from the "rates" and  "currency" key in the dictionary dates the required value which is the conversation rate.
            conversion_rates = data["rates"][currency]
            if len(currency) == 3: #Currency codes are usually 3 digits, this avoiding the error of more than digits when entering.
                result = amount * conversion_rates #The respective conversion is carried out.
                print("The conversion of "+str(amount)+" "+base+" to "+currency+" is "+str(result))
            else:
                print("The currency you want to convert to is not recognized.")
        except KeyError:
            print("Error: Rates were not obtained from the API.")
        
convert_currency()


#AUTHOR: BY BALALEX12
