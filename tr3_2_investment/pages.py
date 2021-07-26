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

        #print(self.participant.vars['treat'])
        #print(self.participant.vars['list'])

        # generate list of male and female obs
        all_male_obs = []
        all_female_obs = []

        for x in self.participant.vars['list']:
            if self.session.vars['female'][x] == 1:
                all_female_obs.append(x)
            else:
                all_male_obs.append(x)

        #print("count obs list", self.session.vars['count_obs_p'])

        if self.participant.vars['treat'] == "verbal_only":
            min_num_obs = min(self.session.vars['count_obs_p'])
            print("min number of obs", min_num_obs)
            #define empty list that gets filled with observations for which conditions are fulfilled (gender and how many dec were made)
            obs_left_male = []
            obs_left_female = []

            # fill list with entries of participant list that contains random shuffled indices of the dataset and only take entries of the specific gender and that were not in more than X decisions already
            for x in self.participant.vars['list']:
                if self.session.vars['count_obs_p'][x] == min_num_obs and self.session.vars['female'][x] == 0:
                    obs_left_male.append(x)

            for x in self.participant.vars['list']:
                if self.session.vars['count_obs_p'][x] == min_num_obs and self.session.vars['female'][x] != 0:
                    obs_left_female.append(x)

            #print("ideas with min num of obs left male", obs_left_male)
            #print("ideas with min num of obs left female", obs_left_female)

            # if there are entries in the list with obs that fulfill conditions above, take the first entry as the first picture
            if len(obs_left_male) != 0:
                male_obs = obs_left_male[0]
            # if not, take any male obs
            else:
                male_obs = all_male_obs[0]

            if len(obs_left_female) != 0:
                female_obs = obs_left_female[0]
            else:
                female_obs = all_female_obs[0]

        elif self.participant.vars['treat'] == "verbal_only_b":
            min_num_obs = min(self.session.vars['count_obs_pb'])
            print("min number of obs", min_num_obs)
            #define empty list that gets filled with observations for which conditions are fulfilled (gender and how many dec were made)
            obs_left_male = []
            obs_left_female = []

            # fill list with entries of participant list that contains random shuffled indices of the dataset and only take entries of the specific gender and that were not in more than X decisions already
            for x in self.participant.vars['list']:
                if self.session.vars['count_obs_pb'][x] == min_num_obs and self.session.vars['female'][x] == 0:
                    obs_left_male.append(x)

            for x in self.participant.vars['list']:
                if self.session.vars['count_obs_pb'][x] == min_num_obs and self.session.vars['female'][x] != 0:
                    obs_left_female.append(x)

            #print("obs left male promo only blind", obs_left_male)
            #print("obs left female promo only blind", obs_left_female)

            # if there are entries in the list with obs that fulfill conditions above, take the first entry as the first picture
            if len(obs_left_male) != 0:
                male_obs = obs_left_male[0]
            # if not, take any male obs
            else:
                male_obs = all_male_obs[0]

            if len(obs_left_female) != 0:
                female_obs = obs_left_female[0]
            else:
                female_obs = all_female_obs[0]

        elif self.participant.vars['treat'] == "no_info":
            min_num_obs = min(self.session.vars['count_obs_ni'])

            #define empty list that gets filled with observations for which conditions are fulfilled (gender and how many dec were made)
            obs_left_male = []
            obs_left_female = []

            # fill list with entries of participant list that contains random shuffled indices of the dataset and only take entries of the specific gender and that were not in more than X decisions already
            for x in self.participant.vars['list']:
                if self.session.vars['count_obs_ni'][x] == min_num_obs and self.session.vars['female'][x] == 0:
                    obs_left_male.append(x)

            for x in self.participant.vars['list']:
                if self.session.vars['count_obs_ni'][x] == min_num_obs and self.session.vars['female'][x] != 0:
                    obs_left_female.append(x)

            #print("obs left male no info", obs_left_male)
            #print("obs left female no info", obs_left_female)

            # if there are entries in the list with obs that fulfill conditions above, take the first entry as the first picture
            if len(obs_left_male) != 0:
                male_obs = obs_left_male[0]
            # if not, take any male obs
            else:
                male_obs = all_male_obs[0]

            if len(obs_left_female) != 0:
                female_obs = obs_left_female[0]
            else:
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

        promo_verbal_1 = self.session.vars['promo_verbal'][x]
        promo_verbal_2 = self.session.vars['promo_verbal'][y]

        #print("num and sex of obs x", self.player.x, female_1, word_1)
        #print("num and sex of obs y", self.player.y, female_2, word_2)

        chose_1 = self.player.chose_1
        chose_2 = self.player.chose_2

        return dict(
            promo_verbal_1=promo_verbal_1,
            promo_verbal_2=promo_verbal_2,
            chose_1=chose_1,
            chose_2=chose_2,
            female_1=female_1,
            female_2=female_2
                )

    def before_next_page(self):
        # in which round is player?
        self.player.roundcount = self.participant.vars['count_round']
        self.participant.vars['count_round'] = self.participant.vars['count_round'] + 1

        if self.participant.vars['treat'] == "verbal_only":
            self.player.obs_num1 = int(self.session.vars['count_obs_p'][self.player.x])
            self.player.obs_num2 = int(self.session.vars['count_obs_p'][self.player.y])
            self.session.vars['count_obs_p'][self.player.x] = self.session.vars['count_obs_p'][self.player.x] + 1
            self.session.vars['count_obs_p'][self.player.y] = self.session.vars['count_obs_p'][self.player.y] + 1

        elif self.participant.vars['treat'] == "verbal_only_b":
            self.player.obs_num1 = int(self.session.vars['count_obs_pb'][self.player.x])
            self.player.obs_num2 = int(self.session.vars['count_obs_pb'][self.player.y])
            self.session.vars['count_obs_pb'][self.player.x] = self.session.vars['count_obs_pb'][self.player.x] + 1
            self.session.vars['count_obs_pb'][self.player.y] = self.session.vars['count_obs_pb'][self.player.y] + 1


        elif self.participant.vars['treat'] == "no_info":
            self.player.obs_num1 = int(self.session.vars['count_obs_ni'][self.player.x])
            self.player.obs_num2 = int(self.session.vars['count_obs_ni'][self.player.y])
            self.session.vars['count_obs_ni'][self.player.x] = self.session.vars['count_obs_ni'][self.player.x] + 1
            self.session.vars['count_obs_ni'][self.player.y] = self.session.vars['count_obs_ni'][self.player.y] + 1

        self.player.id1 = str(self.session.vars['id'][self.player.x])
        self.player.id2 = str(self.session.vars['id'][self.player.y])

        self.player.performance1 = int(self.session.vars['performance'][self.player.x])
        self.player.performance2 = int(self.session.vars['performance'][self.player.y])

        self.player.female_1 = int(self.session.vars['female'][self.player.x])
        self.player.female_2 = int(self.session.vars['female'][self.player.y])

        if self.player.chose_1 == 1 and self.player.performance1 > self.player.performance2:
            self.player.right_choice = 1
        elif self.player.chose_1 == 1 and self.player.performance1 < self.player.performance2:
            self.player.right_choice = 0
        elif self.player.chose_2 == 1 and self.player.performance2 > self.player.performance1:
            self.player.right_choice = 1
        elif self.player.chose_2 == 1 and self.player.performance2 < self.player.performance1:
            self.player.right_choice = 0
        elif self.player.performance1 == self.player.performance2:
            self.player.equal_performance = 1

        # hier werden die ersten zwei einträge der liste entfernt
        # del self.participant.vars['list'][:2]
        # Mit dem remove-Befehl werden die Einträge mit den entsprechenden Werten ohne Kenntnis des Indexes entfernt.
        self.participant.vars['list'].remove(self.player.x)
        self.participant.vars['list'].remove(self.player.y)

        list = self.participant.vars['list']

        # adjust to 21 since then the 20th round already took place

        if len(list) == 0 or self.participant.vars['count_round'] == 21:
            self.participant.vars['list_is_empty'] = 1
            # The following code sets the payoff in the last round after completion of the questionnaire
            # based on a random round.
            # print(self.player.roundcount)
            randomround = randint(1, 20)
            print("round number is", randomround)
            print("right choice?", self.player.in_round(randomround).right_choice)
            if self.player.in_round(randomround).right_choice == 1:
                self.player.payoff = 1.50
            elif self.player.in_round(randomround).equal_performance == 1:
                self.player.payoff = 0.75
            else:
                self.player.payoff = 0
            self.participant.vars['payoff'] = self.player.payoff
            print("payoff", self.player.payoff)
        else:
            self.participant.vars['list_is_empty'] = 0

page_sequence = [investment]
