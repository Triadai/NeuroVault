"""
there was previously a bug that prevented collection folders from being deleted when the collection was deleted.
this is now fixed but this script provides a way to delete all of the leftover collection folders whose corresponding
collections were deleted before the fix.
"""

from neurovault.apps.statmaps.models import Collection
from neurovault.settings import PRIVATE_MEDIA_ROOT
import os
import os.path


collectionsDir = os.path.join(PRIVATE_MEDIA_ROOT, 'images')
for folder in os.listdir(collectionsDir):
    if not Collection.objects.get(id=int(folder)):
        os.rmdir(os.path.join(collectionsDir, folder))
        