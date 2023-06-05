# Vision API repository

## How-To Update
1. Make desired changes in `./visionapi`
2. If you have added or deleted `*.proto` files in step 1, adapt the Rust related files accordingly (in the Makefile and build.rs)
3. Run `make`
4. Make sure that there are no old leftover files in the generated projects
5. Increment the package versions of all files
  a. `./rust/Cargo.toml`
  b. `./python/pyproject.toml`
  c. `./java/pom.xml`
6. Commit, tag with version and push


## Tools & Setup
ProtoBuf compiler can be downloaded here:
https://github.com/protocolbuffers/protobuf/releases