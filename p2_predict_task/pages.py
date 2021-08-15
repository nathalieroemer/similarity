from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from random import randint


class Task(Page):
    form_model = 'player'
    form_fields = [
        'g_answers',
        'g_fem'
    ]

    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 0 and self.participant.vars['test'] == 2

    def vars_for_template(self):
        x = self.participant.vars['list'][0]
        promo = self.session.vars['promo'][x]
        female = self.session.vars['female'][x]
        answers = randint(0, 20)
        self.player.hilfe = answers

        return dict(
            promo=promo,
            female=female,
            answers=answers
        )

    def before_next_page(self):
        # Participant and session variables are accessed to safe them as player variables for this round:
        self.player.x = self.participant.vars['list'][0]
        self.player.promo = str(self.session.vars['promo'][self.player.x])

        # TODO: Die Variablennamne müssen entsprechend dem neuen Datensatz angepasst werden. Für die "answers"-Variable
        #  wird derzeit noch eine zufällige Zahl zwischen 0 und 20 genutzt (siehe vars_for_template).
        #self.player.answers = self.session.vars['recog'][self.player.x]
        self.player.answers = self.player.hilfe
        self.player.female = self.session.vars['female'][self.player.x]

        # payoff/bonus for guess of correctly answered questions
        self.player.dev_ans = abs(self.player.answers - self.player.g_answers)
        if self.player.dev_ans <= 1:
            self.player.ans_pay = 4.00
        if self.player.dev_ans == 2:
            self.player.ans_pay = 2.00
        if self.player.dev_ans > 2:
            self.player.ans_pay = 0

        # payoff/bonus for guess of gender
        rand_num1 = randint(0, 100)
        rand_num2 = randint(0, 100)
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
            self.player.payoff = self.player.in_round(randomround).ans_pay + self.player.in_round(randomround).gen_pay
            self.participant.vars['end'] = 1


class Results(Page):
    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 1 or self.round_number == Constants.num_rounds \
               or self.participant.vars['test'] != 2


page_sequence = [Task, Results]
