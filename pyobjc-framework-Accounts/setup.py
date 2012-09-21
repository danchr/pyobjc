''' 
Wrappers for the "Accounts" framework on MacOS X. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

setup(
    name='pyobjc-framework-Accounts',
    version="2.4a0",
    description = "Wrappers for the framework Accounts on Mac OS X",
    packages = [ "Accounts" ],
    setup_requires = [
        'pyobjc-core>=2.4a0',
    ],
    install_requires = [ 
        'pyobjc-core>=2.4a0',
        'pyobjc-framework-Cocoa>=2.4a0',
    ],
    min_os_level="10.8",
)