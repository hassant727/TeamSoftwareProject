# Property Pricer
CS3305 Team Software Project - Group 13


Team Members:
-
- Hassan Tariq
- Kevin Mukuna
- Kieran Sheedy O'Sullivan
- Killian O' Driscoll
- Kiu Man Yeung



# About The Project
> PropertyPricer is an ecommerce site, designed for users to buy and sell property. In addition to all the basic 
> features of such a site, we have implemented a price prediction model which we believe gives us a unique edge over 
> other similar sites.
> Thanks to our price prediction model, our users will have access to the best possible information when trying to sell 
> their property. Not only do we give an estimate of the predicted price at time of posting, but we also provide an 
> outline of how that price is expected to change over time based on various market factors.
> In order to take advantage of this service, all our users need to do is post a property for sale. Based on the 
> information provided on the property, our algorithm will determine the current & future estimated prices and display 
> them to you in the form of a chart on your profile page.




Using the software: After cloning the project 
-
> execute the code as follows if on windows 
>> `cd CS3305TSP` 
>>> `pip install -r requirement.txt`
>>>> `python manage.py migrate` 
>>>>> `python manage.py createsuperuser`
> follow the steps and finally run the server
>>>>> `python manage.py runserver.py`

> execute the code as follows on unix
> execute the code as follows
>> `cd CS3305TSP`
>>> `chmod +x .runscript.sh`
>>>> `./.runscript.sh` 


# Project Structure (names with a capital letter represent dir )

    CS33305TSP
               ------ CS33305TSP
                                 ----- __init__.py  
                                 ----- asig.py  
                                 ----- settings.py  
                                 ----- urls.py  
                                 ----- views.py  
                                 ----- README.MD
               ------ Dashboard
                               ----- Migrations
                               ----- __init__.py
                               ----- apps.py
                               ----- forms.py
                               ----- models.py
                               ----- tests.py
                               ----- urls.py
                               ----- views.py
               ------ Fixture

               ------ Media
                              ----- Post_images
                              ----- Profile_images
                              ----- default img
               ------ Static
                            ----- Css
                            ----- Img
                            ----- Js
                            ----- User_guide
                            ----- Vendor
                            ----- favicon
               ------ templates
                               ----- Dashboard
                                               ----- all_user_function.html
                                               ----- chart.html
                                               ----- dashboard.html
                               ----- Userpages
                                              ----- acc_Active_email.html
                                              ----- login.html
                                              ----- logout.html
                                              ----- password_reset.html
                                              ----- password_reset_complete.html
                                              ----- password_reset_confirm.html
                                              ----- password_reset_done.html
                                              ----- profile.html
                                              ----- redirect.html
                                              ----- register.html
                               ----- Webpages
                                              ----- about.html
                                              ----- chart.html
                                              ----- home.html
                                              ----- long_post.html
                                              ----- pagination.html
                                              ----- post_confirm_delete.html
                                              ----- post_details.html
                                              ----- post_form.html
                                              ----- search.html
                                              ----- user_guide.html
                                              ----- user_posts.html
                               ----- base.html

               ------ Userpages
                                ----- Migrations
                                ----- __init__.py
                                ----- admin.py
                                ----- apps.py
                                ----- forms.py
                                ----- models.py
                                ----- signals.py
                                ----- tests.py
                                ----- tokens.py
                                ----- urls.py
                                ----- utils.py
                                ----- views.py
                                ----- userpageReadMe.md
               ------ Venv
                            ----- all python env files such as lib and bin
               ------ Webpages
                                ----- Migrations
                                ----- __init__.py
                                ----- admin.py
                                ----- apps.py
                                ----- forms.py
                                ----- models.py
                                ----- price_predictor.py
                                ----- tests.py
                                ----- trainingModel.py
                                ----- urls.py
                                ----- utils.py
                                ----- views.py
                                ----- WebpageReadMe.md
               ------ .runscript.sh
               ------ __init__.py
               ------ db.sqlite3
               ------ estimate.json
               ------ manage.py
               ------ ProjectReadMe.md
               ------ requirement.txt
               ------ setup.py
    Documentation
                  ----- product brief versions
#BRANCHES
        - main: used for the up to date running version of the software

        - develop: used for developing new features, addons and functionality for running version of the software
                this is only merged with master after it has been tested and assurance is given that it will not break
                the main software running under master branch


#CODING CONVENTIONS
        - python coding conventions (file names with underscore if they consist of multiple words)
        - separating complex chunks of code/logic to provide readability
        - django file conventions hierarchy 

#BUILD COMMANDS FROM THE TOP OF THE DIR
        cd CS3305TSP && chmod +x .runscript.sh && ./.runscript.sh     

#AOB 
> This project implements a web applications with multiple apps in it
> see the project readme in each app for individual function file/method explanation
