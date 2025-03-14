class ColdWeapon:  # Холодное оружие -1-
    pass


class Blade(ColdWeapon):  # Клинковое -2-
    pass


class Stabbing(Blade):  # Колющее -3-
    pass


class Swords(Stabbing):  # Шпаги -4-
    pass


class Dirks(Stabbing):  # Кортинки -4-
    pass


class Stilettos(Stabbing):  # Скилеты -4-
    pass


class FacetedBayonets(Stabbing):  # Граненые штыки -4-
    pass


class Multitooths(Stabbing):  # Многозубцы -4-
    pass


class Chopping(Blade):  # Рубящее -3-
    pass


class Sabers(Chopping):  # Сабли -4-
    pass


class Tesaki(Chopping):  # Тесаки -4-
    pass


class Checkers(Chopping):  # Шашки -4-
    pass


class BattleAxes(Chopping):  # Боевые топоры -4-
    pass


class Poleaxs(Chopping):  # Секиры -4-
    pass


class Berdyshi(Chopping):  # Бердыши -4-
    pass


class Combined(ColdWeapon):  # Комбинированное -2-
    pass


class IDontKnow(Combined):  # Колюще-рубящее, режущее ударно-раздробляющее -3-
    pass


class ToothChains(IDontKnow):  # "Зубастые цепи" -4-
    pass


class KnifeClusters(IDontKnow):  # Кластеры-ножи -4-
    pass


class DaggerKnuckles(IDontKnow):  # Кастеты-кинжалы -4-
    pass


class WhipString(IDontKnow):  # Струна-кистень -4-
    pass


class CombatScourgeDagger(IDontKnow):  # Боевой бич-кинжал -4-
    pass

