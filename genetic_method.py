# Программа реализует генетический алгоритм
# для решения задач оптимизации и моделирования
# Выполнено во славу святой Омниссии
# да поможет мне Дух Машины
# и убережет от технологической ереси Хаоса
# Deus est Machina
# 0.673.019.M3

import random

class Bot:

    success = False

    def __init__(self, genes = []):
        # Bot constructor - creates 'genes sequence' of a particular Bot
        # конструктор Bot - создает "последовательность генов" для отдельного бота
        for i in range(len(genes)):
            self._genes[i] = genes[i]

    def __init__(self, number_of_genes, max_value, min_value, target, eps):
        # Bot constructor overload - creates 'genes' for a bot in random manner
        # перегрузка конструктора Bot - создает "гены" для ботов рандомно
        self.target = target
        self.eps = eps

        for i in range(number_of_genes):
            _x_value = random.random()
            self._genes = max_value * _x_value + (1 - _x_value) * min_value

    def get_fitness(self):
        # Check if bot`s genes meet conditions of precision (eps)
        # Проверка, подходит ли набор генов бота для нужной точности
        fitness = abs(self._genes[0] + 2 * self._genes[1] + 3 * self._genes[3] + 4 * self._genes[4] - self.target)
        if fitness <= self.eps:
            self.success = True
        return fitness

    def mutation(self):
        # mutate bot - change genes of one a little
        # мутация бота - немножко меняются значения его генов
        _r_value = random(10)
        _p_value = random(100)

        for i in range(self.number_of_genes):
            self._genes[i] = self._genes[i] * (1 - pow(-1, _r_value) * _p_value / 1000)

    def selection(self, father_bot):
        # interbreed two bots (mamas'n'papas) to create a new one
        # скрестить двух ботов (папа и мама), чтобы получить нового

        _father_bot = father_bot #_myfather=Bot(self.genes)
        _child_bot = Bot(self._genes) #_myfather.assign_bot(_father_bot)

        _separation_mark = random(len(self.genes))
        _child_bot.target = self.target
        _child_bot.eps = self.eps
        _child_bot.success = False

        if _separation_mark == 0:
            _separation_mark = 1

        if _separation_mark == len(self._genes):
            _separation_mark = len(self._genes) - 1

        for i in range(_separation_mark):
            _child_bot.genes[i] = self.genes[i]

        for i in range(_separation_mark + 1 , len(_father_bot.genes)):
            _child_bot.genes[i] = _father_bot.genes[i]

        child_bot = _child_bot
        return child_bot

    def assign_bot(self, jango_fett_bot):
        # bot colning - assigning parameters of Jango-bot to clone bot
        # 200'000 units are ready with a million more on a way
        # клонирование бота - присвоение значений параметров Джанго-бота клонам
        # 200000 единиц уже готовы, миллион на подходе
        self.target = jango_fett_bot.target
        self.fitness = jango_fett_bot.fitness
        self.success = jango_fett_bot.success
        self.eps = jango_fett_bot.eps

        for i in range(len(jango_fett_bot.genes)):
            self._genes[i] = jango_fett_bot.genes[i]

    def dead(self):
        # kill a bot
        # убивает бота
        for i in range(self.number_of_genes):
            self.genes[i] = -1

        self.get_fitness.fitness = -1
        _success = False
        _eps = 0

class Population:

    def __init__(self, _count_bots, max_age, _number_of_genes, _max_value, _min_value, number_of_good, _target, _eps):
        # create a population of bots
        # создает стадо ботов
        bots = []
        for i in range(_count_bots):
            bots[i] = Bot(_number_of_genes, _max_value, _min_value, _target, _eps)

    def dead_population(self):
        # kill the whole population of bots. Not just the man but the women and the children too
        # убить все стадо ботов. Не только мужчин,но и женщин, и детей тоже
        for i in range(self.number_of_good, len(self.bots)):
            self.bots[i].dead()

    def mutation_population(self):
        # mutate bots of population
        for i in range(self.number_of_good, len(self.bots)):
            self.bots[i].mutation

    def calculate_age(self):
        result = False
        allfitness = 0
        botfitness = []

        for i in range(len(self.bots)):
            botfitness[i] = self.bots[i].get_fitness

        for i in range(len(self.bots)):
            if not(self.bots[i].success):
                allfitness = allfitness + 1 / botfitness[i]
            else:
                result = True
                self.winner_bot.assign_bot(self.bots[i])

        for i

    def execute_population(self):
        winner_bot = Bot

        for i in range(1, self.max_age):
            if calculate_age:

