# from Products.CMFCore.utils import getToolByName
from plone.app.contenttypes.indexers import SearchableText
from c2.search.llm.embedding import get_embeddings
from c2.search.llm.store.annotation import set_vector


def embedding_from_text(obj, event):
    # _tool = getToolByName(obj, 'XXXXX', None)
    # if _tool is None:
    #     return None
    text = SearchableText(obj)
    print("print;: ", obj.id, text)
    vector = get_embeddings(text)
    set_vector(obj, vector)
