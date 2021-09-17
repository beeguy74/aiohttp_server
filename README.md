<h1 align="center">MiniCRM</h1>

## Description
<p align="center">
<img src="https://lh3.googleusercontent.com/1t7nZv7HzOVhJUqdd3vRfxQtnEU2_4eXOgcw8-ZDItYnxOikrmV4yeKkaMsCVsHo1f0TYn4u8gmzxR4iKHGK_Ng9PTdczDGCfzrFaw6_5XlgBu-CUQlcSQbBRaZZS0_NPbRsv3Uj0V4sFJOv_YFBeUGA1TSG3J3e6xzA5h70v2TGq35UB-6lZbvctR1bjnd05U6uVsQKivE51IrfWzM8tnWafb1Q3E5GENE7bPpiUD9nquczm90Xd06SfwWxkuz3DoO6YK3GmOeZHFwpjaqhlMeElWTi1TnDOIgXdIqQ_k_PmFg50a9EwaR1RpRADihL2oXzAw3Vip0s2OEh24VFPmufd0Xv066NUhJ14nTOITHApiPQ8pdmRnIHScZj7W0_FibyxkttI2BgikxWr5PmL3qPyY9Ks5Vkd7-zNfSSPAjZdDDZSvDz1SPZjJpBcxGAzVyEOE1D1LvDikm3hrjpbCHYqlG__UyUB5QCTqRhzs5bfRqRohwREJd43q56VHDyKj--cL_ErgKZG9HLvFtZyu3wPY7qCB58FBPEa1cPhonAGaeF_71SvBqlyIn46mKlSqXXZ6zK7AFagJVdVzIbIgfpi3mfQMpx2XGKRr6gWYFU1NR7PCot_TdAtvP30xYuwrjNVKvdUEpl7pFgra62qG5CgNjVvnr-5sOuOl8W2HthmSGFIQwLlWcjT2DfpFF3M1UArS42ZjANkt8bFJq4ni3_=w1374-h1054-no?authuser=0" width="80%"></p>
This is a backend of MiniCRM implemented on aiohttp. Currently, there are only five types of requests.

After starting the server, you can view them in:
Swagger UI at http://localhost:8080/docs#/

or RAW json at http://localhost:8080/docs/json


## How to.

- Add the cookie secret key and administrator credentials to the config.yaml.
- Then you can log in and use the rest of the methods.

## About the project.

- Aiohttp-session is used for authorization. https://github.com/aio-libs/aiohttp-session
- For now, the data is stored in the instance and is erased after the server is stopped. But I'm working on adding postgresql.

## Project setup
You need python 3.7+ to run it.
After cloning the repository run:
```
bash start.sh
```