__all__ = [
    'does_not_raise',
    'PY36',
    # For compatibility with Python 3.6 and 3.7
    'Literal',
    'TypedDict'
]

import sys


# Check if we are running Python 3.6
PY36 = sys.version_info[:2] == (3, 6)

# Ref: https://docs.pytest.org/en/6.2.x/example/parametrize.html#parametrizing-conditional-raising
if sys.version_info[:2] >= (3, 7):
    from contextlib import nullcontext as does_not_raise
else:
    from contextlib import ExitStack as does_not_raise

try:
    from typing import Literal
    from typing import TypedDict
except ImportError:
    from typing_extensions import Literal
    from typing_extensions import TypedDict