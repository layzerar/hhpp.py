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


class FallbackError(Exception):
    """Raises when fallback is failed.
    """


class Fallbacks(object):
    """Implement the fallback processing chain pattern.
    """

    def __init__(self):
        self._chain = []
        self._evaluated = False

    def chain(self, func, *args, **kwds):
        if not self._evaluated:
            self._chain.append((func, args, kwds))
        return self

    def done(self):
        self._evaluated = True
        last_index = len(self._chain)
        for index, (func, args, kwds) in enumerate(self._chain, start=1):
            try:
                result = func(*args, **kwds)
            except FallbackError:
                if index == last_index:
                    raise
            else:
                return result
        return None


def abort(msg="fallback aborted"):
    """Cancel an fallback.
    """
    raise FallbackError(msg)
