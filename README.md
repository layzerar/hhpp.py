# Introduction
[![Build Status](https://travis-ci.org/layzerar/hhpp.py.svg?branch=master)](https://travis-ci.org/layzerar/hhpp.py)
[![Coverage Status](https://coveralls.io/repos/github/layzerar/hhpp.py/badge.svg?branch=master)](https://coveralls.io/github/layzerar/hhpp.py?branch=master)

`hhpp.py` is a programming pattern library for world peace, LOL.

# General Patterns
## Fallback processing chain
```python
from hhpp.llive import fallbacks

def get_key_from_memcached(key):
    return mc.get(key)

def get_key_from_redis(key):
    value = rc.get(key)
    if value is None:
        fallbacks.abort()
    return value

# Live migrate data from memcached to redis:
#   If key not in redis, fallback to memcached. So that we can migrate cache
#   from memcached to redis in the background without data loss.
value = fallbacks.Fallbacks()\
    .chain(get_key_from_redis, 'test_key')\
    .chain(get_key_from_memcached, 'test_key')\
    .done()
```
