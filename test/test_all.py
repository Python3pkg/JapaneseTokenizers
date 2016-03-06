__author__ = 'kensuke-mi'

import sys
import unittest
python_version = sys.version_info


def suite():
    suite = unittest.TestSuite()
    if python_version >= (3, 0, 0):
        from .test_mecab_wrapper_python3 import TestMecabWrapperPython3
        suite.addTest(unittest.makeSuite(TestMecabWrapperPython3))
    else:
        from .test_mecab_wrapper_python2 import TestMecabWrapperPython2
        from .test_juman_wrapper_python2 import TestJumanWrapperPython2
        from .test_kytea_wrapper_python2 import TestKyteaWrapperPython2
        suite.addTest(unittest.makeSuite(TestKyteaWrapperPython2))
        suite.addTest(unittest.makeSuite(TestMecabWrapperPython2))
        suite.addTest(unittest.makeSuite(TestJumanWrapperPython2))


    return suite