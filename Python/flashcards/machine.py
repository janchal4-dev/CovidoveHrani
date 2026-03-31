class Quizz:

    def __init__(self,question_list, lang_choice):
        self.quest_num = 0
        self.question_list = question_list
        self.player_score = 0
        self.lang_choice = lang_choice
        self.wrong_answer_list = []

    def next_question(self):
        self.topical_question = self.question_list[self.quest_num]
        self.quest_num +=1
        if self.lang_choice == "word_cz":
            player_answer = input(f'Otázka číslo {self.quest_num}: " {self.topical_question.word_cz}": ').lower()
            self.pc_answer = self.topical_question.word_en
        elif self.lang_choice == "word_en":
            player_answer = input(f'Otázka číslo {self.quest_num}: " {self.topical_question.word_en}": ').lower()
            self.pc_answer = self.topical_question.word_cz

        
        self.quest_checker = self.question_checker(player_answer, self.pc_answer, self.quest_num)
        # print(self.quest_checker)
        if  self.quest_checker != None:
            self.wrong_answer_list.append(self.quest_checker)
        # print(self.wrong_answer_list)
        
    def question_supervisor(self):
        if self.quest_num < len(self.question_list):
            return True
        else:
            return False
    def question_checker(self, player,pc, quest_num):
        if pc == player:
            print("R")
        else:
            if self.lang_choice == "word_cz":
                print(f'F, right answer: "{self.topical_question.word_en}"')
                return(self.topical_question.word_cz)
            elif self.lang_choice == "word_en":
                print(f'F, right answer: "{self.topical_question.word_cz}"')
                return(self.topical_question.word_en)




        # def next_question(self):
        # self.topical_question = self.question_list[self.quest_num]
        # self.quest_num +=1
        # if self.lang_choice == "word_cz":
        #     player_answer = input(f'Otázka číslo {self.quest_num}: " {self.topical_question.word_cz}": ').lower()
        #     self.pc_answer = self.topical_question.word_en
        # elif self.lang_choice == "word_en":
        #     player_answer = input(f'Otázka číslo {self.quest_num}: " {self.topical_question.word_en}": ').lower()
        #     self.pc_answer = self.topical_question.word_cz

        # self.question_checker(player_answer, self.pc_answer)