from PhotoSharingApplication.Models import *

class PhotoSharingApplication: #this class replaces the original namespace 'PhotoSharingApplication'
    class Controllers: #this class replaces the original namespace 'Controllers'
#C# TO PYTHON CONVERTER TASK: C# attributes do not have Python equivalents:
#ORIGINAL LINE: [HandleError(View = "Error")][ValueReporter] public class PhotoController : Controller
        class PhotoController(Controller):

            def _initialize_instance_fields(self):
                #instance fields found by C# to Python Converter:
                self._context = None


            #Constructors
#C# TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public PhotoController()
            def __init__(self):
                self._initialize_instance_fields()
                self._context = PhotoSharingContext()

#C# TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public PhotoController(IPhotoSharingContext Context)
            def __init__(self, Context):
                self._initialize_instance_fields()
                self._context = Context

            #
            # GET: /Photo/
            def Index(self):
                return View("Index")

#C# TO PYTHON CONVERTER TASK: C# attributes do not have Python equivalents:
#ORIGINAL LINE: [ChildActionOnly] public ActionResult _PhotoGallery(int number = 0)
            def _PhotoGallery(self, number = 0):
                photos = None

                if number == 0:
                    photos = self._context.Photos.ToList()
                else:
                    photos = (from_ p in self._context.Photos orderby p.CreatedDate descending select p).Take(number).ToList()

                return PartialView("_PhotoGallery", photos)

            def Display(self, id):
                photo = self._context.FindPhotoById(id)
                if photo is None:
                    return HttpNotFound()
                return View("Display", photo)

            def DisplayByTitle(self, title):
                photo = self._context.FindPhotoByTitle(title)
                if photo is None:
                    return HttpNotFound()
                return View("Display", photo)

#C# TO PYTHON CONVERTER TASK: Python does not allow method overloads:
            def Create(self):
                newPhoto = Photo()
                newPhoto.CreatedDate = DateTime.Today
                return View("Create", newPhoto)

#C# TO PYTHON CONVERTER TASK: C# attributes do not have Python equivalents:
#ORIGINAL LINE: [HttpPost] public ActionResult Create(Photo photo, HttpPostedFileBase image)
#C# TO PYTHON CONVERTER TASK: Python does not allow method overloads:
            def Create(self, photo, image):
                photo.CreatedDate = DateTime.Today
                if not ModelState.IsValid:
                    return View("Create", photo)
                else:
                    if image is not None:
                        photo.ImageMimeType = image.ContentType
                        photo.PhotoFile = [0 for _ in range(image.ContentLength)]
                        image.InputStream.Read(photo.PhotoFile, 0, image.ContentLength)
                    self._context.Add(photo)
                    self._context.SaveChanges()
                    return RedirectToAction("Index")

            def Delete(self, id):
                photo = self._context.FindPhotoById(id)
                if photo is None:
                    return HttpNotFound()
                return View("Delete", photo)

#C# TO PYTHON CONVERTER TASK: C# attributes do not have Python equivalents:
#ORIGINAL LINE: [HttpPost][ActionName("Delete")] public ActionResult DeleteConfirmed(int id)
            def DeleteConfirmed(self, id):
                photo = self._context.FindPhotoById(id)
                self._context.Delete(photo)
                self._context.SaveChanges()
                return RedirectToAction("Index")

            def GetImage(self, id):
                photo = self._context.FindPhotoById(id)
                if photo is not None:
                    return File(photo.PhotoFile, photo.ImageMimeType)
                else:
                    return None

            def SlideShow(self):
                return View("SlideShow", self._context.Photos.ToList())
