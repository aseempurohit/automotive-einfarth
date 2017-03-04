
tag = car-network
ports = -p 5002:50024

init:
	git submodule update --init 

build:
	docker build -t $(tag) ./

runinteractive: stop
	docker run -it --name=$(tag) $(ports) $(tag)
	
run: stop
	docker run -d --name=$(tag) $(ports) $(tag)
	
	
stop:
	docker stop $(tag) || echo "$(tag) not running"
	docker rm $(tag) || echo "$(tag) container not found"

test:
	python tests.py
