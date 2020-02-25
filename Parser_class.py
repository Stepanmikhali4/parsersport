from bs4 import BeautifulSoup
import urllib.request

class Parser:

    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        rec = urllib.request.urlopen(self.url)
        self.raw_html = rec.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        items = self.html.find_all('div', class_='se19-news-item')

        for thing in items:
            title = thing.find('a').get_text(strip=True)
            href = thing.a.get('href')
            self.results.append({
                'title': title,
                'href': href,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf=8') as f:
            i = 1
            for item in self.results:
                f.write(
                    f'Новость № {i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\n\n*******************\n\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
