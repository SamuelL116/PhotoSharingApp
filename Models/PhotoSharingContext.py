class PhotoSharingApplication: #this class replaces the original namespace 'PhotoSharingApplication'
    class Models: #this class replaces the original namespace 'Models'
        class PhotoSharingContext(DbContext, IPhotoSharingContext):

            def __init__(self):
                #instance fields found by C# to Python Converter:
                self.Photos = None
                self.Comments = None

            def get_photos(self):
                return Photos
            def set_photos(self, value):
                Photos = value
            def get_comments(self):
                return Comments
            def set_comments(self, value):
                Comments = value

            def get_photos(self):
                return self.Photos

            def get_comments(self):
                return self.Comments

            def SaveChanges(self):
                return self.SaveChanges()

            def Add(self, entity):
                return Set().Add(entity)

            def FindPhotoById(self, ID):
                return Set().Find(ID)

            def FindPhotoByTitle(self, Title):
                photo = (from_ p in Set() where p.Title == Title select p).FirstOrDefault()
                return photo

            def FindCommentById(self, ID):
                return Set().Find(ID)


            def Delete(self, entity):
                return Set().Remove(entity)