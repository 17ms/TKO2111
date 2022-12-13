#!/usr/bin/env python3


import random
import unittest
import string
import os
from tests import utils as testutils
from manager import utils


class TestDataModels(unittest.TestCase):
    def test_json_serialization(self):
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
