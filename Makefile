.PHONY: all python

all: clean python

clean:
	rm -f python/visionapi/visionapi/proto/*pb2.py*

python:
	protoc -I=. --python_out=python/visionapi/visionapi --pyi_out=python/visionapi/visionapi proto/*.proto