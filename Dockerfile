FROM python:3.14.3
COPY . /usr/bank_note_authentication_app
EXPOSE 5000
WORKDIR /usr/bank_note_authentication_app
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements-build.txt
CMD python3 -m uvicorn app.run:app --host 0.0.0.0 --port 5000