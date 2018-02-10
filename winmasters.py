from parser import parser
import re
import pandas as pd

class winmasters(parser):
    def __init__(self, url='https://www.winmasters.com'):
        self.url = url
        parser.__init__(self, self.url)

    def get_football(self):
        self.football_url = 'https://www.winmasters.com/sports/football/'
        self._football_html = parser.get_football(self, football_url=self.football_url)

        team = self._football_html.findAll('div', attrs={'class': "content"})
        team = team[0].findAll('a')
        links = []
        for i in team:
            links.append(i['href'])

        team = []
        for link in links:
            html = parser.change_sport(self, new_url=self.url+link)
            for a in html.findAll('a', attrs={'rel': "tooltip"}):
                for span in a.findAll('span'):
                    team.append(span.text)
            for dd in html.findAll('dd'):
                print(dd.findAll('span'))

            # print(team)
            exit()




w = winmasters()
w.get_football()