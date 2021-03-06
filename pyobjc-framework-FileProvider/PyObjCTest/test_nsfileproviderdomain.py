import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderDomain(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(FileProvider.NSFileProviderDomainDidChange, str)

        self.assertEqual(
            FileProvider.NSFileProviderDomainTestingModeAlwaysEnabled, 1 << 0
        )
        self.assertEqual(
            FileProvider.NSFileProviderDomainTestingModeInteractive, 1 << 1
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(FileProvider.NSFileProviderDomain.isDisconnected)
        self.assertResultIsBOOL(FileProvider.NSFileProviderDomain.userEnabled)
        self.assertResultIsBOOL(FileProvider.NSFileProviderDomain.isHidden)
