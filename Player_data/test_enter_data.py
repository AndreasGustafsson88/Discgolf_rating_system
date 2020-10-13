from unittest import TestCase
from Classes.players import Player


class TestInputs(TestCase):

    def test_course_exists(self):
        andreas = Player("Andreas", "Gustafsson")
        andreas.enter_data("Krokhol Disc Golf Course Krokhol Regular Layout", [65])
        self.assertTrue(len(andreas.player_scores) == 1)

    def test_course_doesnt_exists(self):
        andreas = Player("Andreas", "Gustafsson")
        self.assertRaises(KeyError, andreas.enter_data, "Krokhol Disc Golf Bana Vanlig Layout", [65])

    def test_false_score_input(self):
        andreas = Player("Andreas", "Gustafsson")
        self.assertRaises(ValueError, andreas.enter_data, "Krokhol Disc Golf Course Krokhol Regular Layout", [126])

    def empty_score_input(self):
        andreas = Player("Andreas", "Gustafsson")
        self.assertRaises(ValueError, andreas.enter_data, "Krokhol Disc Golf Course Krokhol Regular Layout", [])

    def test_limit_score_input(self):
        andreas = Player("Andreas", "Gustafsson")
        andreas.enter_data("Krokhol Disc Golf Course Krokhol Regular Layout", [125])
        self.assertTrue(len(andreas.player_scores) == 1)

    def test_false_score_input_below(self):
        andreas = Player("Andreas", "Gustafsson")
        self.assertRaises(ValueError, andreas.enter_data, "Krokhol Disc Golf Course Krokhol Regular Layout", [34])

    def test_limit_score_input_lower(self):
        andreas = Player("Andreas", "Gustafsson")
        andreas.enter_data("Krokhol Disc Golf Course Krokhol Regular Layout", [35])
        self.assertTrue(len(andreas.player_scores) == 1)

    def test_multiple_input(self):
        andreas = Player("Andreas", "Gustafsson")
        andreas.enter_data("Krokhol Disc Golf Course Krokhol Regular Layout", [i for i in range(55, 115)])
        self.assertTrue(len(andreas.player_scores) == 60)

    def test_int_input_as_course(self):
        andreas = Player("Andreas", "Gustafsson")
        self.assertRaises(KeyError, andreas.enter_data, 1, [65])

    def test_str_input_as_result(self):
        andreas = Player("Andreas", "Gustafsson")
        self.assertRaises(ValueError, andreas.enter_data, "Krokhol Disc Golf Course Krokhol Regular Layout", "hej")

    def test_int_str_input_as_result(self):
        andreas = Player("Andreas", "Gustafsson")
        self.assertRaises(ValueError, andreas.enter_data, "Krokhol Disc Golf Course Krokhol Regular Layout", [65, 75, "Hej"])