VERSION := $(shell cat VERSION)
REQUIRED_PROTOC_VERSION := 31.1

.PHONY: all python java readme check-protoc-version

all: check-protoc-version clean python java readme

check-protoc-version:
	@INSTALLED_VERSION=$$(protoc --version | awk '{print $$2}'); \
	if [ "$$INSTALLED_VERSION" != "$(REQUIRED_PROTOC_VERSION)" ]; then \
		echo "Error: protoc version $(REQUIRED_PROTOC_VERSION) required, but $$INSTALLED_VERSION is installed."; \
		exit 1; \
	fi

clean:
	rm -f python/visionapi/visionapi/*pb2.py*
	rm -f java/visionapi/src/main/java/de/starwit/visionapi/*.java

python: check-protoc-version
	protoc -I=. --python_out=python/visionapi/ --pyi_out=python/visionapi/ visionapi/*.proto
	(cd python/visionapi && poetry version $(VERSION))

java: check-protoc-version
	protoc -I=. --java_out=java/visionapi/src/main/java/ visionapi/*.proto
	(cd java/visionapi && mvn versions:set -DgenerateBackupPoms=false -DnewVersion=$(VERSION))

readme:
	sed -E 's|tag = "[0-9\.]+"|tag = "$(VERSION)"|' -i README.md
	sed -E 's|<version>[0-9\.]+</version>|<version>$(VERSION)</version>|' -i README.md