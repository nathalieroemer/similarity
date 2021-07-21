from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class q1_AR1(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        # In the first round, the random question is determined by the value of the participant variable, whose value
        # was assigned to it at the end of the previous app. A participant var had to be used to pass it between apps.
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        # In later rounds, the random question is determined by the value of "next_rand_quest" from the previous round,
        # which has a new value at the end of every round (see below).
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        # The page is displayed if the number for the random question is 1.
        return self.player.rand_quest == 1

    def before_next_page(self):
        # Before proceeding to the next page, the variable 'right' is assigned the value 1 if the participant answered correctly and 0 otherwise
        if self.player.answer == 3: # the right option in this case would have been option 3, therefore if he/she answered with option 3, the answer was right
            self.player.right = 1
        elif self.player.answer != 3: # if he or she did select a different answer option, the answer was wrong
            self.player.right = 0

        # Before the next page, the next value from the question list (a participant var) is assigned to the variable
        # next_rand_quest, which will determine the value of the rand_quest in the next round.
        # We cannot just let this assignment happen in a is_displayed method, we have to use next_rand_quest, as this
        # determines, which page will be shown. is_displayed is only executed, when the next page is already shown.
        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            # The element is deleted after it determines the next question:
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1

        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q2_AR2(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 2

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q3_AR3(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 3

    def before_next_page(self):
        if self.player.answer == 3:
            self.player.right = 1
        elif self.player.answer != 3:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q4_AR4(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 4

    def before_next_page(self):
        if self.player.answer == 4:
            self.player.right = 1
        elif self.player.answer != 4:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q5_AO1(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 5

    def vars_for_template(self):
        return dict(
            # Mit .format wird der spezifizierte Wert in den Platzhalter überführt, also {}.
            objects1="{}.png".format("objects1"),
        )

    def before_next_page(self):
        if self.player.answer == 2:
            self.player.right = 1
        elif self.player.answer != 2:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q6_AO2(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 6

    def vars_for_template(self):
        return dict(
            # Mit .format wird der spezifizierte Wert in den Platzhalter überführt, also {}.
            objects2="{}.png".format("objects2"),
        )

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q7_AO3(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 7

    def vars_for_template(self):
        return dict(
            # Mit .format wird der spezifizierte Wert in den Platzhalter überführt, also {}.
            objects3="{}.png".format("objects3"),
        )

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q8_AO4(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 8

    def vars_for_template(self):
        return dict(
            # Mit .format wird der spezifizierte Wert in den Platzhalter überführt, also {}.
            objects4="{}.png".format("objects4"),
        )

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )




class q9_GS1(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 9

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q10_GS2(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 10

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q11_GS3(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 11

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q12_GS4(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 12

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )



class q13_MK1(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 13

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q14_MK2(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 14

    def before_next_page(self):
        if self.player.answer == 2:
            self.player.right = 1
        elif self.player.answer != 2:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q15_MK3(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 15

    def before_next_page(self):
        if self.player.answer == 2:
            self.player.right = 1
        elif self.player.answer != 2:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q16_MK4(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 16

    def before_next_page(self):
        if self.player.answer == 2:
            self.player.right = 1
        elif self.player.answer != 2:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )



class q17_MC1(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 17

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q18_MC2(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 18

    def before_next_page(self):
        if self.player.answer == 2:
            self.player.right = 1
        elif self.player.answer != 2:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q19_MC3(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 19

    def before_next_page(self):
        if self.player.answer == 1:
            self.player.right = 1
        elif self.player.answer != 1:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )


class q20_MC4(Page):
    form_model = 'player'
    form_fields = [
        'answer'
    ]

    def is_displayed(self):
        if self.round_number == 1:
            self.player.rand_quest = self.participant.vars['first_quest']
        elif self.round_number > 1:
            self.player.rand_quest = self.player.in_round(self.round_number - 1).next_rand_quest

        return self.player.rand_quest == 20

    def before_next_page(self):
        if self.player.answer == 4:
            self.player.right = 1
        elif self.player.answer != 4:
            self.player.right = 0

        if self.participant.vars['list_empty'] != 1:
            self.player.next_rand_quest = self.participant.vars['quest_list'][0]
            del self.participant.vars['quest_list'][0]
            q_l = self.participant.vars['quest_list']
            if len(q_l) == 0:
                self.participant.vars['list_empty'] = 1
        print(
            self.participant.vars['quest_list'],
            self.player.next_rand_quest
        )

class Results(Page):
    def is_displayed(self):
        return self.round_number == 20


page_sequence = [
    q1_AR1,
    q2_AR2,
    q3_AR3,
    q4_AR4,
    q5_AO1,
    q6_AO2,
    q7_AO3,
    q8_AO4,
    q9_GS1,
    q10_GS2,
    q11_GS3,
    q12_GS4,
    q13_MK1,
    q14_MK2,
    q15_MK3,
    q16_MK4,
    q17_MC1,
    q18_MC2,
    q19_MC3,
    q20_MC4,
    Results]
