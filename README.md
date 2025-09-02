# Vision API repository

This repo contains the main data model for the Starwit Awareness Engine (SAE). See umbrella repo here: https://github.com/starwit/starwit-awareness-engine

## How-To Use

### Python / Poetry
- Add the following to your `pyproject.toml` dependencies section\
    `visionapi = { git = "https://github.com/starwit/vision-api.git", subdirectory = "python/visionapi", tag = "3.5.2" }`
    
### Java / Maven
- Add dependency to your project:
    ```xml
    <dependency>
      <groupId>de.starwit</groupId>
      <artifactId>vision-api</artifactId>
      <version>3.5.2</version>
    </dependency>
    ```
- Add maven repository to your `~/.m2/settings.xml` (adapt example / your config as necessary):
    ```xml
    <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
                        http://maven.apache.org/xsd/settings-1.0.0.xsd">

    <activeProfiles>
        <activeProfile>github</activeProfile>
    </activeProfiles>

    <profiles>
        <profile>
        <id>github</id>
        <repositories>
            <repository>
            <id>central</id>
            <url>https://repo1.maven.org/maven2</url>
            </repository>
            <repository>
            <id>github</id>
            <url>https://maven.pkg.github.com/starwit/vision-api</url>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
            </repository>
        </repositories>
        </profile>
    </profiles>

    <servers>
        <server>
            <id>github</id>
            <username>YOUR_GITHUB_USER</username>
            <password>GITHUB_TOKEN_WITH_PACKAGE_READ_PERMISSIONS</password>
        </server>
    </servers>
    </settings>

    ```

## Tools & Setup

* Install protoc via pipx:
    ```
    sudo apt install pipx
    pipx install protoc-wrapper==31.1.0
    ```
* ! If you change protoc version, you need to change protobuf version in `java\visionapi\pom.xml`, `python\visionapi\pyproject.toml` and protoc version in `Makefile`

## How-To Update
1. Make desired changes in `./visionapi`
2. Increase version in `./VERSION`
3. Run `make`
4. Make sure that there are no old leftover files in the generated projects
5. Describe change in changelog section below
5. Commit, tag with version and push
    ```
    // Commit stuff, like git add, git commit and such
    git tag <version_tag>
    git push
    git push <version_tag>
    ```

## Changelog
### 3.5.1
- Add `class_name` to `DetectionCount`

### 3.5.0
- Add `ModelMetadata` containing `class_names` mapping to `SaeMessage`

### 3.4.0
- Add `MessageType` field `type` to all top-level messages
- Add `TypeMessage` as a dummy to deserialize type field

### 3.3.0
- Add `PositionMessage` to represent position information from a GNSS receiver

### 3.2.1
- Add `DetectionCountMessage` to summarize detection data

### 3.2.0
- Add `source_id` to messages (to distinguish which source the messages are generated from)
    - Add `IncidentMessage.source_id`
    - Add `AnomalyMessage.source_id`

### 3.1.0
- Add camera location field to all messages (as type `GeoCoordinate`)
    - Add `SaeMessage.frame.camera_location`
    - Add `AnomalyMessage.camera_location`
    - Add `IncidentMessage.camera_location`