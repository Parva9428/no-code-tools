# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python39Packages
    pkgs.nodejs_20
    # pkgs.go
    # pkgs.python311
    # pkgs.python311Packages.pip
    # pkgs.nodejs_20
    # pkgs.nodePackages.nodemon
  ];

  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      # "vscodevim.vim"
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
        # web = {
        #   # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
        #   # and show it in IDX's web preview panel
        #   command = ["npm" "run" "dev"];
        #   manager = "web";
        #   env = {
        #     # Environment variables to set for your server
        #     PORT = "$PORT";
        #   };
        # };
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
         "backend-flask-install" = ''
      cd backend/flask_app
      pip install -r requirements.txt
    '';
    "backend-fastapi-install" = ''
      cd backend/fastapi_app
      pip install -r requirements.txt
    '';
    "frontend-install" = ''
      cd frontend
      npm install
    '';
        # Example: install JS dependencies from NPM
        # npm-install = "npm install";
      };
      # Runs when the workspace is (re)started
      onStart = {
       "backend-flask" = ''
    cd backend/flask_app
    export FLASK_APP=app.py
    nohup python app.py > backend_flask.log 2>&1 &
  '';
  "backend-fastapi" = ''
    cd backend/fastapi_app
    nohup gunicorn -w 4 -k uvicorn.workers.UvicornWorker fastapi_app.app:app > backend_fastapi.log 2>&1 & 
  '';
  "frontend" = ''
    cd frontend
    nohup npm run dev > frontend.log 2>&1 &
  '';
        # Example: start a background task to watch and re-build backend code
        # watch-backend = "npm run watch-backend";
      };
    };
  };
}
