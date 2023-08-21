# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
# Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить
# честный жребий и определить, кто будет делать очередной модуль нового курса.
# Формат входных данных
# На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или
# "бумага". На первой строке записан выбор Тимура, на второй – выбор Руслана.
# Формат выходных данных
# Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, Руслан или
# же они сыграют вничью.
# Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает бумаге,
# а ножницы побеждают бумагу.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# камень
# бумага
# Sample Output 1:
#
# Руслан
# Sample Input 2:
#
# камень
# камень
# Sample Output 2:
#
# ничья
# Sample Input 3:
#
# камень
# ножницы
# Sample Output 3:
#
# Тимур


def game_stone_scissors_paper():
    while True:
        print('Выберите три варианта: камень, ножницы, бумага!!!')
        Timur = input('Выбирает Тимур - ')
        Ruslan = input('Выбирает Руслан - ')


        return win(Timur, Ruslan)


def score(a):
    score_Timur = 0
    score_Ruslan = 0
    total_score = 0

    if a == 'Тимур':
        score_Timur += 1
        total_score += 1

    if a == 'Руслан':
        score_Ruslan += 1
        total_score += 1

    if a == 'ничья':
        total_score -= 1

    print(f'Тимур - {score_Timur}, Руслан - {score_Ruslan}')
    return game_stone_scissors_paper()




def win(Timur, Ruslan):
    stone = 'камень'
    paper = 'бумага'
    scissors = 'ножницы'
    draw = 'ничья'
    if Timur == stone and Ruslan == scissors:
        return score('Тимур')
    elif Timur == stone and Ruslan == paper:
        return score('Руслан')
    elif Timur == paper and Ruslan == stone:
        return score('Тимур')
    elif Timur == paper and Ruslan == scissors:
        return score('Руслан')
    elif Timur == scissors and Ruslan == paper:
        return score('Тимур')
    elif Timur == scissors and Ruslan == stone:
        return score('Руслан')
    else:
        return score(draw)


game_stone_scissors_paper()
