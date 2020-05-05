from . import const


class Skill(object):
    def __init__(self, name, rank=0, level=0, xp=0):
        if name not in const.SKILLS:
            raise Exception("%s is not a valid skill." % name)

        self.name = name
        self.rank = rank
        self.level = level
        self.xp = xp

    # TODO: Add virtual levels to the XP_TABLE
    # xp to next level
    def xp_tnl(self):
        if self.level >= 99: 
            return 0 # already maxed, no real next level
        return const.XP_TABLE[self.level] - self.xp

    def xp_to(self, level):
        if level > 99:
            return 0 # same reason as above.
        return const.XP_TABLE[level - 1] - self.xp

    def __str__(self):
        return f"Skill(name={self.name}, rank={self.rank}, level={self.level}, xp={self.xp})"

    def __repr__(self):
        return self.__str__()
