from App.special_dtml import DTMLFile
from Products.PluginIndexes.unindex import UnIndex
from zope.interface import implementer
from AccessControl.class_init import InitializeClass
from c2.search.llm.interfaces import IVectorIndex


@implementer(IVectorIndex)
class VectorIndex(UnIndex):
    """
    """
    meta_type = 'VectorIndex'
    query_options = ('query', 'range', 'not')

    manage_options = (
        {'label': 'Settings', 'action': 'manage_main'},
        {'label': 'Browse', 'action': 'manage_browse'},
    )


    manage = manage_main = DTMLFile('dtml/manageVectorIndex', globals())
    manage_main._setName('manage_main')
    manage_browse = DTMLFile('dtml/browseIndex', globals())

    def _index_object(self, documentId, obj, threshold=None, attr=""):
        """Index an object
        """
        breakpoint()

        vector = getattr(obj, attr, None)
        if vector is None:
            return 0
        shape = vector.shape
        
        self.unindex_object(documentId)
        self._index[documentId] = vector
        return 1
        

InitializeClass(VectorIndex)
manage_addVectorIndexForm = DTMLFile('dtml/addVectorIndex', globals())


def manage_addVectorIndex(self, id, extra=None, REQUEST=None,
                         RESPONSE=None, URL3=None):
    """Add a vector index"""
    return self.manage_addIndex(id, 'VectorIndex', extra=extra, REQUEST=REQUEST,
                                RESPONSE=RESPONSE, URL1=URL3)
