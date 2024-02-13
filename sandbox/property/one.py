from hypothesis import given, strategies as st
from binaryornot.helpers import is_binary_string

@given(st.binary())
def test_never_crashes(s):
    is_binary_string(s)
