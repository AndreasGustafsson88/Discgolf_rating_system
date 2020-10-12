from unittest import TestCase
from Classes.players import Player


class TestInputs(TestCase):

    def test_course_exists(self):
        andreas = Player("Andreas", "Gustafsson")
        andreas.enter_data("Krokhol Disc Golf Course Krokhol Regular Layout", [65])
        self.assertTrue(len(andreas.player_scores) > 0)

    def test_false_score_input(self):
        andreas = Player("Andreas", "Gustafsson")
        # andreas.enter_data("Krokhol Disc Golf Course Krokhol Regular Layout", [400])
        self.assertRaises(ValueError, andreas.enter_data, "Krokhol Disc Golf Course Krokhol Regular Layout", [400])


        # Vill testa ett högt värde som score t.ex 400 som false, men det kommer ge mig ett keyerror i get_rating
        # måste jag ta in det i enter_data funktionen som en catch för ett fel?
        # vad är rätt och vcad är fel?

