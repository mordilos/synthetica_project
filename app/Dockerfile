FROM python:3

WORKDIR /usr/src/app

# copy and install the requirements.txt 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# start the my_app.py script
CMD [ "python", "./my_app.py" ]
