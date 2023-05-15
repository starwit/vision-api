.PHONY: all python

all: clean python

clean:
	rm -f python/visionapi/visionapi/*pb2.py*

python:
	protoc -I=. --python_out=python/visionapi/ --pyi_out=python/visionapi/ visionapi/*.proto