#proxy=http://192.168.9.196:3128
yum clean all
yum clean metadata
yum install -y gcc python-pip python-devel libyaml
pip --trusted-host pypi.python.org --proxy=$proxy install --upgrade pip
pip --trusted-host pypi.python.org --proxy=$proxy install --upgrade virtualenv
virtualenv venv
source ./venv/bin/activate
pip --trusted-host pypi.python.org --proxy=$proxy install --upgrade -r requirements/production.txt
deactivate
virtualenv --relocatable venv
