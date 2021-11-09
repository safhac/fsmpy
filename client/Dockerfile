FROM python:3.10 AS compile-image

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /deploy

COPY setup.py .

RUN pip install --upgrade pip && \
    pip install .

FROM python:3.10 AS build-image
COPY --from=compile-image /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

CMD ['client']
