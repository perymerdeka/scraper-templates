# importing module
import requests
import json
import math
import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

""" CLASS BASED SCRAPER TEMPLATE

How To Use
1. Creating Virtual Environtment
2. Install Requirements.txt
3. Change the Template as Needed

NOTE: if you need selenium driver extract it from `selenum_driver` directory

Selenium Driver Support:
- Chrome (Linux, Windows, Mac)
- Firefox (Linux, Windows, Mac)

# Requests Module
Requests Docs: https://requests.readthedocs.io/en/master/

 # Parsing Docs
Selenium Docs: https://selenium-python.readthedocs.io/
BeautifulSoup Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

 # Pandas Docs
Pandas: https://pandas.pydata.org/docs/

"""


class Scraper:
    results = []  # <- getting all url in one pages

    final_results = []  # <- Store All Final Result

    # simple headers
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
        'cache-control': 'max-age=0',
        # 'cookie':'zguid=23|%2482971312-d59b-4dbf-95e6-be130386df47; zgsession=1|5a99c9d4-4d68-4926-8ad9-645ef59232d3; _ga=GA1.2.1911770309.1609684744; _gid=GA1.2.567505807.1609684744; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; zjs_user_id=null; zjs_anonymous_id=%2282971312-d59b-4dbf-95e6-be130386df47%22; _gcl_au=1.1.432493643.1609684746; KruxPixel=true; DoubleClickSession=true; _pxvid=6e6f9ed3-4dd1-11eb-a0fb-0242ac12000e; _pin_unauth=dWlkPVpHUXlNR1JoTkRNdFpqUmlNUzAwT1dSa0xXSXpOMll0TjJJd05ESXdOV1ptTkRFdw; KruxAddition=true; g_state={"i_p":1609694581605,"i_l":1}; JSESSIONID=58F1189F61A4E62830C9E1577A776160; _px3=f7c3f9a333c148cb851665258ec4b7589cdc6db6b40183560c794a50097773ab:YQWzRQ3YL9ybVCojGYRFeEVm2CuOUepLnLgS8rxRLlb2JLJEy9DR7m5oVclE8ZWuwgIitoxFTAtaA3tMyA6/8A==:1000:WkYVEE+mCK+jlGnca7AJU9f49kQHr/dQx8h0ATyLNpFRW5k622JQK56sbVDbmQmgNXUcDlfWuH7ZjBvBSraH1T4Tc6WWXMNp9z+nhxODOlH7qAPF/d2O545/PxzCrWnON9y4eBftj0wc6whJLlxJgFqcG6vvcUDcbdaJ7i0YNCo=; _uetsid=6ee457b04dd111eba15027b6e0f16ac3; _uetvid=6ee4a5704dd111eb81fb1b375ee4179a; ki_r=; _gat=1; search=6|1612344715732%7Crect%3D41.2150938491687%252C-73.1429955625%252C40.1927894141644%252C-74.8129174375%26rid%3D6181%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%096181%09%09%09%09%09%09; ki_s=; AWSALB=lHPoabWbXYbNGvKvYt1gxXP4nbu1VVgjApd8xBy4QV69bNnQFyo1zIS9OcZP3OGY3Yj//v+Lo0L9gaEm7Mc78Ebd7Ocb/00Z0l2Er7+nAk8ryv9gdjLhArC4SC1g; AWSALBCORS=lHPoabWbXYbNGvKvYt1gxXP4nbu1VVgjApd8xBy4QV69bNnQFyo1zIS9OcZP3OGY3Yj//v+Lo0L9gaEm7Mc78Ebd7Ocb/00Z0l2Er7+nAk8ryv9gdjLhArC4SC1g; ki_t=1609752622273%3B1609752622273%3B1609752727193%3B1%3B7',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 '
                      'Safari/537.36 '
    }

    # creating function to handle response
    def get_response(self, url, params):
        res = requests.get(url, params=params, headers=self.headers)

        # url checking
        f = open('res.html', 'w+')
        f.write(res.text)
        f.close()
        print(f'Response Status Code: {res.status_code}')
        return res

    # function to getting total page from website
    def get_total_pages(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        # getting total page with some method
        pages = soup.find('sometags')
        item_count = 40  # <- sum content in one pages
        total_pages = math.ceil(int(pages) / item_count)

        return total_pages

    # function to get all detail_url in one pages
    def get_url(self, response):
        soup = BeautifulSoup(response, 'html.parser')

        # scraping process
        container = soup.find('sometags', attrs={'attribute': 'attrs_value'})
        self.results.append(container)
        return self.results

    # function to get detail items from pages (use selenium/ requests)
    def get_detail(self, content_results):
        """ example use selenium """
        PATH = os.path.abspath(os.path.join(os.curdir, 'chromedriver'))
        driver = webdriver.Chrome(PATH)

        # generate json file to view result
        with open('results.json', 'w+') as file:
            # generate result
            data_result = {
                'data_result': content_results,
            }
            json.dump(data_result, file)

        # dev mode
        content_result = content_results[0:1]

        # scraping process
        for data in content_result:
            print('processing URL: {}'.format(data['url']))
            driver.get(data['url'])

            # content checking
            print('Getting Source... of URL: {}'.format(data['url']))
            f = open('res_detail.html', 'w+')
            f.write(driver.page_source)
            f.close()

            # getting Detail Content
            print('Parsing Content...')
            person = []

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # getting dict results
            data_dict = {
                'some_data': person
            }

            # close driver after scraping process
            driver.close()
            return data_dict

    # create csv with pandas
    def create_csv_pandas(self, filename, final_results):
        df = pd.DataFrame(final_results)

        # creating csv
        print('Creating CSV ...')
        csv_file = df.to_csv(filename + '.csv', final_results, index=False)
        print(f'File {filename + ".csv"} Created')
        return csv_file

    # create excel with pandas
    def create_excel_pandas(self, filename, final_results):
        df = pd.DataFrame(final_results)

        # creating excel
        print('Creating Excel File ...')
        excel_file = df.to_excel(filename + '.csv', final_results, index=False)
        print(f'File {filename + ".xlsx"} Created')
        return excel_file

    def run(self):
        # params
        params = {
            'searchQueryState': '{"pagination":{},"usersSearchTerm":"New York, NY","mapBounds":{"west":-74.8129174375,"east":-73.1429955625,"south":40.42945465007956,"north":40.98120890098652},"regionSelection":[{"regionId":6181,"regionType":6}],"isMapVisible":true,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true,"mapZoom":9}',
            'wants': '{"cat1":["listResults","mapResults"]}',
            'requestId': '4'
        }
        #  define website url
        url = 'https://example.com/'

        # getting response
        res = self.get_response(url=url, params=params)

        # total pages
        total_pages = self.get_total_pages(res.text)
        for page in range(total_pages):
            new_params = {
                'searchQueryState': '{"pagination":{"currentPage":%s},"usersSearchTerm":"New York, NY","mapBounds":{"west":-74.8129174375,"east":-73.1429955625,"south":40.42945465007956,"north":40.98120890098652},"regionSelection":[{"regionId":6181,"regionType":6}],"isMapVisible":true,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true,"mapZoom":9}' % str(
                    page),
                'wants': '{"cat1":["listResults","mapResults"]}',
                'requestId': '4'
            }

            # scraping process
            res = self.get_response(url, params=params)
            self.get_url(res.text)
            self.get_detail(content_results=self.results)

            self.final_results.append(self.get_detail(content_results=self.results))

        # create csv file
        self.create_excel_pandas('sample', final_results=self.final_results)

        # create excel file
        self.create_excel_pandas('sample', final_results=self.final_results)


if __name__ == '__main__':
    scraper = Scraper()
    scraper.run()
