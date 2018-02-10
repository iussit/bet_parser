from parser import parser
import re
import pandas as pd

class sporting_bet(parser):
    def __init__(self, url='https://sports.sportingbet.com/en/sports'):
        self.url = url
        parser.__init__(self, self.url)

    def get_team(self, name_teams):
        all_teams =[]
        team_1 = []
        team_2 = []

        for name_team in name_teams:
            for name in name_team.findAll('span'):
                name = re.sub(' -', '', name.text)
                all_teams.append(name)

        i = 0
        for team in all_teams:
            if i % 2 == 0:
                team_1.append(team)
            else:
                team_2.append(team)
            i += 1

        return team_1, team_2




    def get_factor_1x2(self, factors, line):
        factor = []

        reg = re.compile('[^\d.\d]*')

        for x in factors:
            factor.append(reg.sub('', x.text))

        parser.get_factor_1x2(factors=factor, line=line)

    def get_football(self):
        date = parser.get_date()

        self.football_url = 'https://sports.sportingbet.com/en/sports#dateFilter=' + date + '&sportId=4'
        self._football_html = parser.get_football(self, football_url=self.football_url)

        team_1, team_2 = sporting_bet.get_team(self, self._football_html.findAll('a',
                                                                                 attrs={'class': "js-mg-tooltip"}))
        factor = sporting_bet.get_factor_1x2(self, self._football_html.findAll('div', attrs={'class': "mg-option-button__option-odds"}),
                                             line=6)
        football_bet = pd.DataFrame({
                                     'date': [date for d in range(len(team_1))],
                                     'team1': team_1,
                                     'team2': team_2,
                                     'bet': factor
                                     })
        return football_bet

    def get_tennis(self):
        date = parser.get_date()

        self.tennis_url = 'https://sports.sportingbet.com/en/sports/5/betting/tennis#sportId=5'
        self._tennis_html = parser.get_tennis(self, tennis_url=self.tennis_url)

        all_team = []
        for team in self._tennis_html.findAll('div', attrs={'class': "mb-option-button__option-name mb-option-button__option-name--odds-4"}):
            all_team.append(team.text)

        team_1, team_2 = parser.binary_team(all_team)

        all_factors = []
        for factors in self._tennis_html.findAll('div', attrs={'class': "mb-option-button__option-odds"}):
            all_factors.append(factors.text)

        factors_1, factors_2 = parser.binary_team(all_factors)

        tennis_bet = pd.DataFrame({'team1': team_1,
                                   'team2': team_2,
                                   'factor1': factors_1,
                                   'factor2': factors_2})

        return tennis_bet


    def get_ice_hockey(self):
        date = parser.get_date()

        self.hockey_url = 'https://sports.sportingbet.com/en/sports/12/betting/ice-hockey#sportId=12'
        self._hockey_html = parser.get_ice_hockey(self, hockey_url=self.hockey_url)

        team_1, team_2 = sporting_bet.get_team(self, self._hockey_html.findAll('a', attrs={'class': "js-mg-tooltip"}))

        factors = sporting_bet.get_factor_1x2(self, self._hockey_html.findAll('div', attrs={'class': "mg-option-button__option-odds"}),
                                              line=3)

        print(factors)

        ice_hockey_bet = pd.DataFrame({
            'team1': team_1,
            'team2': team_2,
            'bet': factors
        })

        # all_team = []
        # for team in self._hockey_html.findAll('div', attrs={'class': "mb-option-button__option-name mb-option-button__option-name--odds-4"}):
        #     # if team.text != 'X':
        #     all_team.append(team.text)
        #
        # print(len(all_team))
        # team_1, team_2 = sporting_bet.binary_team(self, all_team)
        #
        # all_factors = []
        # for factors in self._hockey_html.findAll('div', attrs={'class': "mb-option-button__option-odds"}):
        #     all_factors.append(factors.text)
        #
        # bets = []
        # count = 0
        # temp = []
        #
        # for bet in all_factors:
        #     if count in [0, 1, 2]:
        #         temp.append(bet)
        #
        #     count += 1
        #
        #     if count == 3:
        #         bets.append(temp)
        #         count = 0
        #         temp = []
        #         continue
        #
        # print(len(bets))
        # print(len(team_1))
        # print(len(team_2))
        #
        # ice = pd.DataFrame({'team1:', team_1,
        #                     'team2:', team_2,
        #                     'factor', bets})

        return ice_hockey_bet









sp = sporting_bet()
print(sp.get_ice_hockey())





