FROM python:3.9

WORKDIR /app

COPY ./main.py .
COPY ./requirements.txt .

RUN pip install --upgrade pip 
RUN pip install fastapi
RUN pip install uvicorn

# CMD ["sleep", "200000"]
CMD ["uvicorn", "main:app", "--reload"]