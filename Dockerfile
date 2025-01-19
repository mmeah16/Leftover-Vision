FROM python:3.13.0
COPY . /app
WORKDIR /app/app
RUN pip3 install -r ../requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD ["-u" , "main.py"]