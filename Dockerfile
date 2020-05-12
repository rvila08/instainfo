FROM python:3

ADD hashtagsearch.py /

RUN pip install flask

CMD [ "python", "./hashtagsearch.py" ]
