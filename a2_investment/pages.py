from django.contrib.staticfiles.templatetags.staticfiles import static
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import io
import os
import re
import base64
# from PIL import Image
from django.conf import settings
from os import path
from uuid import uuid4
dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
from random import seed
from random import randint


class investment(Page):
    form_model = 'player'
    form_fields = ['chose_1', 'chose_2']

    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 0

    def vars_for_template(self):

        x = self.participant.vars['list'][0]
        y = self.participant.vars['list'][1]

        pic_1 = self.session.vars['image_data'][x]
        pic_2 = self.session.vars['image_data'][y]

        promo_verbal_1 = self.session.vars['promo_verbal'][x]
        promo_verbal_2 = self.session.vars['promo_verbal'][y]

        promo_rec_1 = self.session.vars['promo_rec'][x]
        promo_rec_2 = self.session.vars['promo_rec'][y]

        promo_orig_1 = self.session.vars['promo_orig'][x]
        promo_orig_2 = self.session.vars['promo_orig'][y]

        chose_1 = self.player.chose_1
        chose_2 = self.player.chose_2

        return dict(
            photo1=pic_1,
            photo2=pic_2,
            promo_verbal_1=promo_verbal_1,
            promo_verbal_2=promo_verbal_2,
            promo_rec_1=promo_rec_1,
            promo_rec_2=promo_rec_2,
            promo_orig_1=promo_orig_1,
            promo_orig_2=promo_orig_2,
            chose_1=chose_1,
            chose_2=chose_2)

    def before_next_page(self):

        self.player.x = self.participant.vars['list'][0]
        self.player.y = self.participant.vars['list'][1]

        self.player.photo_id_1 = str(self.session.vars['photo_id'][self.player.x])
        self.player.photo_id_2 = str(self.session.vars['photo_id'][self.player.y])

        print("this is orig", self.session.vars['orig'][self.player.x])
        print("this is recog", self.session.vars['recog'][self.player.x])
        print("this is value", self.session.vars['value'][self.player.x])

        self.player.orig_1 = self.session.vars['orig'][self.player.x]
        self.player.orig_2 = self.session.vars['orig'][self.player.y]

        self.player.recog_1 = self.session.vars['recog'][self.player.x]
        self.player.recog_2 = self.session.vars['recog'][self.player.y]

        self.player.value_1 = self.session.vars['value'][self.player.x]
        self.player.value_2 = self.session.vars['value'][self.player.y]

        self.player.word_1 = str(self.session.vars['words'][self.player.x])
        self.player.word_2 = str(self.session.vars['words'][self.player.y])

        if self.player.chose_1 == 1 and self.player.value_1 > self.player.value_2:
            self.player.right_choice = 1
        elif self.player.chose_1 == 1 and self.player.value_1 < self.player.value_2:
            self.player.right_choice = 0
        elif self.player.chose_2 == 1 and self.player.value_2 > self.player.value_1:
            self.player.right_choice = 1
        elif self.player.chose_2 == 1 and self.player.value_2 < self.player.value_1:
            self.player.right_choice = 0


   #     for p in self.player.get_others_in_subsession():
    #        if p.participant.vars['photoid'] == self.session.vars['images'][0]:
   #             p.participant.vars['investment'] = investment_in_1
   #             p.investment = investment_in_1
   #         elif p.participant.vars['photoid'] == self.session.vars['images'][1]:
   #             p.participant.vars['investment'] = investment_in_2
    #            p.investment = investment_in_2
            # print(p.participant.vars['investment'])

        del self.participant.vars['list'][:2]
        list = self.participant.vars['list']
        print(list)
        print(len(list))

        if len(list) == 0:
            self.participant.vars['list_is_empty'] = 1
        else:
            self.participant.vars['list_is_empty'] = 0

        print("empty", self.participant.vars['list_is_empty'])
        print("quest", self.participant.vars['passed_quest'])


class inv_quest(Page):
    def is_displayed(self):
        return self.participant.vars['passed_quest'] == 0 and self.participant.vars['list_is_empty'] == 1

    form_model = 'player'
    form_fields = [
    #    'gender',
    #    'english',
        'english_prof',
        'colourb',
        'stereotypes',
        'chance_bonus',
        'risk_pref',
        'comp'
    ]

    def before_next_page(self):
        self.player.participant.vars['passed_quest'] = 1


page_sequence = [investment, inv_quest]
