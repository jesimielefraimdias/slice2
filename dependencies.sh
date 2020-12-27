sudo apt-get install mysql-server -y
systemctl start mysql
sudo mysql
create database slice2;
exit

python3 -m venv slice2-env
cd slice2-env
source bin/activate
python -m pip install -r requirements.txt
cd src
python
from App import db
db.create_all()
exit()
