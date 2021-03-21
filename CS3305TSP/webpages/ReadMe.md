web pages modification
-
> This is the webpages app, within this app (in django you can have multiple app and combine them together to make 
> one powerful app)
> > - For the sack of clarification I will refer to the app as dir
> > - This dir configs almost everything in the fron end of the site except for the user authentications
> > - I will describe what each file does below
> > > - admin.py : is used to add the dir on the admin portal for access and monitoring if need be
> > > - apps.py defines the app, and is config by passing calling it in setting.py, without this process the whole dir 
> > > will not be visible on the site
> > > - forms.py : is used to declare the forms we use in the templates, some of these may require crispy_forms, 
> > > - models.py : this defines the model, and it attributes types
> > > - price_predictor.py : This consist of the price prediction basic algorithm
> > > - urls.py : consist of urls that are accessed on the browser
> > > - views.py : these are http response