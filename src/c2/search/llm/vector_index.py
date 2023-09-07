from App.special_dtml import DTMLFile
from BTrees.IOBTree import IOBTree
from BTrees.Length import Length
from OFS.SimpleItem import SimpleItem
from Acquisition import Implicit
from Persistence import Persistent
from zope.interface import implementer
from AccessControl.class_init import InitializeClass
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.Permissions import search_zcatalog
from Products.PluginIndexes.interfaces import IQueryIndex
try:
    from plone.app.contenttypes.indexers import SearchableText
except ImportError:
    SearchableText = None

from c2.search.llm.interfaces import IVectorIndex
from c2.search.llm.embedding import get_embeddings


@implementer(IVectorIndex, IQueryIndex)
class VectorIndex(Persistent, Implicit, SimpleItem):
    """
    """
    meta_type = 'VectorIndex'
    query_options = ('query', 'range', 'not')

    manage_options = (
        {'label': 'Settings', 'action': 'manage_main'},
    )

    manage = manage_main = DTMLFile('dtml/manageVectorIndex', globals())
    manage_main._setName('manage_main')

    security = ClassSecurityInfo()
    # security.declareObjectProtected(manage_zcatalog_indexes)

    def __init__(self, id, extra=None, *args, **kwargs):
        self.id = id
        # print(f"extra: {extra}")
        # print(f"args: {args}")
        # print(f"kwargs: {kwargs}")
        self._docvectors = IOBTree()
        self.length = Length()
        self.document_count = Length()

    def _change_length(self, name, value):
        length_obj = getattr(self, name, None)
        if length_obj is not None:
            length_obj.change(value)
        else:
            setattr(self, name, Length(value))

    def index_object(self, documentId, obj, threshold=None):
        count = 0
        if SearchableText is not None:
            text = SearchableText(obj)
            row = self.index_doc(documentId, text)
            count += row
        fields = self.getIndexSourceNames()
        for field in fields:
            value = getattr(obj, field, None)
            if value is not None:
                row = self.index_doc(documentId, value)
                count += row
        return count  # Number of vector rows

    def index_doc(self, docid, text):
        old_vectors = self._docvectors.get(docid, None)
        if old_vectors is not None:
            self._change_length("document_count", -1)
            old_row, old_col = old_vectors.shape
            self._change_length("length", -old_row)
        vectors = get_embeddings(text)
        row, col = vectors.shape
        print("row, col", row, col)
        self._change_length("document_count", 1)
        self._change_length("length", row)
        self._docvectors[docid] = vectors
        return row

    def unindex_object(self, docid):
        old_vectors = self._docvectors.get(docid, None)
        if old_vectors is not None:
            self._change_length("document_count", -1)
            old_row, old_col = old_vectors.shape
            self._change_length("length", -old_row)
        del self._docvectors[docid]

    def _apply_index(self, request):
        print("VectorIndex+++++++@@@@@@@@@@@@@@@@+++ _apply_index", request)  # タイミング未確認

    @security.protected(search_zcatalog)
    def query(self, query, nbest=10):
        print("VectorIndex++++++++++++++++++++++++++ query", query, nbest)  # タイミング未確認
        return []

    def query_index(self, record, resultset=None):
        print("VectorIndex++++++++++++++++++++++++++ query_index", record, resultset)  # タイミング未確認

    def getEntryForObject(self, documentId, default=None):
        print("VectorIndex++++++++++++++++++++++++++ getEntryForObject", documentId, default)  # タイミング未確認

    def uniqueValues(self, name=None, withLengths=0): 
        print("VectorIndex++++++++++++++++++++++++++ uniqueValues", name, withLengths)  # タイミング未確認
        raise NotImplementedError

    def numObjects(self):
        return self.document_count()

    def indexSize(self):
        return self.length()

    def clear(self):
        self._docvectors = IOBTree()
        self.length = Length()
        self.document_count = Length()

    def getIndexSourceNames(self):
        return getattr(self, 'indexed_attrs', [self.id])  # TODO: Not using it now?

    def getIndexQueryNames(self):
        # print("getIndexQueryNames------------------------", f"{self.length()} / {self.document_count()}")
        return (self.id,)

    def getIndexType(self):
        print("getIndexType")  # タイミング未確認
        return "VectorIndex"


InitializeClass(VectorIndex)
manage_addVectorIndexForm = DTMLFile('dtml/addVectorIndex', globals())


def manage_addVectorIndex(self, id, extra=None, REQUEST=None,
                         RESPONSE=None, URL3=None):
    """Add a vector index"""
    return self.manage_addIndex(id, 'VectorIndex', extra=extra, REQUEST=REQUEST,
                                RESPONSE=RESPONSE, URL1=URL3)
