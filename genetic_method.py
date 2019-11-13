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
        """Конструктор Bot - созданная Пользователем "последовательность генов" для отдельного бота"""

        self._genes = genes[:]

    def __init__(self, number_of_genes, max_value, min_value, target, eps):
        """ Bot constructor overload - creates 'genes' for a bot in random manner"""
        """ Перегрузка конструктора Bot - создает "гены" для ботов рандомно"""

        self._target = target
        self._eps = eps

        for i in range(number_of_genes):
            __x_value = random.random()
            self._genes[i] = max_value * __x_value + (1 - __x_value) * min_value

    def get_fitness(self):
        """ Calculates difference between expression with genes and target then checks if it meets conditions of precision (eps)"""
        """ Расчет разности между выражением с подставленными генами и необходимым значением (целью), 
            и проверка, подходит ли набор генов бота для нужной точности"""

        fitness = abs(self._genes[0] + 2 * self._genes[1] + 3 * self._genes[3] + 4 * self._genes[4] - self._target)
        if fitness <= self._eps:
            self.success = True
        return fitness

    def mutation(self):
        """ Mutate bot - change genes of one a little"""
        """ Мутация бота - немножко меняются значения его генов"""

        __r_value = random.random(10)
        __p_value = random.random(100)

        for i in range(self.number_of_genes):
            self._genes[i] = self._genes[i] * (1 - pow(-1, __r_value) * __p_value / 1000)

    def selection(self, father_bot):
        """ Interbreed two bots (mamas'n'papas) by spliting their genes into 2 pieces each to create a new one"""
        """ Скрестить двух ботов (папа и мама), разрезанием каждого на 2 части, чтобы получить нового"""

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
        """ Bot colning - assigning parameters of Jango-bot to clone bot"""
        """ 200'000 units are ready with a million more on a way"""
        """ Клонирование бота - присвоение значений параметров Джанго-бота клону"""
        """ 200000 единиц уже готовы, миллион на подходе"""

        self._target = jango_fett_bot._target
        self.fitness = jango_fett_bot.fitness
        self.success = jango_fett_bot.success
        self._eps = jango_fett_bot._eps

        for i in range(len(jango_fett_bot._genes)):
            self._genes[i] = jango_fett_bot._genes[i]

    def dead(self):
        """ Kill a bot"""
        """ Убивает бота"""

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
        """ Create a population of bots"""
        """ Создает стадо ботов"""

        _number_of_good = number_of_good
        _max_age = max_age

        for i in range(count_bots):
            self.bots.append(Bot(number_of_genes, max_value, min_value, target, eps))

    def genocide_population(self):
        """ Kill the whole population of bots. Not just the man but the women and the children too"""
        """ Убить все стадо ботов. Не только мужчин,но и женщин, и детей тоже"""

        for i in range(self._number_of_good, len(self.bots)):
            self.bots[i].dead()

    def mutation_population(self):
        """ Mutate 'good' bots in population"""
        """ Мутация "хороших" ботов из стада"""

        for i in range(self._number_of_good):
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
        """ Returns winner bot - the one with the best fitness which meets eps"""
        """ Возвращает бота-победителя: у него наименьший fitness и он проходит по точности"""

        __result: Bot = Bot(4, 1, 1, 1, 0.1)

        for i in range(1, self._max_age):
            if self.evolution_chamber:
                __result.assign_bot(self.winner_bot)
                return __result

        __result.assign_bot(self.bots[0])
        return __result

    def resurrection_population(self):
        """ Creates children of survived strong bots and puts them in the remaining slots of population"""
        """ Создает детей выживших сильных ботов и забивает их в свободные слоты стада"""

        for i in range(self._number_of_good, len(self.bots)):
            __x_value = random.random(self._number_of_good - 1)
            __y_value = random.random(self._number_of_good - 1)

            self.bots[i].assign_bot(self.bots[__x_value].Selection(self.bots[__y_value]))

    def sort_fitness(self):
        """ Sort bots population with bubble-method in ascending order (fitness)"""
        """ Сортирует пузырьком ботов в стаде по возрастанию (по fitness)"""

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
