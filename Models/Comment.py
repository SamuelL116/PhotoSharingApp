class PhotoSharingApplication: #this class replaces the original namespace 'PhotoSharingApplication'
    class Models: #this class replaces the original namespace 'Models'
        class Comment:

            def __init__(self):
                #instance fields found by C# to Python Converter:
                self.CommentID = 0
                self.PhotoID = 0
                self.UserName = None
                self.Subject = None
                self.Body = None
                self.Photo = None

            #CommentID. This is the Primary Key

            #PhotoID. This is the ID of the photo that this comment relates to

            #UserName. This is the name of the user who made this comment