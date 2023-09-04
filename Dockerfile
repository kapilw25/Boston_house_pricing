FROM python:3.7 # use python 3.7 as the base image
COPY . /app # copy all files from current directory to /app in the container
WORKDIR /app # set /app as the working directory
RUN pip install -r requirements.txt # install all dependencies
EXPOSE $PORT # expose the port 5000 to the outside world
CMD gunicon --workers ==4 --bind 0.0.0.0:$PORT app:app # run the command to start app.py when the container launches
```