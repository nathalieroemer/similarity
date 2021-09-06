from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from random import randint
# import math


class Task(Page):
    form_model = 'player'
    form_fields = [
        'c_term',
        'c_material',
        'c_display',
        'c_overall'
    ]

    def vars_for_template(self):
        x = self.participant.vars['list'][0]
        y = self.participant.vars['list'][1]

        i = 1
        while self.session.vars['treatments'][x] == self.session.vars['treatments'][y]:
            y = self.participant.vars['list'][1 + i]
            i = i + 1

        self.player.x = x
        self.player.y = y

        print(str(self.session.vars['image_data2'][x]))
        print(str(self.session.vars['image_data2'][y]))

        if str(self.session.vars['image_data2'][x]) == 'nan':
            pic1 = str(self.session.vars['image_data1'][x])
        else:
            pic1 = str(self.session.vars['image_data1'][x]) + str(self.session.vars['image_data2'][x])

        if str(self.session.vars['image_data2'][y]) == 'nan':
            pic2 = str(self.session.vars['image_data1'][y])
        else:
            pic2 = str(self.session.vars['image_data1'][y]) + str(self.session.vars['image_data2'][y])

        word1 = self.session.vars['words'][x]
        word2 = self.session.vars['words'][y]

        return dict(
            pic1=pic1,
            pic2=pic2,
            word1=word1,
            word2=word2,
            erdbeere="{}.jpg".format("Erdbeere"),
            geschenk="{}.jpg".format("Geschenk"),
            kamel="{}.jpg".format("Kamel"),
            schere="{}.jpg".format("schere"),
            schwein="{}.jpg".format("Schwein"),
            tasse="{}.jpg".format("Tasse")
        )

    def before_next_page(self):
        self.player.photo_id1 = str(self.session.vars['photo_ids'][self.player.x])
        self.player.photo_id2 = str(self.session.vars['photo_ids'][self.player.y])

        self.player.word1 = str(self.session.vars['words'][self.player.x])
        self.player.word2 = str(self.session.vars['words'][self.player.y])

        self.player.treatment1 = int(self.session.vars['treatments'][self.player.x])
        self.player.treatment2 = int(self.session.vars['treatments'][self.player.y])

        self.participant.vars['list'].remove(self.player.x)
        self.participant.vars['list'].remove(self.player.y)


class Break(Page):
    def is_displayed(self):
        return self.round_number in [2, 4, 6, 8]


class Finish(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [Task, Break, Finish]
