Execution flow 
--
> created the django project by executing 
>>` django-admin startapp nameOFAPP` 
>>> in our case
>>>> django-admin startapp CS3305TSP

> added the requirement.txt file then executed it content by running
>>pip3 install -r requirement.txt

> ran the app by executing 
> `python manage.py runserver`
>> if you get the error upon running saying something of this caliber
>>> You have "x number of " unapplied migration(s).
>>>> run the following command `python manage.py migrate`

> run the following command to execute the initial project
> `python manage.py runserver`
> 
> then you can view the page working
>  http://127.0.0.1:8000/
> 
> run this to ensure the project has been config correctly, and the admin page is  working
>  http://127.0.0.1:8000/admin 

> now to create a superuser(we need this in order to log as an admin) we need to run the following command 
>> `pyhton manage createsuperuser` and follow the onscreen steps
> 
> then run the server by executing 
>> `python manage.py runserver`

> go to 
>> http:localhost:8000/admin or http://127.0.0.1:8000/ 
>>> and enter the user credentials that you provide when creating super user
> 
> ensure that it works properly, and you can log in and log out without any problem 
> (familiarise yourself with the basic admin page setup)

> 
> With the above steps we should be done with basic creation of admin page, and we will modify it to suite our desire 
> output as we proceed