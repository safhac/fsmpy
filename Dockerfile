FROM python:3.10

ADD . /deploy
WORKDIR /deploy

RUN cd /deploy
RUN pip install --upgrade pip
RUN pip install .
RUN echo 'installed' > deplog
RUN rm -rf /build /deploy
CMD ["program"]