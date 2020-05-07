# tum-rbg2player
A small tool to extract raw video URLs from live.rbg.tum.de streams and VODs and open them in a preferred desktop player via the command line. Also supports the selection of different views (combined, only camera, only presentation).


### Installation

#### Dependencies

`rbg2player` requires Python 3 or later.

#### Install using `pip`

```
pip install git+https://github.com/max-ae/tum-rbg2player
```

#### Upgrade using `pip`

```
pip install -U git+https://github.com/max-ae/tum-rbg2player
```

### Usage

#### Cmdline options

```
Usage: rbg2player [OPTIONS] URL

Options:
  -p, --player TEXT               command that is executed to invoke the
                                  player, defaults to VLC

  -v, --view [combined|camera|presentation]
                                  view to open
  --help                          Show this message and exit.
```
#### Configuration file

There are none. Setting default players or views is supported via aliases in your shell.

For example, the following alias for bash/zsh/etc.

    alias rbg2player='rbg2player -v presentation'

leads to loading the presentation view per default. 

These aliases can be overridden by simply providing a different option.
 
### Examples

1. Opens the provided URL in the default player VLC, with the default combined view.

    ```
    $ rbg2player <URL>
   ```
1. Opens the provided URL in the default player VLC, with only the presentation view.

    ```
    $ rbg2player -v presentation <URL>
   ```
3. Opens the provided URL in the player IINA, with the default combined view.

    ```
    $ rbg2player -p iina <URL>
   ```