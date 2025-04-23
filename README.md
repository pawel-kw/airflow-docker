# Running Airflwo in Docker

This project is based on the [basic Airflow How-To guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html). Read the quide for details of the configuration.

## Running on Mac

To avoid any issues with running Docker Desktop, you can use colima.

### Install colima, docker and docker-compose

Install colima:

`brew install colima`

Install Docker:

`brew install docker`

Install Docker compose:

`brew install docker-compose`

Add some configuration snippet to your `~/.docker/config.json` so docker finds the compose plugins: 

``` "cliPluginsExtraDirs": [ "/opt/homebrew/lib/docker/cli-plugins" ] ```

### Start colima

By default, colima will only allocate 2GB of RAM for docker images, which is not sufficient to run Airflow. This can be modified by running colima with `--memory` argument:

`colima start --memory 8`

Now 8GB of memory should be available for your docker images. You can make sure by running the following command:

`docker run --rm "debian:bookworm-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'`

### Initializing Airflow

This needs to be done before starting Airflow for the first time to create the necessary files, directories and initialize the database.

#### Setting the right Airflow user

`echo -e "AIRFLOW_UID=$(id -u)" > .env`

#### Initialize the database

`docker compose up airflow-init`

This will take a while. Once it's done, you should see a message like this:

```
airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.10.5
start_airflow-init_1 exited with code 0
```

The account created has the login `airflow` and the password `airflow`.

### Running Airflow

To start all the services:

`docker compose up`

Airflow web interface should now be available under http://localhost:8080.

The local `./dags` folder is mounted as a volume to the Docker image - any dags placed there will be parsed and available in the running Airlow instance.

