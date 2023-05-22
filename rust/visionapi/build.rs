use std::{path::PathBuf, env, process::Command};

fn main() {
    let proto_output = PathBuf::from(env::var("OUT_DIR").unwrap()).join("visionapi");
    let proto_target = PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap()).join("src");

    // Use this in build.rs
    protobuf_codegen::Codegen::new()
        // Use `protoc` parser, optional.
        .protoc()
        // Use `protoc-bin-vendored` bundled protoc command, optional.
        //.protoc_path(&protoc_bin_vendored::protoc_bin_path().unwrap())
        // All inputs and imports from the inputs must reside in `includes` directories.
        .includes(&["../.."])
        // Inputs must reside in some of include paths.
        .input("../../visionapi/videosource.proto")
        .input("../../visionapi/detector.proto")
        .input("../../visionapi/tracker.proto")
        // Specify output directory relative to Cargo output directory.
        .cargo_out_dir("visionapi")
        .run_from_script();

    Command::new("cp")
        .arg("-rf")
        .arg(proto_output)
        .arg(proto_target)
        .output().unwrap();
}
