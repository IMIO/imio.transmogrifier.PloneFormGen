#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collective.transmogrifier.interfaces import ISection, ISectionBlueprint
from collective.transmogrifier.utils import defaultMatcher
from zope.interface import classProvides, implements
import logging

logger = logging.getLogger('imio.transmogrifier.cardimporer.ATPhotoToBlobImage')


class FixUTF8Section(object):
    """
    Blueprint that fix utf-8 char import from PloneFormGen Fields.
    """
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.context = transmogrifier.context
        self.pathkey = defaultMatcher(options, 'path-key', name, 'path')
        self.previous = previous

    def __iter__(self):
        """
        Iterate transmogrifier structure
        """
        for item in self.previous:
            pathkey = self.pathkey(*item.keys())[0]
            path = item[pathkey]
            obj = self.context.unrestrictedTraverse(path.lstrip('/'), None)
            if path == '' or obj is None or obj.aq_parent is None:
                yield item; continue
            else:
                parent = obj.aq_parent
                if parent.getPortalTypeName() != 'FormFolder':
                    yield item; continue
            # Add specific treatment for PloneFormGen Items
            # method setDescription seem fixing utf8 error for PloneFormGen fields.
            description = obj.Description()
            obj.setDescription(description)
            yield item
