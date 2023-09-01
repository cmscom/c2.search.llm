from zope.annotation.interfaces import IAnnotations
from BTrees.OOBTree import OOBTree
import numpy as np

STORE_NAME = 'c2.search.llm'


def setup_annotations(context):
    """
    set up the annotations if they haven't been set up
    already. The rest of the functions in here assume that
    this has already been set up
    """
    annotations = IAnnotations(context)
    if STORE_NAME not in annotations:
        annotations[STORE_NAME] = OOBTree()
    return annotations


def get_vector(context) -> np.ndarray:
    """
    Return the vectors of an item (context).
    shpae: (n, 1024)
    """
    annotations = setup_annotations(context)
    return annotations[STORE_NAME].get('vector')


def set_vector(context, vector: np.ndarray) -> str:
    """
    Setting a vector an item (context).
    """
    annotations = setup_annotations(context)
    annotations[STORE_NAME]["vector"] = vector
    return "Done"


def remove_vector(context) -> str:
    annotations = setup_annotations(context)
    annotations[STORE_NAME] = OOBTree()
    return "Done"
