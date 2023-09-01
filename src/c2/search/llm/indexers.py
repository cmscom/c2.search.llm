from plone.indexer import indexer
# from zope.interface import Interface
from plone.dexterity.interfaces import IDexterityContent
# from plone.app.contenttypes.interfaces import IDocument, IFile
from plone.app.contenttypes.indexers import SearchableText
from c2.search.llm.embedding import get_embeddings


@indexer(IDexterityContent)
def llm_vector(obj):
    """Return the vector for the given object"""
    print("obj", obj)
    text = SearchableText(obj)
    # print("print;: ", obj.id, text)
    vector = get_embeddings(text)
    return vector
