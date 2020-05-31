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
        self.author = 'Roi Levi'

    def get_all_country_stats(self, country, text=True):
        """
        Get country statistics, include infected amount, deaths amount, recovered amount and country's rank
        """
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
                    return [infected, deaths, recovered, ''.join(self.get_rank_by_country(country, text=False))]
                return {'Infected': infected, 'Deaths': deaths, 'Recovered': recovered, 'Rank': ''.join(self.get_rank_by_country(country, text=False))}
            return False
        else:
            raise ValueError(f'{country} is not supported, or not valid code-name. Please use only lower case names!')

    def get_global_stats(self, text=True):
        """
        Get global statistics, include infected amount, deaths amount, recovered amount and the country that have the highest amount of total cases
        """
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            body = soup.find('div', class_='row')
            infected = body.find('div').find('div', class_='card-body').find('span', class_='h5 card-title').text
            deaths = body.find('div', class_='card text-white col-md-3 ml-auto mr-auto mb-2').find('div').find('span', class_='h5 card-title').text.split()[0]
            recovered = body.findAll('div', class_='card text-center text-white col-md-3 ml-auto mr-auto mb-2')[1].find('div').find('span', class_='h5 card-title').text.split()[0]
            if not text:
                return [infected, deaths, recovered, ''.join(self.get_country_by_rank('1', text=False))]
            return {'Infected': infected, 'Deaths': deaths, 'Recovered': recovered, 'Highest Cases': ''.join(self.get_country_by_rank('1', text=False))}
        return False

    def get_country_infected(self, country, text=True):
        """
        Total amount of infected people cases in a country
        """
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        if country in self.countries:
            resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                body = soup.find('tbody').find('tr', {'onclick': f"window.location='coronavirus/{country}';"}).findAll('td')
                infected = body[1].text
                if not text:
                    return [infected]
                return {'Infected': infected}
            return False
        else:
            raise ValueError(f'{country} is not supported, or not valid code-name. Please use only lower case names!')

    def get_country_deaths(self, country, text=True):
        """
        Total amount of deaths cases in a country
        """
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        if country in self.countries:
            resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                body = soup.find('tbody').find('tr', {'onclick': f"window.location='coronavirus/{country}';"}).findAll('td')
                deaths = body[2].text
                if not text:
                    return [deaths]
                return {'Deaths': deaths}
            return False
        else:
            raise ValueError(f'{country} is not supported, or not valid code-name. Please use only lower case names!')
    
    def get_country_recovered(self, country, text=True):
        """
        Total amount of recovered cases in a country
        """
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        if country in self.countries:
            resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                body = soup.find('tbody').find('tr', {'onclick': f"window.location='coronavirus/{country}';"}).findAll('td')
                recovered = body[3].text
                if not text:
                    return [recovered]
                return {'Recovered': recovered}
            return False
        else:
            raise ValueError(f'{country} is not supported, or not valid code-name. Please use only lower case names!')

    def get_rank_by_country(self, country, text=True):
        """
        The rank is based on the amount of total cases in the country
        """
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        if country in self.countries:
            resp = requests.get('https://virusncov.com/', headers=headers)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.content, 'html.parser')
                rank = None
                for country_ in soup.find('tbody').findAll('tr'):
                    if country_.find('a', href=True)['href'] == f'/covid-statistics/{country}':
                        rank = country_.find('td').text
                if not text:
                    return [rank]
                return {'Rank': rank}
            return False
        else:
            raise ValueError(f'{country} is not supported, or not valid code-name. Please use only lower case names!')

    def get_country_by_rank(self, rank, text=True):
        """
        The rank is based on the amount of total cases in the country
        """
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
        resp = requests.get('https://virusncov.com/', headers=headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            country = None
            for country_ in soup.find('tbody').findAll('tr'):
                if country_.find('td').text == rank:
                    country = country_.find('a', href=True)['href'].split('/')[2]
            if not text:
                return [country]
            return {'Country': country}
        return False
