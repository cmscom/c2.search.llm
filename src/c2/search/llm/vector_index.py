from App.special_dtml import DTMLFile
# from Products.PluginIndexes.unindex import UnIndex
from OFS.SimpleItem import SimpleItem
from Acquisition import Implicit
from Persistence import Persistent
from zope.interface import implementer
from AccessControl.class_init import InitializeClass
from AccessControl.SecurityInfo import ClassSecurityInfo
from AccessControl.Permissions import search_zcatalog
from Products.PluginIndexes.interfaces import IQueryIndex
from c2.search.llm.interfaces import IVectorIndex


@implementer(IVectorIndex, IQueryIndex)
class VectorIndex(Persistent, Implicit, SimpleItem):
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

    security = ClassSecurityInfo()
    # security.declareObjectProtected(manage_zcatalog_indexes)

    def __init__(self, id, extra=None, *args, **kwargs):
        self.id = id
        print(f"extra: ", extra )
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")

    @security.protected(search_zcatalog)
    def query(self, query, nbest=10):
        print("VectorIndex++++++++++++++++++++++++++ query", query, nbest)  # タイミング未確認
        return []
    
    def index_object(self, documentId, obj, threshold=None):
        print("VectorIndex++++++++++++++++++++++++++ index_object", documentId, obj, threshold)
        return 1  # TODO

    def unindex_object(self, docid):
        print("VectorIndex++++++++++++++++++++++++++ unindex_object", docid)

    def _apply_index(self, request):
        print("VectorIndex++++++++++++++++++++++++++ _apply_index", request)  # タイミング未確認

    def query_index(self, record, resultset=None):
        print("VectorIndex++++++++++++++++++++++++++ query_index", record, resultset)  # タイミング未確認

    def getEntryForObject(self, documentId, default=None):
        print("VectorIndex++++++++++++++++++++++++++ getEntryForObject", documentId, default)  # タイミング未確認

    def uniqueValues(self, name=None, withLengths=0): 
        print("VectorIndex++++++++++++++++++++++++++ uniqueValues", name, withLengths)  # タイミング未確認
        raise NotImplementedError
    
    def numObjects(self):
        print("VectorIndex++++++++++++++++++++++++++ numObjects")
        return 0

    def indexSize(self):
        print("VectorIndex++++++++++++++++++++++++++ indexSize")
        return 0
    
    def clear(self):
        print("VectorIndex++++++++++++++++++++++++++ clear")

    def getIndexSourceNames(self):
        print("VectorIndex++++++++++++++++++++++++++ getIndexSourceNames")
        return []
    
    def getIndexQueryNames(self):
        print("VectorIndex++++++++++++++++++++++++++ getIndexQueryNames")  # タイミング未確認
        return []
    
    def getIndexType(self):
        print("getIndexType")  # タイミング未確認
        return "VectorIndex"


    # def index_doc(self, docid, text):
    #     print("index_doc", docid, text)

    # def _reindex_doc(self, docid, text):
    #     print("_reindex_doc", docid, text)

    # def unindex_doc(self, docid):
    #     print("unindex_doc", docid)

    # def search(self, term):
    #     print("search", term)


InitializeClass(VectorIndex)
manage_addVectorIndexForm = DTMLFile('dtml/addVectorIndex', globals())


def manage_addVectorIndex(self, id, extra=None, REQUEST=None,
                         RESPONSE=None, URL3=None):
    """Add a vector index"""
    return self.manage_addIndex(id, 'VectorIndex', extra=extra, REQUEST=REQUEST,
                                RESPONSE=RESPONSE, URL1=URL3)
