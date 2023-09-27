import unittest
from unittest.mock import Mock
from percentages import bereken_succes_percentage


class TestSpaceX(unittest.TestCase):
    def test_bereken_succes_percentage(self):
        api_data = [
            {"launch_success": True},
            {"launch_success": False},
            {"launch_success": True},
            {"launch_success": True},
            {"launch_success": False},
        ]

        # Mock the spacex_connectie.spacex_connection function
        spacex_connectie_mock = Mock(return_value=api_data)

        # Call the function with the mock data
        success_percentage = bereken_succes_percentage(spacex_connectie_mock())

        # Calculate the expected success percentage manually
        expected_percentage = (3 / 5) * 100

        # Assert that the function's result matches the expected result
        self.assertEqual(success_percentage, expected_percentage)

    def test_bereken_succes_percentage_alles_goed(self):
        api_data = [
            {"launch_success": True},
            {"launch_success": True},
            {"launch_success": True},
            {"launch_success": True},
            {"launch_success": True},
        ]
        # Mock the spacex_connectie.spacex_connection function
        spacex_connectie_mock = Mock(return_value=api_data)

        # Call the function with the mock data
        success_percentage = bereken_succes_percentage(spacex_connectie_mock())

        # Calculate the expected success percentage manually
        self.assertEqual(success_percentage, 100)

    def test_bereken_succes_percentage_alles_fout(self):
        api_data = [
            {"launch_success": False},
            {"launch_success": False},
            {"launch_success": False},
            {"launch_success": False},
            {"launch_success": False},
        ]
        # Mock the spacex_connectie.spacex_connection function
        spacex_connectie_mock = Mock(return_value=api_data)

        # Call the function with the mock data
        success_percentage = bereken_succes_percentage(spacex_connectie_mock())

        # Calculate the expected success percentage manually
        self.assertEqual(success_percentage, 0)

    def test_bereken_succes_percentage_geen_data(self):
        api_data = []
        # Mock the spacex_connectie.spacex_connection function
        spacex_connectie_mock = Mock(return_value=api_data)

        # Call the function with the mock data
        success_percentage = bereken_succes_percentage(spacex_connectie_mock())

        # Calculate the expected success percentage manually
        self.assertEqual(success_percentage, 0)


if __name__ == '__main__':
    unittest.main()
