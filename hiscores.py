#! python3.5

import const
import re
import urllib.request
from skill import Skill

class Hiscores(object):

	def __init__(self, username, type = const.AccountType.NORMAL):
		self.username = username
		self._url = const.BASE_URL + const.HISCORE_URLS[type] + "?player="
		self.update()

	def update(self):
		self._api_response = self._get_api_data()
		self._set_data()

	def _get_api_data(self):
		try:
			url = urllib.request.urlopen("%s%s" % (self._url, self.username))
		except urllib.error.HTTPError:
			raise Exception("Unable to find %s in the hiscores." % self.username)

		data = url.read()
		url.close()

		skill_data = list(map(int, re.findall(r'\d+', str(data))))
		return skill_data

	def _set_data(self):
		offset = 3 # first three are rank, total level, and total xp

		self.rank, self.total_level, self.total_xp = [self._api_response[i] for i in range(offset)]		

		self.skills = {}
		for i in range(1, const.SKILLS_AMT + 1):
			index = offset * i
			skill, rank, level, xp = (const.SKILLS[i - 1],
									  self._api_response[index],
									  self._api_response[index + 1],
									  self._api_response[index + 2])

			self.skills[skill] = Skill(skill, rank, level, xp)

	def max_skill(self, method = 'xp'):
		ninf = -float('inf')
		max_skill = Skill('attack', xp = ninf, rank = ninf)
		for skill in self.skills.values():
			if getattr(skill, method) > getattr(max_skill, method):
				max_skill = skill

		return max_skill

	def min_skill(self, method = 'xp'):
		inf = float('inf')
		min_skill = Skill('attack', xp = inf, rank = inf)
		for skill in self.skills.values():
			if getattr(skill, method) < getattr(min_skill, method):
				min_skill = skill

		return min_skill

	def closest_skill(self):
		closest = Skill('attack')
		closest_xp_tnl = float('inf')
		for skill in self.skills.values():
			if skill.xp_tnl() < closest_xp_tnl:
				closest_xp_tnl, closest = skill.xp_tnl(), skill

		return closest

	def skills_under(self, value, method = 'level'):
		def under(hiscore, s):
			return getattr(hiscore.skills[s], method) < value

		return self.filter(under)

	def skills_over(self, value, method = 'level'):
		def over(hiscore, s):
			return getattr(hiscore.skills[s], method) > value

		return self.filter(over)

	def filter(self, predicate):
		return {s : self.skills[s] for s in self.skills if predicate(self, s)}


	def __str__(self):
		return ('\n'.join(str(item) for item in [self.rank, self.total_level, self.total_xp]) + '\n' +
		        '\n'.join(str(self.skills[skill]) for skill in self.skills))

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
			return self.rank > other.rank # flipped because lower rank is better
		return False

	# >
	def __gt__(self, other):
		if isinstance(other, Hiscores):
			return self.rank < other.rank # flipped because lower rank is better
		return False

	# <=
	def __le__(self, other):
		return self.__eq__(other) or self.__lt__(other)

	# >=
	def __ge__ (self, other):
		return self.__eq__(other) or self.__gt__(other)



def main():
	top = Hiscores('Lelalt', const.AccountType.IRONMAN)
	print(str(top))

if __name__ == '__main__':
	main()