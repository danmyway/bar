# BAR
Build alias resolver

## Usage
```commandline
usage: main.py [-h] [-o OWNER] project package reference

Returns copr build ID based on alias contained in package version.

positional arguments:
  project               Specify, under which project to look for the package build ID.
  package               Specify, which package to get the build ID for.
  reference             Specify a string for which to look for in the NVR.

options:
  -h, --help            show this help message and exit
  -o OWNER, --owner OWNER
                        Define required package build owner.
                        Default: @oamg

```
