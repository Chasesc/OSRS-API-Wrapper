import unittest

from osrs_api.hiscores import Hiscores
from osrs_api.const import SKILLS_AMT, MINIGAMES_AMT, BOSSES_AMT


class TestHiscore(unittest.TestCase):
    def test_api_length(self):
        """Check to see if the API returns the same number of skills, minigames, and bosses that are mentioned in const.py. If this test fails, the items in const.py need to be updated."""
        score = Hiscores(username="Lelalt")
        expected_num_api_elements = SKILLS_AMT + MINIGAMES_AMT + BOSSES_AMT
        api_data = score._get_api_data()

        # Remove empty string and overall values since they're not used
        len_api_data = len(api_data) - 2

        self.assertEqual(expected_num_api_elements, len_api_data)
