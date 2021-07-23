from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class p1_Welcome(Page):
    pass


class p2_YourTask(Page):
    pass

class p3_AttentionCheck(Page):
    form_model = 'player'
    form_fields = ['testq']

    def before_next_page(self):
        # The first question is already set in this app as it determines the next page, which is the first page of the
        # next app. It is stored in a participant variable so we can access it in the next app.
        # The number for the first question is the number of the first element in the list:
        first_quest = self.participant.vars['quest_list'][0]
        # The element which determines the next question is removed from the list so no page can be shown more than
        # once.
        del self.participant.vars['quest_list'][0]
        # The number for the first question is stored in a participant variable:
        self.participant.vars['first_quest'] = first_quest
        print(
            self.participant.vars['quest_list'],
            first_quest
        )

        self.participant.vars['testq'] = self.player.testq

page_sequence = [p1_Welcome, p2_YourTask, p3_AttentionCheck]