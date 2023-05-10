.PHONY: all python

all: python

python:
	protoc -I=proto --python_out=python/visionapi/visionapi proto/*.proto