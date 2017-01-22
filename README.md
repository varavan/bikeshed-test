# BikeShed

This project is a demostration about django. The point is to create a Bike CRM where registered users can register new Bikes and everybody can consult the database


## Requirements

- [docker](https://www.docker.com/)

## Usage

In order to run the app on development mode ( no production environment provided) just run `docker-compose up` on root directory.
This will create a container that exposes the app on port `8000` so to access the app just do `http://{IP_DOCKER}:8000`

On start container `bikeshed/run.sh` is executed and a bunch of bikes along with a demo user are automatically created

Demo user **demo** / **demo**

## Testing

To run test with docker execute `docker-compose run test`.
