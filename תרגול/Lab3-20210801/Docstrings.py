#https://www.python.org/dev/peps/pep-0257/
"""One-line Docstrings."""
"""
Multi-line 
Docstrings
"""
"""
Home Work number
Names+IDs
"""
def f1(x,y):
    """
    Question number.
    Function description.
    Parameters list.
    Return value.
    """
    if x>y:
        return True
    return False

print('f1 Docstrings')
print (f1.__doc__)
help(f1)
print('File Docstrings')
print(__doc__)
