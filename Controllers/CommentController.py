from PhotoSharingApplication.Models import *

class PhotoSharingApplication: #this class replaces the original namespace 'PhotoSharingApplication'
    class Controllers: #this class replaces the original namespace 'Controllers'
        class CommentController(Controller):

            def _initialize_instance_fields(self):
                #instance fields found by C# to Python Converter:
                self._context = None


            #Constructors
#C# TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public CommentController()
            def __init__(self):
                self._initialize_instance_fields()
                self._context = PhotoSharingContext()

#C# TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public CommentController(IPhotoSharingContext Context)
            def __init__(self, Context):
                self._initialize_instance_fields()
                self._context = Context

            #
            # GET: A Partial View for displaying in the Photo Details view
#C# TO PYTHON CONVERTER TASK: C# attributes do not have Python equivalents:
#ORIGINAL LINE: [ChildActionOnly] public PartialViewResult _CommentsForPhoto(int PhotoId)
#C# TO PYTHON CONVERTER TASK: Python does not allow method overloads:
            def _CommentsForPhoto(self, PhotoId):
                #The comments for a particular photo have been requested. Get those comments.
                comments = from_ c in self._context.Comments where c.PhotoID == PhotoId select c
                #Save the PhotoID in the ViewBag because we'll need it in the view
                ViewBag.PhotoId = PhotoId
                return PartialView(comments.ToList())

            #
            #POST: This action creates the comment when the AJAX comment create tool is used
#C# TO PYTHON CONVERTER TASK: C# attributes do not have Python equivalents:
#ORIGINAL LINE: [HttpPost] public PartialViewResult _CommentsForPhoto(Comment comment, int PhotoId)
#C# TO PYTHON CONVERTER TASK: Python does not allow method overloads:
            def _CommentsForPhoto(self, comment, PhotoId):

                #Save the new comment
                self._context.Add(comment)
                self._context.SaveChanges()

                #Get the updated list of comments
                comments = from_ c in self._context.Comments where c.PhotoID == PhotoId select c
                #Save the PhotoID in the ViewBag because we'll need it in the view
                ViewBag.PhotoId = PhotoId
                #Return the view with the new list of comments
                return PartialView("_CommentsForPhoto", comments.ToList())

            #
            # GET: /Comment/_Create. A Partial View for displaying the create comment tool as a AJAX partial page update
            def _Create(self, PhotoId):
                #Create the new comment
                newComment = Comment()
                newComment.PhotoID = PhotoId

                ViewBag.PhotoID = PhotoId
                return PartialView("_CreateAComment")



            #
            # GET: /Comment/Delete/5
            def Delete(self, id = 0):
                comment = self._context.FindCommentById(id)
                ViewBag.PhotoID = comment.PhotoID
                if comment is None:
                    return HttpNotFound()
                return View(comment)

            #
            # POST: /Comment/Delete/5
#C# TO PYTHON CONVERTER TASK: C# attributes do not have Python equivalents:
#ORIGINAL LINE: [HttpPost, ActionName("Delete")] public ActionResult DeleteConfirmed(int id)
            def DeleteConfirmed(self, id):
                comment = self._context.FindCommentById(id)
                self._context.Delete(comment)
                self._context.SaveChanges()
                class AnonymousType:
                    def __init__(self, _id):
                        self.id = _id

                return RedirectToAction("Display", "Photo", AnonymousType(comment.PhotoID))

