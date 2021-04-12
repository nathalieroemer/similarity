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
        return self.participant.vars['list_is_empty'] == 0 and self.participant.vars['testq'] == 2

    def vars_for_template(self):
        global female_obs, male_obs
        l = [1, 2]
        r = random.choice(l)


        # generate list of male and female obs
        all_male_obs = []
        all_female_obs = []

        for x in self.participant.vars['list']:
            if self.session.vars['female'][x] == 1:
                all_female_obs.append(x)
            else:
                all_male_obs.append(x)
        print(all_male_obs)
        print(all_female_obs)

        male_obs = all_male_obs[0]
        female_obs = all_female_obs[0]

        if r == 1:
            y = female_obs
            x = male_obs
        else:
            y = male_obs
            x = female_obs

        self.player.x = x
        self.player.y = y

        female_1 = self.session.vars['female'][x]
        female_2 = self.session.vars['female'][y]

        pic_1 = self.session.vars['image_data'][x]
        pic_2 = self.session.vars['image_data'][y]

        chose_1 = self.player.chose_1
        chose_2 = self.player.chose_2

        return dict(
            photo1=pic_1,
            photo2=pic_2,
            chose_1=chose_1,
            chose_2=chose_2,
            female_1=female_1,
            female_2=female_2
                )

    def before_next_page(self):
        # in which round is player?
        self.player.roundcount = self.participant.vars['count_round']
        self.participant.vars['count_round'] = self.participant.vars['count_round'] + 1

        self.player.photo_id_1 = str(self.session.vars['photo_id'][self.player.x])
        self.player.photo_id_2 = str(self.session.vars['photo_id'][self.player.y])


        self.player.female_1 = int(self.session.vars['female'][self.player.x])
        self.player.female_2 = int(self.session.vars['female'][self.player.y])

   #     for p in self.player.get_others_in_subsession():
    #        if p.participant.vars['photoid'] == self.session.vars['images'][0]:
   #             p.participant.vars['investment'] = investment_in_1
   #             p.investment = investment_in_1
   #         elif p.participant.vars['photoid'] == self.session.vars['images'][1]:
   #             p.participant.vars['investment'] = investment_in_2
    #            p.investment = investment_in_2
            # print(p.participant.vars['investment'])

        # hier werden die ersten zwei einträge der liste entfernt
        # del self.participant.vars['list'][:2]
        # Mit dem remove-Befehl werden die Einträge mit den entsprechenden Werten ohne Kenntnis des Indexes entfernt.
        self.participant.vars['list'].remove(self.player.x)
        self.participant.vars['list'].remove(self.player.y)


        list = self.participant.vars['list']
        print(list)
        print(len(list))
        # adjust to 51 since then the 50th round already took place
        if len(list) == 0 or self.participant.vars['count_round'] == 35:
            self.participant.vars['list_is_empty'] = 1
        else:
            self.participant.vars['list_is_empty'] = 0

        print("empty", self.participant.vars['list_is_empty'])
        print("quest", self.participant.vars['passed_quest'])


class inv_quest(Page):
    def is_displayed(self):
        return self.participant.vars['passed_quest'] == 0 and self.participant.vars['list_is_empty'] == 1 and self.participant.vars['testq'] == 2

    form_model = 'player'
    form_fields = [
        'gender',
        'english',
        'english_prof',
        'colourb',
        'stereotypes',
        'chance_bonus',
        'risk_pref',
        'comp'
    ]

    def before_next_page(self):
        self.player.participant.vars['passed_quest'] = 1



class Results(Page):
    def is_displayed(self):
        return self.participant.vars['passed_quest'] == 1 or self.participant.vars['testq'] != 2
        # Is shown when the participant passed the experiment (questionnaire) or didn't pass the attention check.


page_sequence = [investment, inv_quest, Results]
