from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):
    form_model = 'player'
    title_text = "Einen Moment bitte."
    body_text = "Bitte warten Sie auf die anderen TeilnehmerInnen."

    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [ResultsWaitPage, Results]
