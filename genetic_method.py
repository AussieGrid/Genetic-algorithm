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
    _genes = []

    def __init__(self):
        pass

    def __init__(self, genes):
        """Bot constructor - 'genes sequence' of a particular Bot created by a User"""
        """конструктор Bot - созданная Пользователем "последовательность генов" для отдельного бота"""

        self._genes = genes[:]

    def __init__(self, number_of_genes, max_value, min_value, target, eps):
        """ Bot constructor overload - creates 'genes' for a bot in random manner"""
        """ перегрузка конструктора Bot - создает "гены" для ботов рандомно"""

        self._target = target
        self._eps = eps

        for i in range(number_of_genes):
            __x_value = random.random()
            self._genes[i] = max_value * __x_value + (1 - __x_value) * min_value

    def get_fitness(self):
        """ Calculates fitness and checks if bot`s genes meet conditions of precision (eps)"""
        """ Расчет разности между значением уравнения с генами и целью и Проверка, подходит ли набор генов бота для нужной точности"""

        fitness = abs(self._genes[0] + 2 * self._genes[1] + 3 * self._genes[3] + 4 * self._genes[4] - self._target)
        if fitness <= self._eps:
            self.success = True
        return fitness

    def mutation(self):
        """ mutate bot - change genes of one a little"""
        """ мутация бота - немножко меняются значения его генов"""

        __r_value = random.random(10)
        __p_value = random.random(100)

        for i in range(self.number_of_genes):
            self._genes[i] = self._genes[i] * (1 - pow(-1, __r_value) * __p_value / 1000)

    def selection(self, father_bot):
        """ interbreed two bots (mamas'n'papas) to create a new one"""
        """ скрестить двух ботов (папа и мама), чтобы получить нового"""

        _father_bot = father_bot #_myfather=Bot(self.genes)
        _child_bot = Bot(self._genes) #_myfather.assign_bot(_father_bot)

        _separation_mark = random.random(len(self._genes))
        _child_bot._target = self._target
        _child_bot._eps = self._eps
        _child_bot.success = False

        if _separation_mark == 0:
            _separation_mark = 1

        if _separation_mark == len(self._genes):
            _separation_mark = len(self._genes) - 1

        for i in range(_separation_mark):
            _child_bot._genes[i] = self._genes[i]

        for i in range(_separation_mark, len(_father_bot.genes)):
            _child_bot._genes[i] = _father_bot.genes[i]

        child_bot = _child_bot
        return child_bot

    def assign_bot(self, jango_fett_bot):
        """ bot colning - assigning parameters of Jango-bot to clone bot"""
        """ 200'000 units are ready with a million more on a way"""
        """ клонирование бота - присвоение значений параметров Джанго-бота клонам"""
        """ 200000 единиц уже готовы, миллион на подходе"""

        self._target = jango_fett_bot._target
        self.fitness = jango_fett_bot.fitness
        self.success = jango_fett_bot.success
        self._eps = jango_fett_bot._eps

        for i in range(len(jango_fett_bot._genes)):
            self._genes[i] = jango_fett_bot._genes[i]

    def dead(self):
        """ kill a bot"""
        """ убивает бота"""

        for i in range(self.number_of_genes):
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
        """ create a population of bots"""
        """ создает стадо ботов"""

        _number_of_good = number_of_good
        _max_age = max_age

        for i in range(count_bots):
            self.bots.append(Bot(number_of_genes, max_value, min_value, target, eps))

    def genocide_population(self):
        """ kill the whole population of bots. Not just the man but the women and the children too"""
        """ убить все стадо ботов. Не только мужчин,но и женщин, и детей тоже"""

        for i in range(self._number_of_good, len(self.bots)):
            self.bots[i].dead()

    def mutation_population(self):
        """ mutate 'good' bots in population"""
        """ мутация "хороших" ботов из стада"""

        for i in range(self._number_of_good, len(self.bots)):
            self.bots[i].mutation()

    def evolution_chamber(self):
        """ Calculates new fitness for population than sort them, kills weak ones, mutate strong and repopulate with stronk children"""
        """ Расчитывает новый fitness, потом убивает слабых ботов, мутирует оставшихся и восстанавливает стадо с помощью сильных детей"""

        __result = False
        __all_fitness = 0
        __bot_fitness = []

        for i in range(len(self.bots)):
            __bot_fitness[i] = self.bots[i].get_fitness # тут может быть ошибка - попробовть через append

        for i in range(len(self.bots)):
            if not self.bots[i].success:
                __all_fitness = __all_fitness + 1 / __bot_fitness[i]
            else:
                __result = True
                self.winner_bot.assign_bot(self.bots[i])
                return __result # переместить в конец метода?

        for i in range(len(self.bots)):
            self.bots[i].fitness = 1 / __bot_fitness[i] / __all_fitness

        self.sort_fitness()
        self.genocide_population()
        self.mutation_population()
        self.resurrection_population()

    def execute_population(self):
        __result: Bot = Bot(4, 1, 1, 1, 0.1)

        for i in range(1, self._max_age):
            if self.evolution_chamber:
                __result.assign_bot(self.winner_bot)
                return __result

        __result.assign_bot(self.bots[0])
        return __result

    def resurrection_population(self):
        for i in range(self._number_of_good, len(self.bots)):
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
