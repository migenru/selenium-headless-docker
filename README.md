# Headless Selenium (Docker Selenium)

## Prepare host
 - Install Docker (https://docs.docker.com/engine/install/) 
 - Install docker-compose (https://docs.docker.com/compose/install/)

## Run

1. Clone repository: ```git clone https://github.com/migenru/selenium-headless-docker.git scraper```
2. Open folder: `cd scraper`
3. Run docker-compose.yml: ```docker-compose up --build```


## Description components

* `.env.docker` - variable for settings.
  * POSTGRES_HOST - ip-address for Postgres
  * POSTGRES_PORT - port Postgres
  * POSTGRES_DB - name database Postgres
  * POSTGRES_USER - username Postgres
  * POSTGRES_PASSWORD - password Postgres
  * TZ - Time TZ
* `Dockerfile` - Container Python + Selenium + Firefox
* `docker-compose` - services of system: Python + Postgres containers
* `run.sh` - run file for scraper
* 

