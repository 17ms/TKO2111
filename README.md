# TKO2111 course assignment

[In-depth documentation of the assignment (in Finnish)](docs/DOCUMENTATION.md)

### Usage

Setup:

```shell
git clone git@github.com:17ms/TKO2111.git
cd tko2111

mkvirtualenv tko2111 # optional, requires virtualenwrapper
python3 -m pip install -r requirements.txt
chmod +x app.py
```

Run as a client:

```shell
./app.py --filename example.json --client
```

Run as an admin:

```shell
./app.py --filename example.json --admin
```

### Internal commands

Client:

```
usage: [list | ticket | help | quit] <ARGUMENTS>

commands:
  list      SECTION      list all data entries of a section
  ticket    ID VIEWER    book a ticket into a screening
  help                   show this help message
  quit                   exit the app
```

Admin:

```
usage: [list | add | edit | delete | help | quit] <ARGUMENTS>

commands:
  list      SECTION             list all data entries of a section
  add       SECTION             add a new entry into a section
  edit      SECTION ID FIELD    edit a field of a section entry
  delete    SECTION ID          delete an entry from a section
  help                          show this help message
  quit                          exit the app
```

### General assignment requirements

- Written in Python
- Contains at least 5 functions
- Writes and reads data to a file
- Contains at least 100 lines of code in total
- Utilizes lists and dictionaries
