FROM python:3.8.6-buster
COPY model.joblib /model.joblib
COPY memobrainmodel /memobrainmodel
COPY api /api
COPY requirements.txt /requirements.txt
COPY /path/to/your/credentials.json /credentials.json
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
