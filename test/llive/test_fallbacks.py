# -*- coding: utf-8 -*-
#
# Copyright 2017 Melvi Ts <layzerar@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from hhpp.llive import fallbacks


class FallbacksTest(unittest.TestCase):

    def test_ok(self):
        self.assertTrue(
            fallbacks.Fallbacks().done() is None
        )
        self.assertEqual(
            'func1',
            fallbacks.Fallbacks()
            .chain(lambda: 'func1')
            .chain(lambda: 'func2')
            .chain(lambda: 'func3')
            .done()
        )
        self.assertEqual(
            'func2',
            fallbacks.Fallbacks()
            .chain(fallbacks.abort)
            .chain(lambda: 'func2')
            .chain(lambda: 'func3')
            .done()
        )

    def test_ok_with_args(self):
        self.assertEqual(
            'func2',
            fallbacks.Fallbacks()
            .chain(fallbacks.abort)
            .chain(lambda name: name, 'func2')
            .chain(lambda name: name, 'func3')
            .done()
        )
        self.assertEqual(
            'func2',
            fallbacks.Fallbacks()
            .chain(fallbacks.abort)
            .chain(lambda name='default2': name, name='func2')
            .chain(lambda name='default3': name, name='func3')
            .done()
        )

    def test_abort(self):
        self.assertEqual(
            'func3',
            fallbacks.Fallbacks()
            .chain(fallbacks.abort)
            .chain(fallbacks.abort)
            .chain(lambda: 'func3')
            .done()
        )
        self.assertEqual(
            'func2',
            fallbacks.Fallbacks()
            .chain(fallbacks.abort)
            .chain(lambda: 'func2')
            .chain(fallbacks.abort)
            .chain(lambda: 'func4')
            .done()
        )

    def test_abort_at_last(self):
        self.assertRaises(
            fallbacks.FallbackError,
            fallbacks.Fallbacks()
            .chain(fallbacks.abort)
            .done
        )
        self.assertRaises(
            fallbacks.FallbackError,
            fallbacks.Fallbacks()
            .chain(fallbacks.abort)
            .chain(fallbacks.abort)
            .chain(fallbacks.abort)
            .done
        )


if __name__ == '__main__':
    unittest.main()
