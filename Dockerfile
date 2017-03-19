FROM centos:latest
MAINTAINER mrbarge "mattbargenquast@gmail.com"
RUN yum update -y ; yum clean all
RUN yum install -y epel-release ; yum clean all
RUN yum install -y python python34-pip 

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

ENV FLASK_CONFIG /data/flaskdemo/flaskdemo.conf

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["flaskdemo/flaskdemo.py"]
