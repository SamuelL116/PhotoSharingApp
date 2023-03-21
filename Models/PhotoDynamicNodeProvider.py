from MvcSiteMapProvider.Extensibility import *

class PhotoSharingApplication: #this class replaces the original namespace 'PhotoSharingApplication'
    class Models: #this class replaces the original namespace 'Models'
        class PhotoDynamicNodeProvider(DynamicNodeProviderBase):

            def __init__(self):
                #instance fields found by C# to Python Converter:
                self._context = PhotoSharingContext()


            def GetDynamicNodeCollection(self):
                returnList = []

                for item in self._context.Photos:
                    newNode = DynamicNode()
                    newNode.Title = item.Title
                    newNode.ParentKey = "AllPhotos"
                    newNode.RouteValues.Add("id", item.PhotoID)
                    returnList.append(newNode)

                return returnList