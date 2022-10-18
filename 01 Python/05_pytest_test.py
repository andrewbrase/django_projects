# > python -m venv venv
# >.\venv\Scripts\activate
# > python -m pip install pytest

# def increment(num):
#     return num + 1

# def test_answer():
#     assert increment(5) == 6

# > pytest
# ================================================== 1 passed in 0.03s ==================================================

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# wrong answer example 
def increment(num):
    return num + 1

def test_answer():
    assert increment(5) == 10505

# ====================================================== FAILURES =======================================================
# _____________________________________________________ test_answer _____________________________________________________

#     def test_answer():
# >       assert increment(5) == 10505
# E       assert 6 == 10505
# E        +  where 6 = increment(5)

# 05_pytest_test.py:20: AssertionError
# =============================================== short test summary info ===============================================
# FAILED 05_pytest_test.py::test_answer - assert 6 == 10505
# ================================================== 1 failed in 0.07s ==================================================