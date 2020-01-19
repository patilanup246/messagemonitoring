# importing the required libraries

from bs4 import BeautifulSoup as soup
import requests
import csv

def main():
    file_name = 'ebay_wavery_hills.csv'
    data_to_file = open(file_name, 'w', newline='')
    csv_writer = csv.writer(data_to_file, delimiter=',')
    csv_writer.writerow(["ebay_url", "item_details_url", "ebay_seller_url", "ebay_title", "ebay_item_number", "ebay_product_condition", "ebay_price", "ebay_seller", "ebay_upc", "ebay_mpn", "ebay_brand"])

    items_per_page = 0
    for pages in range(1, 2):   # page iterations
        try:
            #   if pages > 3:
            #       debug = ''

            if items_per_page == 0:
                url = 'https://www.ebay.com/sch/m.html?_nkw=&_armrs=1&_from=&_ssn=waverlyhills1&_pgn=1&rt=nc'
            else:
                url = 'https://www.ebay.com/sch/m.html?_nkw=&_armrs=1&_from=&_ssn=waverlyhills1&_pgn=' + str(pages) + '&_skc=' + str(items_per_page) + '&rt=nc'
            ureq = requests.get(url)
            page_soup = soup(ureq.content, 'html5lib')
            table = page_soup.findAll('h3', {'class': 'lvtitle'})    # print(len(table))

            b = 1
            for rows in table:   # Row iteration
                try:

                    ebay_url = 'https://www.ebay.com/sch/waverlyhills1/m.html?_nkw=&_armrs=1&_from='
                    ebay_title = rows.text.strip()
                    item_details_url = rows.find('a').attrs['href']
                    item_url_request = requests.get(item_details_url)
                    item_soup = soup(item_url_request.content, 'html5lib')
                    try:
                        ebay_upc = item_soup.find('h2', {'itemprop': 'gtin13'}).text.strip()
                    except Exception:
                        table_item = item_soup.findAll('div', {'class', 'prodDetailSec'})
                        if len(table_item) > 0:
                            for row_item in table_item:
                                a = row_item.findAll('td')
                                for i in range(0, len(a)):
                                    if row_item.findAll('td')[i].text.strip().upper() == 'UPC':
                                        ebay_upc = (row_item.findAll('td')[i + 1].text.strip())
                        if ebay_upc is None :
                            ebay_upc = 'Not Aplicable'
                        pass

                    try:
                        ebay_seller_url = item_soup.find('div', {'class', 'mbg vi-VR-margBtm3'}).a['href']
                    except Exception:
                        ebay_seller_url = 'Not Aplicable'
                        pass

                    try:
                        ebay_item_number = item_soup.find('div', {'id': 'descItemNumber'}).text.strip()
                    except Exception:
                        ebay_item_number = 'Not Aplicable'
                        pass

                    try:
                        ebay_product_condition = item_soup.find('div', {'id': 'vi-itm-cond'}).text.strip()
                    except Exception:
                        ebay_product_condition = 'Not Aplicable'
                        pass

                    try:
                        ebay_price = item_soup.find('span', {'id': 'convbinPrice'}).text.strip()
                    except Exception:
                        ebay_price = 'Not Aplicable'
                        pass

                    try:
                        ebay_seller = item_soup.find('span', {'class': 'mbg-nw'}).text.strip()
                    except Exception:
                        ebay_seller = 'Not Aplicable'
                        pass

                    try:
                        ebay_mpn = item_soup.find('h2', {'itemprop': 'mpn'}).text.strip()
                    except Exception:
                        table_item = item_soup.findAll('div', {'class', 'prodDetailSec'})
                        if len(table_item) > 0:
                            for row_item in table_item:
                                a = row_item.findAll('td')
                            #    print('a.row size  :  ' + str(len(a)))
                                for i in range(0, len(a)):
                                    if row_item.findAll('td')[i].text.strip().upper() == 'MPN':  # or 'MANUFACTUREPRODUCTNUMBER':
                                        ebay_mpn = (row_item.findAll('td')[i + 1].text.strip())
                        if ebay_mpn is None :
                            ebay_mpn = 'Not Aplicable'
                        pass

                    try:
                        ebay_brand = item_soup.find('h2', {'itemscope': 'itemscope'}).find('span').text.strip()
                        # item_soup.findAll('span', {'itemprop' : 'name'})[6].text.strip()
                    except Exception:
                        table_item = item_soup.findAll('div', {'class', 'prodDetailSec'})
                        if len(table_item) > 0:
                            for row_table in table_item:
                                a = row_table.findAll('td')
                                for i in range(0, len(a)):
                                    if row_table.findAll('td')[i].text.strip().upper() == 'BRAND':
                                        ebay_brand = (row_table.findAll('td')[i + 1].text.strip())
                        if ebay_brand is None :
                            ebay_brand = 'Not Aplicable'
                        pass
                    csv_writer.writerow([ebay_url, item_details_url, ebay_seller_url, ebay_title, ebay_item_number, ebay_product_condition, ebay_price, ebay_seller, ebay_upc, ebay_mpn, ebay_brand])
                    b = b + 1

                except Exception:
                    print(' - - ->> Inner-Page level ERROR NO  :  ' + str(pages) + '  , ROW NO : ' + str(b))
                    b = b + 1
                    pass

            items_per_page += 50
            print('Completed page No. ' + str(pages))

        except Exception:
            print("Page Level ERROR NO :  " + str(pages))
            items_per_page += 50
            pass

if __name__ == '__main__':
    main()
