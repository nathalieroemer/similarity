from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from random import randint
import itertools


class Welcome(Page):
    def is_displayed(self):
        return self.participant.vars['passed_instr'] == 0


class Instructions(Page):
    def is_displayed(self):
        return self.participant.vars['passed_instr'] == 0

    def vars_for_template(self):
        return dict(
            material="{}.png".format("material"),
        )


class Instructions2(Page):
    def is_displayed(self):
        return self.participant.vars['passed_instr'] == 0

    def before_next_page(self):
        self.participant.vars['passed_instr'] = 1


class Task(Page):
    form_model = 'player'
    form_fields = ['guess_gender', 'guess_recog', 'guess_orig']

    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 0

    def vars_for_template(self):
        x = self.participant.vars['list'][0]

        promo = self.session.vars['promo'][x]
        word = self.session.vars['words'][x]

        return dict(
            promo=promo,
            word=word,
            )

    def before_next_page(self):
        if self.round_number == 1:
            self.player.roundcount = 1
        elif self.round_number > 1:
            self.player.roundcount = self.player.in_round(self.round_number - 1).roundcount + 1

        self.player.x = self.participant.vars['list'][0]
        self.player.photo_id = str(self.session.vars['photo_id'][self.player.x])

        self.player.word = str(self.session.vars['words'][self.player.x])
        self.player.promo = str(self.session.vars['promo'][self.player.x])

        self.player.orig = self.session.vars['orig'][self.player.x]
        self.player.recog = self.session.vars['recog'][self.player.x]
        self.player.female = self.session.vars['female'][self.player.x]

        if self.player.orig == self.player.guess_orig:
            self.player.orig_pay = 1.00
        else:
            self.player.orig_pay = 0

        if self.player.female == self.player.guess_gender:
            self.player.fem_pay = 1.00
        else:
            self.player.fem_pay = 0

        self.player.dev_recog = abs(self.player.recog - self.player.guess_recog)

        if self.player.dev_recog <= 5:
            self.player.recog_pay = 1.00
        if self.player.dev_recog in range(6,15):
            self.player.recog_pay = 0.50
        if self.player.dev_recog >= 15:
            self.player.recog_pay = 0

        del self.participant.vars['list'][:1]
        list = self.participant.vars['list']
        print(list)
        print(len(list))

        if len(list) == 0:
            self.participant.vars['list_is_empty'] = 1
            print(self.participant.vars['list_is_empty'])
            randomround = randint(1, self.player.roundcount)
            self.player.payoffround = randomround
            print("round number is", randomround)
            self.player.payoff = self.player.in_round(randomround).fem_pay + self.player.in_round(randomround).orig_pay + self.player.in_round(randomround).recog_pay


class Results(Page):
    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 1 or self.round_number == Constants.num_rounds

    def vars_for_template(self):
        final_payoff = self.participant.payoff_plus_participation_fee()

        return dict(
            final_payoff=final_payoff,
        )


page_sequence = [Welcome, Instructions, Instructions2, Task, Results]
