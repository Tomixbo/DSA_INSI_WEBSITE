# DSA_INSI_WEBSITE
Repository for DSA website files.

The project is a website made with Django. The objective of the website is the management of coding challenges and coding contests between the DSA's member.

## Features : 
- Managing challenges + levels + I/O files
- Testing user outputs
- Category and difficulty classement

## Future implementations :
- User account and profile
- User performance monitoring
- Time managment
- Making contest

## Deployment :
- create virtual environment with python 3.10.0
> python3.10 -m venv .venv
- activate the virtual environment
> .venv\Scripts\activate
- install all requirements in : requirements.txt
> pip install --yes -r requirements.txt
- launch the django website
> cd local_contest </br>
> python manage.py runserver 127.0.0.1:8001
- open the url 127.0.0.1:8001 in a browser
- to access the website with another device in the same LAN : ip-address-of-pc-server:8001 (ex : 192.168.88.125:8001) </br>
*Note : use the cmd command : "ipconfig -all" to see the ip-address

### Administration page :
Go to the next url for database administration :
> 127.0.0.1/admin
</br>

Super-user :
- username : admin </br>
- password : mysecret
