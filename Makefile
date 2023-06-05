.PHONY: all python rust java

all: clean python rust java

clean:
	rm -f python/visionapi/visionapi/*pb2.py*
	rm -f rust/visionapi/src/messages.rs
	rm -f java/visionapi/src/main/java/de/starwit/visionapi/*.java

python:
	protoc -I=. --python_out=python/visionapi/ --pyi_out=python/visionapi/ visionapi/*.proto

rust:
	(cd rust/visionapi && cargo build)

java:
	protoc -I=. --java_out=java/visionapi/src/main/java/ visionapi/*.proto