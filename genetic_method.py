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
    fitness = 0

    def __init__(self):
        pass

    def __init__(self, genes):
        # Bot constructor - creates 'genes sequence' of a particular Bot
        # конструктор Bot - создает "последовательность генов" для отдельного бота
        for i in range(len(genes)+1):
            self._genes[i] = genes[i]

    def __init__(self, number_of_genes, max_value, min_value, target, eps):
        # Bot constructor overload - creates 'genes' for a bot in random manner
        # перегрузка конструктора Bot - создает "гены" для ботов рандомно
        self._target = target
        self._eps = eps

        for i in range(number_of_genes+1):
            __x_value = random.random()
            self._genes = max_value * __x_value + (1 - __x_value) * min_value

    def get_fitness(self):
        # Check if bot`s genes meet conditions of precision (eps)
        # Проверка, подходит ли набор генов бота для нужной точности
        fitness = abs(self._genes[0] + 2 * self._genes[1] + 3 * self._genes[3] + 4 * self._genes[4] - self._target)
        if fitness <= self._eps:
            self.success = True
        return fitness

    def mutation(self):
        # mutate bot - change genes of one a little
        # мутация бота - немножко меняются значения его генов
        __r_value = random.random(10)
        __p_value = random.random(100)

        for i in range(self.number_of_genes + 1):
            self._genes[i] = self._genes[i] * (1 - pow(-1, __r_value) * __p_value / 1000)

    def selection(self, father_bot):
        # interbreed two bots (mamas'n'papas) to create a new one
        # скрестить двух ботов (папа и мама), чтобы получить нового

        _father_bot = father_bot #_myfather=Bot(self.genes)
        _child_bot = Bot(self._genes) #_myfather.assign_bot(_father_bot)

        _separation_mark = random.random(len(self._genes))
        _child_bot.target = self.target
        _child_bot.eps = self.eps
        _child_bot.success = False

        if _separation_mark == 0:
            _separation_mark = 1

        if _separation_mark == len(self._genes):
            _separation_mark = len(self._genes) - 1

        for i in range(_separation_mark + 1):
            _child_bot.genes[i] = self._genes[i]

        for i in range(_separation_mark + 2 , len(_father_bot.genes) + 1):
            _child_bot.genes[i] = _father_bot.genes[i]

        child_bot = _child_bot
        return child_bot

    def assign_bot(self, jango_fett_bot):
        # bot colning - assigning parameters of Jango-bot to clone bot
        # 200'000 units are ready with a million more on a way
        # клонирование бота - присвоение значений параметров Джанго-бота клонам
        # 200000 единиц уже готовы, миллион на подходе
        self._target = jango_fett_bot._target
        self.fitness = jango_fett_bot.fitness
        self.success = jango_fett_bot.success
        self._eps = jango_fett_bot._eps

        for i in range(len(jango_fett_bot._genes) + 1):
            self._genes[i] = jango_fett_bot._genes[i]

    def dead(self):
        # kill a bot
        # убивает бота
        for i in range(self.number_of_genes + 1):
            self._genes[i] = -1

        self.get_fitness.fitness = -1
        _success = False
        _eps = 0


class Population:

    _max_age: int = 0
    _number_of_good: int = 0
    bots = []
    winner_bot: Bot

    def __init__(self, count_bots, max_age, number_of_genes, max_value, min_value, number_of_good, target, eps):
        # create a population of bots
        # создает стадо ботов
        _number_of_good = number_of_good
        _max_age = max_age
        for i in range(count_bots):
            self.bots.append(Bot(number_of_genes, max_value, min_value, target, eps))

    def dead_population(self):
        # kill the whole population of bots. Not just the man but the women and the children too
        # убить все стадо ботов. Не только мужчин,но и женщин, и детей тоже
        for i in range(self._number_of_good, len(self.bots) + 1):
            self.bots[i].dead()

    def mutation_population(self):
        # mutate bots of population
        # мутация стада ботов
        for i in range(self._number_of_good, len(self.bots) + 1):
            self.bots[i].mutation()

    def evolution_chamber(self):
        __result = False
        __all_fitness = 0
        __bot_fitness = []

        for i in range(len(self.bots) + 1):
            __bot_fitness[i] = self.bots[i].get_fitness

        for i in range(len(self.bots) + 1):
            if not self.bots[i].success:
                __all_fitness = __all_fitness + 1 / __bot_fitness[i]
            else:
                __result = True
                self.winner_bot.assign_bot(self.bots[i])
                return __result

        for i in range(len(self.bots) + 1):
            self.bots[i].fitness = 1 / __bot_fitness[i] / __all_fitness

        self.sort_fitness()
        self.dead_population()
        self.mutation_population()
        self.resurrection_population()

    def execute_population(self):
        __result: Bot = Bot(1, 1, 1, 1, 0.1)

        for i in range(1, self._max_age + 1):
            if self.evolution_chamber:
                __result.assign_bot(self.winner_bot)
                return __result

        __result.assign_bot(self.bots[0])
        return __result

    def resurrection_population(self):
        for i in range(self._number_of_good, len(self.bots) + 1):
            __x_value = random.random(self._number_of_good - 1)
            __y_value = random.random(self._number_of_good - 1)

            self.bots[i].assign_bot(self.bots[__x_value].Selection(self.bots[__y_value]))

    def sort_fitness(self):
        _bot = Bot()
        _m = len(self.bots)
        for i in range(_m):
            for j in range(_m - i - 2):
                if self.bots[j].fitness < self.bots[j+1].fitness:
                    _bot.assign_bot(self.bots[j])
                    self.bots[j].assign_bot(self.bots[j+1])
                    self.bots[j+1].assign_bot(_bot)


popul = Population(1000, 50, 4, 30, 0, 200, 0, pow(10, -5))

popul.execute_population()
