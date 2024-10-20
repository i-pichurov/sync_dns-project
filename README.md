# Required

Python: 3.12.3\

    python3 --version

Pip: 24.0\ - ставится вместе с питоном

    python3 -m pip --version

Poetry: 1.8.3

    poetry --version
    
- ставится так: https://github.com/python-poetry/install.python-poetry.org
- или так: https://python-poetry.org/docs/#installing-with-pipx
  
pipx (если в системе стоит Homebrev)
ставится так:

    brew install pipx
    pipx ensurepath

# Installing

Copy the contents of the repository:
    
    git clone git@github.com:i-pichurov/sync_dns-project.git
    
Install the package using the command in the Makefile:
    
    make package-install
    or 
    pipx install dist/*.whl (если в системе стоит Homebrev)

After installing the package use:

    check_dns 'domain' 'dns_record_type(UPPERCASE)' 'dns_record_name'
    or
    check_dns -h 
