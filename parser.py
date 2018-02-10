import proxy_changer as prch
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

class parser:
    def __init__(self, url):
        prch.check_ip()
        self.url = url
        self.html = ''

    def read_url(self):
        self.html = urllib.request.urlopen(self.url).read()


    def get_date(self):
        now = datetime.now()
        date = now.strftime("%Y-%m-") + str(now.day)
        return date

    def create_soup(self):
        parser.read_url(self)
        self.html = BeautifulSoup(self.html)
        return self.html

    def change_sport(self, new_url):
        new_sport = BeautifulSoup(urllib.request.urlopen(new_url).read())
        return new_sport

    def print_(self, bs_obj):
        print(bs_obj.prettify())


    def get_football(self, football_url):
        return parser.change_sport(self, new_url=football_url)


    def get_tennis(self, tennis_url):
        return parser.change_sport(self, new_url=tennis_url)


    def get_ice_hockey(self, hockey_url):
        return parser.change_sport(self, new_url=hockey_url)

    @classmethod
    def binary_team(self, all_teams):
        team_1 = []
        team_2 = []
        i = 0
        for team in all_teams:
            if i % 2 == 0:
                team_1.append(team)
            else:
                team_2.append(team)
            i += 1
        return team_1, team_2

    def get_factor_1x2(self, factors, line):

        bets = []
        count = 0
        temp = []

        for bet in factors:
            if count in [0, 1, 2]:
                temp.append(bet)

            count += 1

            if count == line:
                bets.append(temp)
                count = 0
                temp = []
                continue
        return bets





# url = 'https://sports.sportingbet.com/en/sports'
# pa = parser(url)
# pa.read_url()
# pa.create_soup()

