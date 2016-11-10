#Package for checking adidas stock on shoes

import requests
import json
import time
from Tkinter import *

class AdidasStock:

    def __init__(self, clientId, sku):
        # Locale for me is always US, sucks for others
        self.session = requests.session()
        self.headers = {"User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"}
        self.locale = 'US'
        self.clientId = clientId
        self.sku = sku
        self.skus = []

    def getVarientStock(self, sku):
        base = "http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US"
        urlVariantStock = base + '/Product-GetVariants?pid=' + sku
        self.session.headers = self.headers
        r = self.session.get(urlVariantStock)
        try:
            versions = json.loads(r.text)['variations']['variants']
        except:
            if r.status_code == 404:
                return {'error' : '"' + self.sku + '" is an invalid SKU!'}
            else:
                return {'error' : 'There was an error checking Stock, make sure the SKU is correct and try again.'}
            return
        stock = {}
        total = 0
        for version in versions:
            stockCount = version["ATS"]
            total += int(stockCount)
            stockSizes = version["attributes"]["size"]
            stock[stockSizes] = stockCount
        stock['total'] = total
        return stock

while False:
    sku = raw_input("Enter the SKU for the requested shoe: ")
    cId = raw_input("If you have a ClientId, enter it now. If not, click enter: ")
    a = AdidasStock(cId, sku)
    a.getVarientStock(sku)
    
#for sku in x.keys():
#    AdidasStock.getVarientStock(x[sku], sku)
#    time.sleep(5)


