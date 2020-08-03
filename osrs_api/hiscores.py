import re
import urllib.request

from collections import namedtuple
from urllib.parse import quote

from . import const
from .skill import Skill

Minigame = namedtuple("Minigame", ["name", "rank", "score"])
Boss = namedtuple("Boss", ["name", "rank", "kills"])


class Hiscores(object):
    def __init__(self, username, account_type=None):
        self.username = username
        self._type = account_type
        self._api_response = None

        if self._type is None:
            self._find_account_type() # _type is set inside _find_account_type

        self.rank, self.total_level, self.total_xp = -1, -1, -1

        self.skills = {}
        self.minigames = {}
        self.bosses = {}

        self.update()

    def update(self):
        # In the default case (account_type=None), we already have this information. We don't need to do it again
        if self._api_response is None:
            self._api_response = self._get_api_data()
        self._set_data()
        self._api_response = None

    @property
    def _url(self):
        return const.BASE_URL + self._type.value + "?player="

    def _find_account_type(self):
        '''
        The RS API does not tell you the account type, so we have to find out here.
        Try in the order of special type -> normal account, so we find the correct type
        '''

        for possible_type in reversed(const.AccountType.normal_types()):
            try:
                self._type = possible_type
                self._api_response = self._get_api_data()
                return
            except:
                pass

        self._raise_bad_username()

    def _raise_bad_username(self):
        raise Exception("Unable to find %s in the hiscores." % self.username)

    def _get_api_data(self):
        try:
            safe_url = "%s%s" % (self._url, quote(self.username))
            url = urllib.request.urlopen(safe_url)
        except urllib.error.HTTPError:
            self._raise_bad_username()

        data = url.read()
        url.close()

        return data.decode().split("\n")

    def _set_data(self):
        """
        The RS api is not documented and is given as a list of numbers on multiple lines. These lines are:

        "overall_rank, total_level, total_xp"
        "skill_rank, skill_level, skill_xp" for all skills
        "minigame_rank, minigame_score" for all minigames
        "boss_rank, boss_kills" for all bosses

        If a player is unranked for any of these categories, there is a value of -1 in that row.

        example: https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws?player=lelalt
        """

        # Get all the skills, minigames, or bosses
        def _get_api_chunk(cls, *, names, start_index):
            """
            cls: Skill, Minigame, or Boss - Type of the chunk 
            names: List[str] - a list of all the (Skill, Minigame, or Boss) names in the order the API returns them.
                   (const.SKILLS, const.MINIGAMES, or const.BOSSES)
            start_index: The index into self._api_response where the chunk begins
            """

            chunk = {}

            for i, name in enumerate(names, start=start_index):
                if name == const.UNUSED_OR_UNKNOWN:
                    continue

                # The API only returns integers
                row_data = [int(col) for col in self._api_response[i].split(",")]

                chunk[name] = cls(name, *row_data)

            return chunk

        overall_data = self._api_response[0].split(",")
        self.rank, self.total_level, self.total_xp = (
            int(overall_data[0]),
            int(overall_data[1]),
            int(overall_data[2]),
        )

        self.skills = _get_api_chunk(Skill, names=const.SKILLS, start_index=1)
        self.minigames = _get_api_chunk(
            Minigame, names=const.MINIGAMES, start_index=1 + const.SKILLS_AMT
        )
        self.bosses = _get_api_chunk(
            Boss,
            names=const.BOSSES,
            start_index=1 + const.SKILLS_AMT + const.MINIGAMES_AMT,
        )

    def max_skill(self, method="xp"):
        ninf = -float("inf")
        max_skill = Skill("attack", xp=ninf, rank=ninf)
        for skill in self.skills.values():
            if getattr(skill, method) > getattr(max_skill, method):
                max_skill = skill

        return max_skill

    def min_skill(self, method="xp"):
        inf = float("inf")
        min_skill = Skill("attack", xp=inf, rank=inf)
        for skill in self.skills.values():
            if getattr(skill, method) < getattr(min_skill, method):
                min_skill = skill

        return min_skill

    def closest_skill(self):
        closest = Skill("attack")
        closest_xp_tnl = float("inf")
        for skill in self.skills.values():
            if skill.xp_tnl() < closest_xp_tnl:
                closest_xp_tnl, closest = skill.xp_tnl(), skill

        return closest

    def skills_under(self, value, method="level"):
        def under(hiscore, s):
            return getattr(hiscore.skills[s], method) < value

        return self.filter(under)

    def skills_over(self, value, method="level"):
        def over(hiscore, s):
            return getattr(hiscore.skills[s], method) > value

        return self.filter(over)

    def filter(self, predicate):
        return {s: self.skills[s] for s in self.skills if predicate(self, s)}

    def __str__(self):
        attrs = [
            ("Rank", self.rank),
            ("Total Level", self.total_level),
            ("Total XP", self.total_xp),
        ]
        return (
            "\n".join(f"{name}: {str(item)}" for name, item in attrs)
            + "\n"
            + "\n".join(str(self.skills[skill]) for skill in self.skills)
        )

    def __repr__(self):
        return f"Hiscores({self.username}, type={self._type.name})"

    # ==
    def __eq__(self, other):
        if isinstance(other, Hiscores):
            return self.rank == other.rank
        return False

    # !=
    def __ne__(self, other):
        equals = self.__eq__(other)
        return not equals

    # <
    def __lt__(self, other):
        if isinstance(other, Hiscores):
            return self.rank > other.rank  # flipped because lower rank is better
        return False

    # >
    def __gt__(self, other):
        if isinstance(other, Hiscores):
            return self.rank < other.rank  # flipped because lower rank is better
        return False

    # <=
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    # >=
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)


def main():
    top = Hiscores("Lelalt", const.AccountType.IRONMAN)
    print(str(top))


if __name__ == "__main__":
    main()
