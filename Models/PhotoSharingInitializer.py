class PhotoSharingApplication: #this class replaces the original namespace 'PhotoSharingApplication'
    class Models: #this class replaces the original namespace 'Models'
        class PhotoSharingInitializer(DropCreateDatabaseAlways):
            #This method puts sample data into the database
            def Seed(self, context):
                super().Seed(context)

                #Create some photos
                temp_var = Photo()
                temp_var.Title = "Sample Photo 1"
                temp_var.Description = "This is the first sample photo in the Adventure Works photo application"
                temp_var.UserName = "AllisonBrown"
                temp_var.PhotoFile = self._getFileBytes("\\Images\\flower.jpg")
                temp_var.ImageMimeType = "image/jpeg"
                temp_var.CreatedDate = DateTime.Today.AddDays(-5)
                temp_var2 = Photo()
                temp_var2.Title = "Sample Photo 2"
                temp_var2.Description = "This is the second sample photo in the Adventure Works photo application"
                temp_var2.UserName = "RogerLengel"
                temp_var2.PhotoFile = self._getFileBytes("\\Images\\orchard.jpg")
                temp_var2.ImageMimeType = "image/jpeg"
                temp_var2.CreatedDate = DateTime.Today.AddDays(-14)
                temp_var3 = Photo()
                temp_var3.Title = "Sample Photo 3"
                temp_var3.Description = "This is the third sample photo in the Adventure Works photo application"
                temp_var3.UserName = "AllisonBrown"
                temp_var3.PhotoFile = self._getFileBytes("\\Images\\path.jpg")
                temp_var3.ImageMimeType = "image/jpeg"
                temp_var3.CreatedDate = DateTime.Today.AddDays(-14)
                temp_var4 = Photo()
                temp_var4.Title = "Sample Photo 4"
                temp_var4.Description = "This is the forth sample photo in the Adventure Works photo application"
                temp_var4.UserName = "JimCorbin"
                temp_var4.PhotoFile = self._getFileBytes("\\Images\\fungi.jpg")
                temp_var4.ImageMimeType = "image/jpeg"
                temp_var4.CreatedDate = DateTime.Today.AddDays(-12)
                temp_var5 = Photo()
                temp_var5.Title = "Sample Photo 5"
                temp_var5.Description = "This is the fifth sample photo in the Adventure Works photo application"
                temp_var5.UserName = "JamieStark"
                temp_var5.PhotoFile = self._getFileBytes("\\Images\\pinkflower.jpg")
                temp_var5.ImageMimeType = "image/jpeg"
                temp_var5.CreatedDate = DateTime.Today.AddDays(-11)
                temp_var6 = Photo()
                temp_var6.Title = "Sample Photo 6"
                temp_var6.Description = "This is the sixth sample photo in the Adventure Works photo application"
                temp_var6.UserName = "JamieStark"
                temp_var6.PhotoFile = self._getFileBytes("\\Images\\blackberries.jpg")
                temp_var6.ImageMimeType = "image/jpeg"
                temp_var6.CreatedDate = DateTime.Today.AddDays(-11)
                temp_var7 = Photo()
                temp_var7.Title = "Sample Photo 7"
                temp_var7.Description = "This is the seventh sample photo in the Adventure Works photo application"
                temp_var7.UserName = "BernardDuerr"
                temp_var7.PhotoFile = self._getFileBytes("\\Images\\coastalview.jpg")
                temp_var7.ImageMimeType = "image/jpeg"
                temp_var7.CreatedDate = DateTime.Today.AddDays(-10)
                temp_var8 = Photo()
                temp_var8.Title = "Sample Photo 8"
                temp_var8.Description = "This is the eigth sample photo in the Adventure Works photo application"
                temp_var8.UserName = "FengHanYing"
                temp_var8.PhotoFile = self._getFileBytes("\\Images\\headland.jpg")
                temp_var8.ImageMimeType = "image/jpeg"
                temp_var8.CreatedDate = DateTime.Today.AddDays(-9)
                temp_var9 = Photo()
                temp_var9.Title = "Sample Photo 9"
                temp_var9.Description = "This is the ninth sample photo in the Adventure Works photo application"
                temp_var9.UserName = "FengHanYing"
                temp_var9.PhotoFile = self._getFileBytes("\\Images\\pebbles.jpg")
                temp_var9.ImageMimeType = "image/jpeg"
                temp_var9.CreatedDate = DateTime.Today.AddDays(-8)
                temp_var10 = Photo()
                temp_var10.Title = "Sample Photo 10"
                temp_var10.Description = "This is the tenth sample photo in the Adventure Works photo application"
                temp_var10.UserName = "SalmanMughal"
                temp_var10.PhotoFile = self._getFileBytes("\\Images\\pontoon.jpg")
                temp_var10.ImageMimeType = "image/jpeg"
                temp_var10.CreatedDate = DateTime.Today.AddDays(-7)
                temp_var11 = Photo()
                temp_var11.Title = "Sample Photo 11"
                temp_var11.Description = "This is the eleventh sample photo in the Adventure Works photo application"
                temp_var11.UserName = "JamieStark"
                temp_var11.PhotoFile = self._getFileBytes("\\Images\\ripples.jpg")
                temp_var11.ImageMimeType = "image/jpeg"
                temp_var11.CreatedDate = DateTime.Today.AddDays(-5)
                temp_var12 = Photo()
                temp_var12.Title = "Sample Photo 12"
                temp_var12.Description = "This is the twelth sample photo in the Adventure Works photo application"
                temp_var12.UserName = "JimCorbin"
                temp_var12.PhotoFile = self._getFileBytes("\\Images\\rockpool.jpg")
                temp_var12.ImageMimeType = "image/jpeg"
                temp_var12.CreatedDate = DateTime.Today.AddDays(-3)
                temp_var13 = Photo()
                temp_var13.Title = "Sample Photo 13"
                temp_var13.Description = "This is the thirteenth sample photo in the Adventure Works photo application"
                temp_var13.UserName = "AllisonBrown"
                temp_var13.PhotoFile = self._getFileBytes("\\Images\\track.jpg")
                temp_var13.ImageMimeType = "image/jpeg"
                temp_var13.CreatedDate = DateTime.Today.AddDays(-1)
                photos = [temp_var, temp_var2, temp_var3, temp_var4, temp_var5, temp_var6, temp_var7, temp_var8, temp_var9, temp_var10, temp_var11, temp_var12, temp_var13]
                photos.ForEach(lambda s : context.Photos.Add(s))
                context.SaveChanges()

                #Create some comments
                temp_var14 = Comment()
                temp_var14.PhotoID = 1
                temp_var14.UserName = "JamieStark"
                temp_var14.Subject = "Sample Comment 1"
                temp_var14.Body = "This is the first sample comment in the Adventure Works photo application"
                temp_var15 = Comment()
                temp_var15.PhotoID = 1
                temp_var15.UserName = "JimCorbin"
                temp_var15.Subject = "Sample Comment 2"
                temp_var15.Body = "This is the second sample comment in the Adventure Works photo application"
                temp_var15 = Comment()
                temp_var15.PhotoID = 3
                temp_var15.UserName = "RogerLengel"
                temp_var15.Subject = "Sample Comment 3"
                temp_var15.Body = "This is the third sample photo in the Adventure Works photo application"
                comments = [temp_var, temp_var2, temp_var3]
                comments.ForEach(lambda s : context.Comments.Add(s))

            context.SaveChanges()

                #This gets a byte array for a file at the path specified
                #The path is relative to the route of the web site
                #It is used to seed images
            private byte[] self._getFileBytes(string path)
            fileOnDisk = FileStream(HttpRuntime.AppDomainAppPath + path, FileMode.Open)
            fileBytes = None
            with BinaryReader(fileOnDisk) as br:
            fileBytes = br.ReadBytes(int(fileOnDisk.Length))
            return fileBytes