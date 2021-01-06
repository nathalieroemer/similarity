from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'a3_results'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def set_payoffs(self):
        for p in self.get_players():
            p.payoff = p.participant.vars['investment']
            #if p.role == 'innovator':
            #    p.payoff = 5  # p.participant.vars['investment']
            #elif p.role == 'investor':
            #    p.payoff = 0


class Player(BasePlayer):

    def role(self):
        if self.participant.vars['investor'] == 1:
            return 'investor'
        else:
            return 'innovator'
