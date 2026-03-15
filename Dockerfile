FROM python:3.14.3

# Prevent python buffering
ENV PYTHONUNBUFFERED=1

# Create non-root user
RUN useradd -m appuser
USER appuser

COPY . /usr/bank_note_authentication_app


WORKDIR /usr/bank_note_authentication_app
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements-build.txt

# Cloud Foundry provides PORT env variable
ENV PORT=5000
EXPOSE ${PORT}

# Start FastAPI server
CMD python3 -m uvicorn app.run:app --host 0.0.0.0 --port ${PORT}