FROM python:3.11-slim

# Prevent python buffering
ENV PYTHONUNBUFFERED=1

# Create non-root user with numeric UID
RUN useradd -u 1000 -m appuser

# Create working directory
WORKDIR /usr/bank_note_authentication_app

# Copy application code
COPY . .

# Install dependencies
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements-build.txt

# Change ownership to non-root user
RUN chown -R 1000:1000 /usr/bank_note_authentication_app

# Switch to non-root user
USER 1000

# Expose port optional but recommended for clarity
EXPOSE 8080

# Start FastAPI server
CMD ["sh", "-c", "python -m uvicorn app.run:app --host 0.0.0.0 --port ${PORT:-8080}"]