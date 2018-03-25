#!/usr/bin/env python3

# This entire file is super hacky since directly importing apertium-init
# is not possible but we want to maintain backwards compatibility.

import sys
from os import path

initial_name = __name__

sys.path.append(path.abspath(path.dirname(__file__)))  # for repo execution
sys.path.append(path.join(sys.prefix, 'apertium_init'))  # for installed execution
module = __import__('apertium-init')
globals().update(vars(module))

if initial_name == '__main__':
    main()  # type: ignore  # noqa: F821
