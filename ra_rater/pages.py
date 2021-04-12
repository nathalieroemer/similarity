from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    def is_displayed(self):
        return self.participant.vars['passed_instr'] == 0


class Instructions(Page):
    def is_displayed(self):
        return self.participant.vars['passed_instr'] == 0

    def before_next_page(self):
        self.participant.vars['passed_instr'] = 1


class Task(Page):
    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 0

    form_model = 'player'
    form_fields = ['word_guess']

    def vars_for_template(self):

        x = self.participant.vars['list'][0]

        pic = self.session.vars['image_data'][x]
        word = self.session.vars['words'][x]
        self.player.x = x

        return dict(
            photo=pic,
            word=word,
            )

    def before_next_page(self):
        self.player.photo_id = str(self.session.vars['photo_id'][self.player.x])

        self.player.word = str(self.session.vars['words'][self.player.x])
        if self.player.word_guess != None:
            if self.player.word_guess.lower() == self.player.word.lower():
            # .lower() method converts all uppercase characters to lowercase ones so the comparison is case insensitive
            # Alternatively, use .casefold() which is more aggressive as it also converts, e.g., ß to ss.
                self.player.payoff = 0.1
            else:
                self.player.payoff = 0
            # payoff of each round gets automatically stored in self.participant.payoff
        else:
            self.player.payoff=0

        self.participant.vars['list'].remove(self.player.x)
        self.participant.vars['count_round'] = self.participant.vars['count_round'] + 1

        list = self.participant.vars['list']
        # print(list)
        print(len(list))
        print("round count is", self.participant.vars['count_round'] )

        if self.participant.vars['count_round'] == 50 or len(list) == 0:
            self.participant.vars['list_is_empty'] = 1
        else:
            self.participant.vars['list_is_empty'] = 0


class Results(Page):
    def is_displayed(self):
        return self.participant.vars['list_is_empty'] == 1 or self.round_number == Constants.num_rounds

    def vars_for_template(self):
        final_payoff = self.participant.payoff_plus_participation_fee()

        return dict(
            final_payoff=final_payoff,
        )


page_sequence = [Welcome, Instructions, Task, Results]
