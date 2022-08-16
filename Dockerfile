FROM python:3.10
COPY /workdir /workdir
WORKDIR workdir
RUN pip install --no-cache-dir --upgrade -r requirements.txt && python pull_nlp_models.py
CMD ["uvicorn", "backend_fastapi:app", "--host", "0.0.0.0", "--port", "80"]