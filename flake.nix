{
  description = "A Nix-flake-based Python development environment";

  inputs.nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.1.*.tar.gz";

  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      devShells = forEachSupportedSystem ({ pkgs }: {
        default = pkgs.mkShell {
          venvDir = "venv";
          buildInputs = [
            pkgs.glfw
            pkgs.libGL
            pkgs.libGL.dev
            pkgs.stdenv.cc.cc.lib
            pkgs.libevdev
          ];
          postShellHook = ''
            export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pkgs.lib.makeLibraryPath[
              pkgs.glfw
              pkgs.libGL
              pkgs.libGL.dev
              pkgs.stdenv.cc.cc.lib
              pkgs.libevdev
            ]};
          '';
          packages = with pkgs; [ 
            python312 
          ] ++
            (with pkgs.python312Packages; [ 
              pip
              venvShellHook 
            ]);
        };
      });
    };
}
