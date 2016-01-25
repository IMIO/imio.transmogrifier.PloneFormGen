# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from imio.transmogrifier.PloneFormGen.testing import IMIO_TRANSMOGRIFIER_PLONEFORMGEN_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that imio.transmogrifier.PloneFormGen is properly installed."""

    layer = IMIO_TRANSMOGRIFIER_PLONEFORMGEN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if imio.transmogrifier.PloneFormGen is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'imio.transmogrifier.PloneFormGen'))

    def test_browserlayer(self):
        """Test that IImioTransmogrifierPloneformgenLayer is registered."""
        from imio.transmogrifier.PloneFormGen.interfaces import (
            IImioTransmogrifierPloneformgenLayer)
        from plone.browserlayer import utils
        self.assertIn(IImioTransmogrifierPloneformgenLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IMIO_TRANSMOGRIFIER_PLONEFORMGEN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['imio.transmogrifier.PloneFormGen'])

    def test_product_uninstalled(self):
        """Test if imio.transmogrifier.PloneFormGen is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'imio.transmogrifier.PloneFormGen'))
