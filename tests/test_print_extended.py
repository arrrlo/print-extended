import unittest
from io import StringIO
from contextlib import redirect_stdout

import print_extended
from print_extended import PrintControl


class TestPrintExtended(unittest.TestCase):

    def setUp(self):
        PrintControl.template = ' --> {print} <-- '
        PrintControl.fg_color = 'green'
        PrintControl.bg_color = 'blue'

    def tearDown(cls):
        PrintControl.reset()

    def test_print_extended(self):
        printed = StringIO()
        with redirect_stdout(printed):
            print('This Is Test!')

        self.assertEqual(printed.getvalue()[:-1], ' --> This Is Test! <-- ')

        PrintControl.disable()

        printed = StringIO()
        with redirect_stdout(printed):
            print('This Is Test!')

        self.assertEqual(printed.getvalue()[:-1], '')

        PrintControl.enable()

        printed = StringIO()
        with redirect_stdout(printed):
            print('This Is Test!')

        self.assertEqual(printed.getvalue()[:-1], ' --> This Is Test! <-- ')
