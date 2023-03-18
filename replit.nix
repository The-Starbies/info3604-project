{ pkgs }: {
  deps = [
    pkgs.python39Packages.pip
    pkgs.python39Packages.pip
    pkgs.flask
    pkgs.python39Packages.bootstrapped-pip
    pkgs.python39Packages.flask
    pkgs.sudo
    pkgs.sudo
    pkgs.pip install flask
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server  
  ];
}