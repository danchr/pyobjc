from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCLayer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCLayer.isDebuggingEnabled)
