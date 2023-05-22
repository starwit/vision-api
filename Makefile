.PHONY: all python rust

all: clean python rust

clean:
	rm -f python/visionapi/visionapi/*pb2.py*
	rm -f rust/visionapi/src/*.rs

python:
	protoc -I=. --python_out=python/visionapi/ --pyi_out=python/visionapi/ visionapi/*.proto

rust:
	(cd rust/visionapi && cargo build)