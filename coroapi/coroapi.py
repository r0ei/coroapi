import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

class Corona:
    def __init__(self):
        self.date = datetime.now()
        self.countries = ["usa", "brazil", "russia", "spain", "uk", "italy", "france", "germany", "india", "turkey", "iran",
                 "peru", "chile", "canada", "mexico", "saudi-arabia", "pakistan", "belgium", "qatar", "netherlands",
                 "bangladesh", "belarus", "ecuador", "sweden", "singapore", "portugal", "switzerland",
                 "south-africa", "colombia", "kuwait", "indonesia", "ireland", "poland", "ukraine", "egypt", "romania",
                 "philippines",  "israel", "japan", "austria", "dominican-republic", "argentina", "afghanistan", "panama",
                 "denmark","south-korea","serbia","bahrain","oman","kazakhstan","nigeria","czech-republic","algeria", "armenia",
                 "bolivia","norway","moldova","ghana","malaysia","morocco","australia","finland", "iraq","cameroon","azerbaijan",
                 "honduras","guatemala","sudan","luxembourg","hungary","tajikistan","guinea","senegal","uzbekistan","djibouti",
                 "thailand","greece","gabon","bulgaria", "bosnia-and-herzegovina",
                 "el-salvador","croatia","cuba","estonia","somalia","iceland", "kenya","kyrgyzstan","mayotte","lithuania",
                 "maldives","haiti","sri-lanka","slovakia","new-zealand","slovenia","nepal","venezuela","equatorial-guinea","guinea-bissau",
                 "mali","lebanon","albania","tunisia","latvia","ethiopia","zambia","costa-rica","south-sudan","niger",
                 "cyprus","paraguay","central-african-republic","sierra-leone","burkina-faso","uruguay","andorra","chad","nicaragua","madagascar",
                 "georgia","jordan","san-marino","malta","jamaica","congo","channel-islands","tanzania","reunion","french-guiana",
                 "taiwan","togo","mauritania","rwanda","isle-of-man","mauritius","uganda","vietnam","montenegro",
                 "yemen","liberia","malawi","mozambique","myanmar","benin","martinique","mongolia","gibraltar","guadeloupe",
                 "zimbabwe","guyana", "cayman-islands","bermuda","cambodia","syria","libya","trinidad-and-tobago","bahamas",
                 "aruba","monaco","barbados","comoros","liechtenstein","angola","sint-maarten","french-polynesia","burundi",
                 "saint-martin","eritrea","botswana","bhutan", "saint-vincent-and-the-grenadines","antigua-and-barbuda","gambia","timor-leste",
                 "grenada","namibia", "new-caledonia","belize","curacao","fiji","saint-lucia", "dominica","saint-kitts-and-nevis",
                 "greenland","suriname", "montserrat","seychelles","western-sahara","british-virgin-islands","papua-new-guinea",
                 "caribbean-netherlands", "anguilla","lesotho", "china"]

    def get_all_country_stats(self, country, text=True):
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        if country in self.countries:
            resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                body = soup.find('tbody').find('tr', {'onclick': f"window.location='coronavirus/{country}';"}).findAll('td')
                infected = body[1].text
                deaths = body[2].text
                recovered = body[3].text
                if not text:
                    return f'{infected}\n{deaths}\n{recovered}'
                return f'Infected: {infected}\nDeaths: {deaths}\nRecovered: {recovered}'
            return False
        else:
            raise ValueError(f'{country} is not supported, or not valid code-name')

    def get_global_stats(self, text=True):
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            body = soup.find('div', class_='row')
            infected = body.find('div').find('div', class_='card-body').find('span', class_='h5 card-title').text
            deaths = body.find('div', class_='card text-white col-md-3 ml-auto mr-auto mb-2').find('div').find('span', class_='h5 card-title').text.split()[0]
            recovered = body.findAll('div', class_='card text-center text-white col-md-3 ml-auto mr-auto mb-2')[1].find('div').find('span', class_='h5 card-title').text.split()[0]
            if not text:
                return f'{infected}\n{deaths}\n{recovered}'
            return f'Infected: {infected}\nDeaths: {deaths}\nRecovered: {recovered}'
        return False

    def get_country_infected(self, country, text=True):
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        if country in self.countries:
            resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                body = soup.find('tbody').find('tr', {'onclick': f"window.location='coronavirus/{country}';"}).findAll('td')
                infected = body[1].text
                if not text:
                    return f'{infected}'
                return f'Infected: {infected}'
            return False
        else:
            raise ValueError(f'{country} is not supported, or not valid code-name')

    def get_country_deathes(self, country, text=True):
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        if country in self.countries:
            resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                body = soup.find('tbody').find('tr', {'onclick': f"window.location='coronavirus/{country}';"}).findAll('td')
                deaths = body[2].text
                if not text:
                    return f'{deaths}'
                return f'Deaths: {deaths}'
            return False
        else:
            raise ValueError(f'{country} is not supported, or not valid code-name')
    
    def get_country_recovered(self, country, text=True):
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        if country in self.countries:
            resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                body = soup.find('tbody').find('tr', {'onclick': f"window.location='coronavirus/{country}';"}).findAll('td')
                recovered = body[3].text
                if not text:
                    return f'{recovered}'
                return f'Recovered: {recovered}'
            return False
        else:
            raise ValueError(f'{country} is not supported, or not valid code-name')
