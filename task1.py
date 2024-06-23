import random
#условие таково, что тот кто поймал мяч, тот и отвечает на вопрос. 

#ответы и вопросы, которые типо должны выводится
def comp_resp(history):
    resp = [ "Нет",
             "Да",
             "Трудно ответить...наверное нет.",
             "Трудно ответить...наверное да.",
             "Я люблю когда волосатые мужики...",
             "Ты вероятнее всего кринж по жизни, раз уж задаешь подобные вопросы.",]
    return random.choice(resp)

def comp_quest():
    quest = ["Сколько тебе лет?",
             "Как тебя зовут?",
             "Ты лох? (знак вопроса для приличия)",
             "Ты адекватный?",
             "Ты любишь фурри?",]
    return random.choice(quest)

results = {}


#Сама игра
def play_game():
    history = []
    round_number = 1

    while round_number <= 10:
        print(f"Раунд {round_number}:")

#в случае если бросате комп
        print("Компьютер бросает вам мяч...")
        if random.random() <= 0.7:
            print("Вы поймали мяч.")
            print(f"Компьютер: {comp_quest()}")
            response = input("Ваш ответ: ")
        else:
            print("Вы не поймали мяч.")

#в случае если бросает игрок
        print("Теперь ваш ход. Бросьте мяч.")
        print("Вы бросаете...")
        if random.random() <= 0.7:
            print("Компьютер поймал мяч.")
            quest = input("Ваш вопрос: ")
            print(f"Компьютер: {comp_resp(history)}")
        else:
            print("Компьютер не поймал мяч.")

        round_number += 1

    print("\nРезультаты:", results)
    
   


play_game()