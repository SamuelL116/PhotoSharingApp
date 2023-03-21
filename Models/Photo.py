import datetime

class PhotoSharingApplication: #this class replaces the original namespace 'PhotoSharingApplication'
    class Models: #this class replaces the original namespace 'Models'
        class Photo:

            def __init__(self):
                #instance fields found by C# to Python Converter:
                self.PhotoID = 0
                self.Title = None
                self.PhotoFile = None
                self.ImageMimeType = None
                self.Description = None
                self.CreatedDate = datetime()
                self.UserName = None
                self.ICollection = None