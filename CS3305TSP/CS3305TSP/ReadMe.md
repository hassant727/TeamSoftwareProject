changes in the setting.py
-
line 80 -> 89
> I have configured the setting to use .env file in order to hide the database credentials
----
> > so in the CS3305TSP I created a file called .env 
> >> from terminal `cat >> .env` or whichever way that suit u
>>>> within the env file exported the following from my db(formatting is very important you can not place all the 
> exports in one line even though u separating them with a comma)
>>>>>`export
DB_NAME=db.sqlite3,
DB_USER=root,
DB_USER_PASSWORD=password,
DB_HOST=localhost,`
----
> in setting between <b>80-89</b> I am using environment to get the user credentials(this is important because only you 
> can have access to your db password) 
>> if a user forget their credentials you will have to configure setting(see line 141-142 in settings.py) to use your gmail to send a reset token/link, 
> since we're sharing a github repo, this is essential for individual privacy
> 
----
> no chnages i just added an alternative smtp loggin option that we can you  if you cant set up your .env file
external links
if the above doesnt work for you(see the link below on how to add enviroment variables)
https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm

# if you add anything into setting.py please state which lines at the time of working you've modified