from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNTrackRectangleRequest(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            Vision.VNTrackRectangleRequest.initWithRectangleObservation_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTrackRectangleRequest.initWithCompletionHandler_, 0, b"v@@"
        )

    def test_constants(self):
        self.assertEqual(Vision.VNTrackRectangleRequestRevision1, 1)
