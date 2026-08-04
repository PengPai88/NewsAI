import unittest
from news_api import TextSummaryProcessor


class TestTextSummaryProcessor(unittest.TestCase):

    def test_generate_summary_normal(self):

        title = "NASA discovers new planet - CNN"

        result = TextSummaryProcessor.generate_summary(title)

        self.assertEqual(
            result,
            "Brief summary: NASA discovers new planet"
        )

    def test_generate_summary_empty(self):

        result = TextSummaryProcessor.generate_summary("")

        self.assertEqual(
            result,
            "Brief summary: "
        )

    def test_generate_summary_long_title(self):

        long_title = "A" * 100

        result = TextSummaryProcessor.generate_summary(long_title)

        self.assertTrue(result.startswith("Brief summary: "))
        self.assertTrue(result.endswith("..."))


if __name__ == "__main__":
    unittest.main()