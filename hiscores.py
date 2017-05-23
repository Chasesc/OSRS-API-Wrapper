#! python3.5

import const
import re
import urllib.request
from skill import Skill

class Hiscores(object):

	def __init__(self, username):
		self.username = username
		self.update()

	def update(self):
		self._api_response = self._get_api_data()
		self._set_data()

	def _get_api_data(self):
		try:
			url = urllib.request.urlopen("%s%s" % (const.HISCORE_URL, self.username))
		except urllib.error.HTTPError:
			raise Exception("Unable to find %s in the hiscores." % self.username)

		data = url.read()
		url.close()

		skill_data = list(map(int, re.findall(r'\d+', str(data))))
		return skill_data

	def _set_data(self):
		offset = 3 # first three are rank, total level, and total xp

		self.rank, self.total_level, self.total_xp = [self._api_response[i] for i in range(offset)]		

		self.skills = []
		for i in range(1, const.SKILLS_AMT + 1):
			index = offset * i
			skill, rank, level, xp = (const.SKILLS[i - 1],
									  self._api_response[index],
									  self._api_response[index + 1],
									  self._api_response[index + 2])

			self.skills.append(Skill(skill, rank, level, xp))


	def __str__(self):
		return '\n'.join(str(skill) for skill in self.skills)




def main():
	test = Hiscores('Zezima')
	print(str(test))

if __name__ == '__main__':
	main()