import sys
# Detect if code is called from test and set sys constant
# to prevent loading unnecessary modules

def pytest_configure(config):
    setattr(sys, "_called_from_test", True)

def pytest_unconfigure(config):
    delattr(sys, "_called_from_test")