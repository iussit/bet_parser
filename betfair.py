from parser import parser
import re
import pandas as pd

class betfair(parser):
    def __init__(self, url='https://www.betfair.com/sport/'):
        self.url = url
        parser.__init__(self, self.url)


    def get_football(self):
        self.football_url = 'https://www.betfair.com/sport/football'
        self._football_html = parser.get_football(self, football_url=self.football_url)

        req = re.compile('\\n')
        team_1 = []
        for i in self._football_html.findAll('span', attrs={'class': "home-team-name"}):
            team_1.append(req.sub('', i.text))

        team_2 = []
        for i in self._football_html.findAll('span', attrs={'class': "away-team-name"}):
            team_2.append(req.sub('', i.text))

        all_factor = []
        for factor in self._football_html.findAll('a', attrs={'data-is-fctc': "0"}):
            all_factor.append(factor.span.text)

        bets = parser.get_factor_1x2(all_factor, 3)

        football_bets = pd.DataFrame({'team1': team_1,
                                      'team2': team_2,
                                      'bets': bets[0:len(team_1)]})
        return football_bets


    def get_ice_hockey(self):
        self.hockey_url = 'https://www.betfair.com/sport/ice-hockey'
        self._hockey_html = parser.get_ice_hockey(self, hockey_url=self.hockey_url)

        req = re.compile('\\n')
        team = []
        for i in self._hockey_html.findAll('span', attrs={'class': "team-name"}):
            team.append(req.sub('', i.text))

        team = team[10:]

        team_1, team_2 = parser.binary_team(all_teams=team)

        all_factor = []
        for factor in self._hockey_html.findAll('a', attrs={'data-is-fctc': "0"}):
            all_factor.append(factor.span.text)

        all_factor = all_factor[25:]

        bets = []
        count = 0
        temp = []

        for bet in all_factor:
            if count in [2, 3, 4]:
                temp.append(bet)

            count += 1

            if count == 5:
                bets.append(temp)
                count = 0
                temp = []
                continue

        hockey_bets = pd.DataFrame({'team1': team_1,
                                    'team2': team_2,
                                    'bets': bets[0:len(team_1)]})

        return hockey_bets

    def get_tennis(self):
        self.tennis_url = 'https://www.betfair.com/sport/tennis'
        self._tennis_html = parser.get_tennis(self, tennis_url=self.tennis_url)

        req = re.compile('\\n')
        team_1 = []
        for i in self._tennis_html.findAll('span', attrs={'class': "home-team-name"}):
            team_1.append(req.sub('', i.text))

        team_2 = []
        for i in self._tennis_html.findAll('span', attrs={'class': "away-team-name"}):
            team_2.append(req.sub('', i.text))

        all_factor = []
        for factor in self._tennis_html.findAll('a', attrs={'data-is-fctc': "0"}):
            all_factor.append(factor.span.text)

        bets = []
        count = 0
        temp = []

        for bet in all_factor:
            if count in [0, 1]:
                temp.append(bet)

            count += 1

            if count == 2:
                bets.append(temp)
                count = 0
                temp = []
                continue



        tennis_bets = pd.DataFrame({'team1': team_1,
                                      'team2': team_2,
                                      'bets': bets[0:len(team_1)]})
        # return tennis_bets
        print(tennis_bets)





ld = betfair()
ld.get_tennis()