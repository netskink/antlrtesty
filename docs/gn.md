# gn


## Commands

### Getting help

* gn help gen
* gn help dotfile

### Building Ninja Files

* gn gen out

Generates ninja files from the current tree and puts them in the given output directory - out/.  See `$ gn help gen`

```
$ gn gen out
```


### Cleaning gn output - removing ninja files


This command will also delete the ninja build results.  It will
preserve some gn output files though.  For instance, these files
will persist:

```
$ gn clean out
```

* out/args.gn
* out/build.ninja.d
* out/build.ninja


### Notable gn options

* gn -v xxxx to run in verbose mode


## Components

Essential files to create a ninja project

* .gn is the top level file that identifies a gn project.  It is at the root of the project.
* BUILD.gn are in each directory of the project
* BUILDCONFIG.gn

## creating a simple C++ build

Use this directory to demo a tiered c++ build. 

* src/gncc/

Need to make sure you use spaces and not tabs

### Command Sequence

```
$ cd src/gncc
# set environment
$ . /workspaces/antlrtesty/bin/setenv.sh 
# use gn to generate ninja files
$ gn gen out
# build source using ninja
$ ninja -C out tutorial 
# Test run the result
$ ./out/tutorial 
```




### Contents:

#### Required

```
src/gncc/.gn                   <-   copied from gn/examples/simple_build
src/gncc/build/                <-   transcribed from gn quickstart url
src/gncc/build/BUILD.gn        <-   transcribed from gn quickstart url
src/gncc/build/BUILDCONFIG.gn  <-   ditto
src/gncc/toolchain/BUILD.gn    <-   copied from gn/examples/simple_build
src/gncc/tutorial/BUILD.gn     <-   copied from gn/examples/simple_build
src/gncc/tutorial/tutorial.cc. <-   copied from gn/examples/simple_build
```

#### Generated

Stuff created by `gn gen out`

```
src/gncc/out                   
src/gncc/out/args.gn
src/gncc/out/build.ninja
src/gncc/out/build.ninja.d
src/gncc/out/build.ninja.stamp
src/gncc/out/obj
src/gncc/out/obj/tutorial
src/gncc/out/obj/tutorial/tutorial.ninja

```

Stuff created by `ninja`

You can do either command sequence and the result is the same

* `ninja -C out`
* `ninja -C out tutorial`



```
out/.ninja_log
out/.ninja_deps
out/build.ninja.stamp
out/tutorial
out/obj/tools.stamp 
out/obj/tutorial/tutorial.tutorial.o
```


## src/gncc/BUILD.gn

Sample quick start files.  These all came from the quickstart [step by step]([Title](https://gn.googlesource.com/gn/%252B/main/docs/quick_start.md#Step_by_step))


```
group("tools") {
  deps = [
    # This will expand to name "//tutorial:tutorial" which is the full name
    # of our new target.  Run "gn help labels" for more.
    "//tutorial",
  ]
}
```

## src/gncc/tutorial/BUILD.gn

This also came from the quickstart guide

```
executable("tutorial") {
  sources = [
    "tutorial.cc",
  ]
}
```

## src/gncc/build/BUILD.gn

```
config("compiler_defaults") {
  if (current_os == "linux") {
    cflags = [
      "-fPIC",
      "-pthread",
    ]
  }
}

config("executable_ldconfig") {
  if (!is_mac) {
    ldflags = [
      "-Wl,-rpath=\$ORIGIN/",
      "-Wl,-rpath-link=",
    ]
  }
}
```

## src/gncc/build/BUILDCONFIG.gn

```
if (target_os == "") {
  target_os = host_os
}
if (target_cpu == "") {
  target_cpu = host_cpu
}
if (current_cpu == "") {
  current_cpu = target_cpu
}
if (current_os == "") {
  current_os = target_os
}

is_linux = host_os == "linux" && current_os == "linux" && target_os == "linux"
is_mac = host_os == "mac" && current_os == "mac" && target_os == "mac"

# All binary targets will get this list of configs by default.
_shared_binary_target_configs = [ "//build:compiler_defaults" ]

# Apply that default list to the binary target types.
set_defaults("executable") {
  configs = _shared_binary_target_configs

  # Executables get this additional configuration.
  configs += [ "//build:executable_ldconfig" ]
}
set_defaults("static_library") {
  configs = _shared_binary_target_configs
}
set_defaults("shared_library") {
  configs = _shared_binary_target_configs
}
set_defaults("source_set") {
  configs = _shared_binary_target_configs
}

set_default_toolchain("//build/toolchain:gcc")

```