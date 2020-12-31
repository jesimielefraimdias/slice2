# Pull ubuntu image
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python3-dev libmysqlclient-dev build-essential -y
RUN apt-get install mysql-server
RUN systemctl start mysql
RUN mysql



# Define default command
CMD bash /data/startup.sh

# Expose ports
EXPOSE 5000