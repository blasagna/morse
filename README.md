# morse
Morse code decoding using [golang](https://golang.org/).

## dependencies
[Download and install](https://golang.org/dl/) golang.

## install
You can install the morse package using [`go get`](https://golang.org/cmd/go/#hdr-Download_and_install_packages_and_dependencies):
```golang
go get github.com/blasagna/morse
```

## command line runner
There is a command line executable which uses the morse library in cli/

It also depends on termbox, which you can install using `go get github.com/nsf/termbox-go`

## learning Morse code

There are many resources out there for learning Morse code, but one good one is [Hello Morse](https://experiments.withgoogle.com/collection/morse).

Extensions to Morse code are included for:
* space     dot-dot-dash-dash
* backspace dash-dash-dash-dash

## run tests
Run `go test` from the morse/ directory to run all unit tests.

## TODO
* configure input at runtime:
  * keyboard keys or mouse clicks
  * set inputs for dot and dash

