# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import imio.transmogrifier.PloneFormGen


class ImioTransmogrifierPloneformgenLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=imio.transmogrifier.PloneFormGen)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'imio.transmogrifier.PloneFormGen:default')


IMIO_TRANSMOGRIFIER_PLONEFORMGEN_FIXTURE = ImioTransmogrifierPloneformgenLayer()


IMIO_TRANSMOGRIFIER_PLONEFORMGEN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IMIO_TRANSMOGRIFIER_PLONEFORMGEN_FIXTURE,),
    name='ImioTransmogrifierPloneformgenLayer:IntegrationTesting'
)


IMIO_TRANSMOGRIFIER_PLONEFORMGEN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IMIO_TRANSMOGRIFIER_PLONEFORMGEN_FIXTURE,),
    name='ImioTransmogrifierPloneformgenLayer:FunctionalTesting'
)


IMIO_TRANSMOGRIFIER_PLONEFORMGEN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        IMIO_TRANSMOGRIFIER_PLONEFORMGEN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ImioTransmogrifierPloneformgenLayer:AcceptanceTesting'
)
