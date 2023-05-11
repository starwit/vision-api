.PHONY: all python

all: clean python

clean:
	rm -f python/visionapi/proto/*pb2.py*

python:
	protoc -I=. --python_out=python/visionapi/ --pyi_out=python/visionapi/ proto/*.proto