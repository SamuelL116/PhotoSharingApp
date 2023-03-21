class PhotoSharingApplication: #this class replaces the original namespace 'PhotoSharingApplication'
    class Controllers: #this class replaces the original namespace 'Controllers'
        class ValueReporter(ActionFilterAttribute):
            def OnActionExecuting(self, filterContext):
                self._LogValues(filterContext.RouteData)

            def _LogValues(self, routeData):
                controller = routeData.Values["controller"]
                action = routeData.Values["action"]
                message = "Controller: {0:s}; Action: {1:s}".format(controller, action)
                Debug.WriteLine(message, "Action Values")

                for item in routeData.Values:
                    Debug.WriteLine(">> Key: {0}; Value {1}", item.Key, item.Value)