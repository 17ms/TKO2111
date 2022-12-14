#!/usr/bin/env python3


import random
import unittest
import string
import os
from tests import testutils
from manager import utils


class TestFileUtils(unittest.TestCase):
    def test_json_conversion(self):
        self.maxDiff = None
        generated_data = testutils.generate_testdata()
        filepath = (
            "./"
            + "".join(random.choice(string.ascii_lowercase) for _ in range(8))
            + ".json"
        )

        utils.write_json(filepath, generated_data)
        read_data = utils.read_json(filepath)

        self.assertEqual(generated_data, read_data)

        os.remove(filepath)
