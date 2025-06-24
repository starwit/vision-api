VERSION := $(shell cat VERSION)

.PHONY: all python java readme

all: clean python java readme

clean:
	rm -f python/visionapi/visionapi/*pb2.py*
	rm -f java/visionapi/src/main/java/de/starwit/visionapi/*.java

python:
	protoc -I=. --python_out=python/visionapi/ --pyi_out=python/visionapi/ visionapi/*.proto
	(cd python/visionapi && poetry version $(VERSION))

java:
	protoc -I=. --java_out=java/visionapi/src/main/java/ visionapi/*.proto
	(cd java/visionapi && mvn versions:set -DgenerateBackupPoms=false -DnewVersion=$(VERSION))

readme:
	sed -E 's|tag = "[0-9\.]+"|tag = "$(VERSION)"|' -i README.md
	sed -E 's|<version>[0-9\.]+</version>|<version>$(VERSION)</version>|' -i README.md