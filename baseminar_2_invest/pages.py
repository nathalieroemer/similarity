from django.contrib.staticfiles.templatetags.staticfiles import static
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import io
import os
import re
import base64
#from PIL import Image
from django.conf import settings
from os import path
from uuid import uuid4
dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
from random import seed
from random import randint
import random
from itertools import takewhile

class investment(Page):
    form_model = 'player'
    form_fields = ['chose_1', 'chose_2']

    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 0

    def vars_for_template(self):
        x = self.participant.vars['list'][0]
        y = self.participant.vars['list'][1]

        self.player.x = self.participant.vars['list'][0]
        self.player.y = self.participant.vars['list'][1]

        female_1 = self.session.vars['female'][x]
        female_2 = self.session.vars['female'][y]

        pic_1 = self.session.vars['image_data'][x]
        pic_2 = self.session.vars['image_data'][y]

        promo_verbal_1 = self.session.vars['promo_verbal'][x]
        promo_verbal_2 = self.session.vars['promo_verbal'][y]

        word_1 = self.session.vars['words'][x]
        word_2 = self.session.vars['words'][y]

        self.player.value_1 = int(self.session.vars['value'][self.player.x])
        self.player.value_2 = int(self.session.vars['value'][self.player.y])

        chose_1 = self.player.chose_1
        chose_2 = self.player.chose_2

        return dict(
            photo1=pic_1,
            photo2=pic_2,
            promo_verbal_1=promo_verbal_1,
            promo_verbal_2=promo_verbal_2,
            chose_1=chose_1,
            chose_2=chose_2,
            word_1=word_1,
            word_2=word_2,
            female_1=female_1,
            female_2=female_2
                )

    def before_next_page(self):
        # in which round is player?
        self.player.roundcount = self.participant.vars['count_round']
        self.participant.vars['count_round'] = self.participant.vars['count_round'] + 1

        if self.player.chose_1 == 1 and self.player.value_1 > self.player.value_2:
            self.player.right_choice = 1
        elif self.player.chose_1 == 1 and self.player.value_1 < self.player.value_2:
            self.player.right_choice = 0
        elif self.player.chose_2 == 1 and self.player.value_2 > self.player.value_1:
            self.player.right_choice = 1
        elif self.player.chose_2 == 1 and self.player.value_2 < self.player.value_1:
            self.player.right_choice = 0
        elif self.player.value_1 == self.player.value_2:
            self.player.equal_value = 1

        self.participant.vars['list'].remove(self.player.x)
        self.participant.vars['list'].remove(self.player.y)

        list = self.participant.vars['list']
        if len(list) == 0 or self.participant.vars['count_round'] == 1:
            self.participant.vars['list_is_empty'] = 1
        else:
            self.participant.vars['list_is_empty'] = 0

        #print("empty", self.participant.vars['list_is_empty'])
        #print("quest", self.participant.vars['passed_quest'])


class inv_quest(Page):
    def is_displayed(self):
        return self.participant.vars['passed_quest'] == 0 and self.participant.vars['list_is_empty'] == 1

    form_model = 'player'
    form_fields = [
        'gender',
        'name'
    ]

    def before_next_page(self):
        self.player.participant.vars['passed_quest'] = 1
        # The following code sets the payoff in the last round after completion of the questionnaire
        # based on a random round.
        #print(self.player.roundcount)
        randomround = randint(1, self.player.roundcount)
        #print("round number is", randomround)
        if self.player.in_round(randomround).right_choice == 1:
            self.player.payoff = 5.00
            self.player.pay_euro = 5
        else:
            self.player.payoff = 0
            self.player.pay_euro = 0


class Results(Page):
    def is_displayed(self):
        return self.participant.vars['passed_quest'] == 1


page_sequence = [investment, inv_quest, Results]
