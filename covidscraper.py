import requests
import datetime
from bs4 import BeautifulSoup

def scrapeGlobalCase ():
    try:
        url = "https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F09c7w0&state=7&gl=US&ceid=US%3Aen"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        data = soup.find_all("div",class_ = "UvMayb")
        totalCases = (data[0].text.strip().replace(',', ''))
        deaths = (data[1].text.strip().replace(',', ''))
        totalDoses = (data[2].text.strip().replace(',', ''))
        fullyVaccinated = (data[3].text.strip().replace(',', ''))

        TimeNow = datetime.datetime.now()
        return {
            'date': str(TimeNow),
            'TotalCases': totalCases,
            'Deaths': deaths,
            'TotalDoses': totalDoses,
            'FullyVaccinated': fullyVaccinated,
        }
    except Exception as e: print(e)

testResult = scrapeGlobalCase()
#print("Date:", testResult['date'], "TotalCases:", testResult['TotalCases'], "Total Deaths:", testResult['Deaths'], "Total Doses:" , testResult['TotalDoses'], "Fully Vaccinated:", testResult['FullyVaccinated'])

