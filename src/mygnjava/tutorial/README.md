Notes on the simple java app

## compile

```
$ javac Tutorial.java
```

## Run

```
$ java Tutorial
```


## a build.ninja

This `build.ninja` file does what I want.

```
cc = javac
out = out

# use cc to make .class files in out dir
rule cc
  command = $cc -d $out $in
build $out/Tutorial.class: cc tutorial/Tutorial.java
```

Use like so:

```
$ out=out ninja
```

It will use the src/Tutorial.java and build the class file in the out dir.