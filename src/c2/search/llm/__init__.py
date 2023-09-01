# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory
from c2.search.llm.vector_index import VectorIndex, manage_addVectorIndex, manage_addVectorIndexForm


_ = MessageFactory('c2.search.llm')


def initialize(context):
    context.registerClass(VectorIndex,
                          permission='Add Pluggable Index',
                          constructors=(manage_addVectorIndexForm,
                                        manage_addVectorIndex),
                          visibility=None,
                          )
