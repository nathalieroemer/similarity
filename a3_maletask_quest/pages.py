from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class PromotionInstr(Page):
    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1 and self.participant.vars['testq'] ==2



class Promotion(Page):
    form_model = 'player'
    form_fields = ['promotion']

    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1 and self.participant.vars['testq'] ==2

class Promotion_other(Page):
    form_model = 'player'
    form_fields = [
        'promo6scale',
        'promo100scale',
    ]

    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1 and self.participant.vars['testq'] ==2


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
        'competition',
        'belief_correct_q'
    ]

    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1

class FinalPage(Page):
    def is_displayed(self):
        return self.participant.vars['list_empty'] == 1 or self.participant.vars['testq'] !=2

page_sequence = [
    PromotionInstr,
    Promotion,
    Promotion_other,
    Questionnaire,
    FinalPage
    ]
