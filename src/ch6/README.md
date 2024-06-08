
# notes on chapter 6


# URLS

* [ninja manual](https://ninja-build.org/manual.html#_comparison_to_make)
* [ninja guide](https://spectra.mathpix.com/article/2024.01.00364/a-complete-guide-to-the-ninja-build-system)

# Usage

Replace ch4/tour with whatever you wish: tour, tour2, ...

```
$ cd bin
$ . ./setenv.sh
$ cd ..
$ cd src/ch4/tour
$ ninja
```

## List available targets

```
$ ninja -t targets
```

## Run a particular target

```
$ ninja do_test3
```

## Clean all targets

```
$ ninja -t clean
```
