import unittest
from datetime import datetime
from collections import defaultdict, Counter
from src.utils.process_data import process_data


class TestProcessData(unittest.TestCase):
    def test_process_data(self):
        # Caso de prueba con una sola línea de tweet
        lines_single_tweet = [
            '{"date": "2022-01-01T12:00:00+00:00", "user": {"username": "user1"}, "text": "Example tweet"}']
        expected_single_tweet = defaultdict(Counter, {datetime(2022, 1, 1).date(): Counter({'user1': 1})})
        self.assertEqual(process_data(lines_single_tweet), expected_single_tweet)

        # Caso de prueba con múltiples líneas de tweets
        lines_multiple_tweets = [
            '{"date": "2022-01-01T12:00:00+00:00", "user": {"username": "user1"}, "text": "Tweet 1"}',
            '{"date": "2022-01-01T12:00:00+00:00", "user": {"username": "user2"}, "text": "Tweet 2"}',
            '{"date": "2022-01-02T12:00:00+00:00", "user": {"username": "user1"}, "text": "Tweet 3"}'
        ]
        expected_multiple_tweets = defaultdict(Counter, {
            datetime(2022, 1, 1).date(): Counter({'user1': 1, 'user2': 1}),
            datetime(2022, 1, 2).date(): Counter({'user1': 1})
        })
        self.assertEqual(process_data(lines_multiple_tweets), expected_multiple_tweets)


if __name__ == '__main__':
    unittest.main()
