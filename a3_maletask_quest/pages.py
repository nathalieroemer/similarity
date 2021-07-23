from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class PromotionInstr(Page):
    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1



class Promotion(Page):
    form_model = 'player'
    form_fields = ['promotion']

    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1

class BeliefCorrectQ(Page):
    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1

class Promotion_other(Page):
    form_model = 'player'
    form_fields = [
        'promo6scale',
        'promo100scale',
        'application',
        'success'
    ]

    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1


class Questionnaire(Page):
    form_model = 'player'
    form_fields = [
        'colorb',
        'native',
        'eng_prof',
        'difficult',
        'stereotypes',
        'bonus_chance',
        'prom_quality',
        'risk_pref',
        'competition'
    ]

    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1

page_sequence = [
    PromotionInstr,
    Promotion,
    BeliefCorrectQ,
    Promotion_other,
    Questionnaire,
    ]
