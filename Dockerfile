FROM python:3.7

COPY . /web
WORKDIR /web
RUN pip install -r ./Requirements.txt
ENTRYPOINT ["python"]
CMD ["/web/Database/sqlite_create.py"]