# Vision API repository

## How-To Update
1. Make desired changes in `./visionapi`
2. If you have added or deleted `*.proto` files in step 1, adapt the Rust related files accordingly (in the Makefile and build.rs)
3. Run `make`
4. Make sure that there are no old leftover files in the generated projects
5. Increment the package versions of all files
    * `./rust/Cargo.toml`
    * `./python/pyproject.toml`
    * `./java/pom.xml`
6. Commit, tag with version and push
    ```
    git commit
    git tag <version_tag>
    git push
    git push <version_tag>
    ```



## Tools & Setup
ProtoBuf compiler can be downloaded here:
https://github.com/protocolbuffers/protobuf/releases