from autotest import *

T = Test("Test 1")

T.add(100, "Adding",
     """
     Testing the basic setup of the Notebook environment. 
     """,
     NB("notebook.ipynb", "tests/test.ipynb"))
T.report()
