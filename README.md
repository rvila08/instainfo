# InstaInfo

A project using Facebook for Developers' Instagram Graph API (more specifically features needed to use the hashtag search) coded in python. See [hashtagsearch.py](https://github.com/rvila08/instainfo/blob/master/hashtagsearch.py) and [info.py](https://github.com/rvila08/instainfo/blob/master/info.py) for this code. We also have an HTML page, [instainfo.html](https://github.com/rvila08/instainfo/blob/master/templates/instainfo.html) that implements Flask functionality to interact with the aforementioned python code. 

## Instructions for Implementation With Docker

* Clone into this repository
* Run the command `docker build --tag [insert name here]`.
* Then run `docker run --name [insert name here] -p 5000:5000 [insert name here]`.
  * This will open a Flask server on your local host.
* Navigate to http://0.0.0.0:5000/ to now see [instainfo.html](https://github.com/rvila08/instainfo/blob/master/templates/instainfo.html) in full effect.
* One can know enter any hashtag into the text box and after submitting will be redirected to the most popular Instagram page containing that hashtag.


## Instructions for Implementation Without Docker

* Clone into this repository
* Run the command `python3 hashtagsearch.py`.
  * This will open a Flask server on your local host.
* Navigate to http://0.0.0.0:5000/ to now see [instainfo.html](https://github.com/rvila08/instainfo/blob/master/templates/instainfo.html) in full effect.
* One can know enter any hashtag into the text box and after submitting will be redirected to the most popular Instagram page containing that hashtag.

## Information

Group Members: Justin Bindi, Ethan Dang, James Romero, John Savage, Ricky Vila


CPSC 353 


Dr. Micheal Fahy


12 May 2020
