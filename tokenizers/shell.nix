{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = with pkgs; [
	cargo
	rustc
	rustfmt
	criterion
    (python3.withPackages (ps: with ps; [
      memory-profiler
    ]))
  ];

RUSTFLAGS = "-C target-cpu=native";

}
