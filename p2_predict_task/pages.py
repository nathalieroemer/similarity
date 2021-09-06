from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from random import randint


class Task(Page):
    form_model = 'player'
    form_fields = [
        'g_score',
        'g_fem'
    ]

    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 0 and self.participant.vars['test'] == 2

    def vars_for_template(self):
        x = self.participant.vars['list'][0]
        promo = self.session.vars['promo'][x]
        # The variables female and score are only displayed for test purposes (shown in Debug info at bottom of page).
        female = self.session.vars['female'][x]
        score = self.session.vars['score'][x]

        return dict(
            promo=promo,
            female=female,
            answers=score
        )

    def before_next_page(self):
        # Participant and session variables are accessed to safe them as player variables for this round:
        self.player.x = self.participant.vars['list'][0]
        self.player.promo = str(self.session.vars['promo'][self.player.x])

        self.player.score = self.session.vars['score'][self.player.x]
        self.player.female = self.session.vars['female'][self.player.x]

        # payoff/bonus for guess of correctly answered questions
        self.player.dev_score = abs(self.player.score - self.player.g_score)
        if self.player.dev_score <= 1:
            self.player.score_pay = 4.00
        if self.player.dev_score == 2:
            self.player.score_pay = 2.00
        if self.player.dev_score > 2:
            self.player.score_pay = 0

        # payoff/bonus for guess of gender
        rand_num1 = randint(0, 100)
        rand_num2 = randint(0, 100)
        print("random num1 is", rand_num1)
        print("random num2 is", rand_num2)
        if (self.player.g_fem >= rand_num1 and self.player.female == 1) or \
                (self.player.g_fem >= rand_num2 and self.player.female == 1):
            self.player.gen_pay = 1.00
        elif (self.player.g_fem < rand_num1 and self.player.female == 0) or \
                (self.player.g_fem < rand_num2 and self.player.female == 0):
            self.player.gen_pay = 1.00
        else:
            self.player.gen_pay = 0

        # The element of the list that was used in this round is deleted from the list:
        del self.participant.vars['list'][:1]
        list = self.participant.vars['list']

        # This code will be executed, when the list is empty or when the max amount of rounds is reached:
        if len(list) == 0 or self.round_number == Constants.num_rounds:
            self.participant.vars['list_is_empty'] = 1
            randomround = randint(1, self.round_number)
            print("random round number is", randomround)
            self.player.payoff = self.player.in_round(randomround).score_pay + self.player.in_round(randomround).gen_pay
            self.participant.vars['end'] = 1


class Results(Page):
    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 1 or self.round_number == Constants.num_rounds \
               or self.participant.vars['test'] != 2


page_sequence = [Task, Results]
