# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import c2.search.llm


class C2SearchLlmLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=c2.search.llm)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'c2.search.llm:default')


C2_SEARCH_LLM_FIXTURE = C2SearchLlmLayer()


C2_SEARCH_LLM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(C2_SEARCH_LLM_FIXTURE,),
    name='C2SearchLlmLayer:IntegrationTesting',
)


C2_SEARCH_LLM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(C2_SEARCH_LLM_FIXTURE,),
    name='C2SearchLlmLayer:FunctionalTesting',
)


C2_SEARCH_LLM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        C2_SEARCH_LLM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='C2SearchLlmLayer:AcceptanceTesting',
)
