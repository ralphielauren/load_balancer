# LOAD BALANCER
This project is just a dummy load balancer to help me understand the different ways that LBs work.

It is written in Python.

It is not supposed to be a sophisticated project, just an exploration based on different demos, 
tutorials and ideas I read online about and want to try out to understand.

## Structure
Using the `docker-compose.yaml`, create 2 apps `apple` and `cat`. In the tests folder,
use `test_client` for the the load balancer app and depending on the hosts, or paths of the 
request, hit the appropriate dockerised app. 

## Installing
On root dir, run:
```shell script
make install
```

## Tests
On root dir, run:
```shell script
make test
```

