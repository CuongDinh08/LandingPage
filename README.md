# LandingPage

LandingPage is an light-weigth and simple website to check if your server is working correctly.

## Pre-requirements

If you want to install this website manually, you need to have:

- Python 3.10.12
- pip 22.0.2
- gunicorn 20.1.0
- python3-venv (optional)


```bash
sudo apt-get update
sudo apt-get install python3 python3-pip gunicorn
sudo apt-get install python3-venv # optional
```

If you want to install through Docker and Docker-compose, you need to have:

- docker (optional)

```bash
sudo apt-get update
sudo apt-get install docker docker-compose
```

## Set up settings

Create ```server_settings.py``` at the same directory of ```settings.py```.

Create attributes: ```SECRET_KEYS```, ```ALLOWED_HOSTS```, ```SERVER_NAME```.

You can view ```sample_server_settings.py``` for an example.

## Manual installation

### Activate virtual environment (optional)

If you already install ```python3-venv```, you can create a virtual environment and activate it.

```bash
python3 -m venv env
source env/bin/activate
```

### Install required modules and libraries

You need to install required modules and libraries before going further.

```bash
pip3 install -r requirements.txt
```

### Run gunicorn

By default, the project will be host at port ```8000```. Change port at attribute ```bind``` at ```gunicorn.py```.

```bash
gunicorn -c gunicorn.py
```

### Stop gunicorn

You can get the PID of current gunicorn from ```/var/run/gunicorn/landingpage.pid```:

```bash
cat /var/run/gunicorn/landingpage.pid
```

With the PID, you can stop the process by command:

```bash
sudo kill -9 <PID>
```
### Read gunicorn logs

You can read the project logs at ```/var/log/gunicorn/landingpage.log```:

```bash
vim /var/log/gunicorn/landingpage.log
```

## Install from Docker-compose

```bash
sudo docker-compose up -d
```
