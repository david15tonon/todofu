FROM python:3

# Set the working directory
WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install --nocache-dir --upgrade -r ./requirements.txt

EXPOSE 3001

CMD ["python", ".src/server.py"]