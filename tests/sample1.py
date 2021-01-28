import unittest


def remove_a(value: str):
    if value is None:
        raise ValueError("Value is required")

    return value.replace("a", "")


class TestRemoveA(unittest.TestCase):
    def test_remove_a_correctly(self):
        value = "abc"
        result = remove_a(value)
        self.assertEqual(result, "bc")

    def test_remove_a_with_empty_data(self):
        value = None

        with self.assertRaises(ValueError):
            remove_a(value)


if __name__ == "__main__":
    unittest.main()
