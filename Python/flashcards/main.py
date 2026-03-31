import random
from data import word_data
from engine import cardEngine
from machine import Quizz

li=[]
for x in range(0, len(word_data)):
    li.append(x)
#converting list to set so that to remove repeating elements
se=set(li)
li=list(se)
#we use this list to get non-repeating elemets
# print(random.sample(li,len(word_data)))
random_list = random.sample(li,len(word_data))
word_data_shuffeled = []
# print(random_list)
for x in range(0, len(word_data)):
    order = random_list[x]
    # print(order)
    # question_data_new_order.append((Question((question_data[order]["text"]),(question_data[order]["answer"]))))
    word_data_shuffeled.append((word_data[order]))
# print(word_data_shuffeled)
question_list = []

for one_word in word_data_shuffeled:
    word_cz = one_word["word_cz"]
    word_en = one_word["word_en"]
    # print(f"{word_cz} - {word_en}")
    next_question = cardEngine(word_cz, word_en)
    question_list.append(next_question)

# print(question_list)



# lang_choice = "word_cz"
lang_choice = input("EN / CZ: ").lower()
if lang_choice == "en" or lang_choice == "english":
    lang_choice = "word_en"
elif lang_choice == "cz" or lang_choice == "czech":
    lang_choice = "word_cz"

quiz = Quizz(question_list, lang_choice)

while quiz.question_supervisor() == True:
    quiz.next_question()

# print(quiz.wrong_answer_list)

while len(quiz.wrong_answer_list) > 0:
    new_word_data = []
    for one_word_count in range(0,len(quiz.wrong_answer_list)):
        #################
        for wrong_word in word_data:
            if wrong_word[lang_choice] == quiz.wrong_answer_list[one_word_count]:
            # if wrong_word["word_cz"] == "tradiční":
                # print("Found student:", wrong_word)
                new_word_data.append(wrong_word)
                break
            # else:
            #     print("Student not found")       
        #################

    # print(new_word_data)
    question_list0 = []

    for one_word in new_word_data:
        word_cz = one_word["word_cz"]
        word_en = one_word["word_en"]
        # print(f"{word_cz} - {word_en}")
        next_question = cardEngine(word_cz, word_en)
        question_list0.append(next_question)


    quiz = Quizz(question_list0, lang_choice)

    while quiz.question_supervisor() == True:
        quiz.next_question()        