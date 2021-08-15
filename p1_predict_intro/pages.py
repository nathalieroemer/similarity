from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass


class Instructions(Page):
    pass


class Instructions2(Page):
    def vars_for_template(self):
        return dict(
            figure1="{}.png".format("examplebar"),
        )


class AttentionCheck(Page):
    form_model = 'player'
    form_fields = [
        'test'
    ]

    def before_next_page(self):
        # To use the result from the attention check in the next app it is saved in a participant variable.
        self.participant.vars['test'] = self.player.test


page_sequence = [Welcome, Instructions, Instructions2, AttentionCheck]
