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
        self.pathkey = defaultMatcher(options, 'path-key', name, 'path')

    def __iter__(self):
        """
        Iterate transmogrifier structure
        """
        for item in self.previous:
            pathkey = self.pathkey(*item.keys())[0]
            path = item[pathkey]
            obj = self.context.unrestrictedTraverse(path.lstrip('/'), None)
            if not obj.portal_type == 'FormCaptchaField' and not obj.portal_type == 'FormTextField' and not obj.portal_type == 'FormMailerAdapter' and not obj.portal_type == 'FormStringField' and not obj.portal_type ==  'FormSelectionField' and not obj.portal_type ==  'FormIntegerField':
                yield item; continue

            # Add specific treatment for PloneFormGen Items
            # set utf8 fix for description/formQuestion PloneFormGen fields.
            description = obj.Description()
            obj.setDescription(description)
            yield item
