FROM python:3.13.0
COPY . /app
# WORKDIR /app/app
WORKDIR /app
# RUN pip3 install -r ../requirements.txt
RUN pip3 install -r requirements.txt
ENV RUNNING_IN_DOCKER=true
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD ["-u" , "main.py"]