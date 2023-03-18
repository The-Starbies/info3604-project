{ pkgs }: {
  deps = [
    pkgs.sudo
    pkgs.sudo
    pkgs.pip install flask
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server  
  ];
}