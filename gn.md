


# gn

Starter commands:

* gn help gen
* gn help dotfile
* touch .gn
* gn gen out


## Components

* .gn is the top level file that identifies a gn project.  It is at the root of the project.
* BUILD.gn are in each directory of the project
*

## creating a simple C++ build

Use this directory
* examples/simple_build/

Need to make sure you use spaces and not tabs

### Contents:

```
examples/simple_build/.gn      <-   copied from gn/examples
examples/build/
examples/build/BUILD.gn
examples/build/BUILDCONFIG.gn  <-   referenced by .gn file
examples/toolchain/BUILD.gn    <-   copied from gn/examples

```

## simple_build/BUILD.gn

[This came from the quickstart step by step]([Title](https://gn.googlesource.com/gn/%252B/main/docs/quick_start.md#Step_by_step))


```
group("tools") {
  deps = [
    # This will expand to name "//tutorial:tutorial" which is the full name
    # of our new target.  Run "gn help labels" for more.
    "//tutorial",
  ]
}
```

## simple_build/tutorial/BUILD.gn

This also came from the quickstart guide

```
executable("tutorial") {
  sources = [
    "tutorial.cc",
  ]
}
```

## simple_build/build/BUILD.gn

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

## simple_build/build/BUILDCONFIG.gn

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