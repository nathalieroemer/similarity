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

class inv_quest(Page):
    def is_displayed(self):
        return self.participant.vars['passed_quest'] == 0 and self.participant.vars['list_is_empty'] == 1 and self.participant.vars['testq'] == 2

    form_model = 'player'
    form_fields = [
        'gender',
        'english',
        'english_prof',
        'stereotypes',
        'chance_bonus',
        'risk_pref',
        'comp'
    ]

    def before_next_page(self):
        self.player.participant.vars['passed_quest'] = 1

        self.player.payoff = self.participant.vars['payoff']

class Results(Page):
    def is_displayed(self):
        return self.participant.vars['passed_quest'] == 1 or self.participant.vars['testq'] != 2
        # Is shown when the participant passed the experiment (questionnaire) or didn't pass the attention check.


page_sequence = [inv_quest, Results]
