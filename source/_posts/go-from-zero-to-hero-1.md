---
title: go from zero to hero(1)
date: 2020-10-22 16:00:43
tags:
- go
- golang
categories:
- golang从零大神
- go from zero to hero
---

Golang: simplicity is complicated!
>Let’s start with a small introduction to Go (or Golang). Go was designed by Google engineers Robert Griesemer, Rob Pike, and Ken Thompson. It is a statically typed, compiled language. The first version was released as open source in March 2012.
>

>“Go is an open source programming language that makes it easy to build simple, reliable, and efficient software”. — GoLang
>

Next, I take you to learn golang from zero to hero!

### Installation
From package manager
```shell
# Linux(Redhat/CentOS)
yum install go

# macOS
brew install go

# Windows
scoop install go
```
From binary package
```
download golang installer from `https://golang.org/dl/`
```

### Code
Create a file named which you like, example: `main.go`, edit it:
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

### Run
```shell
go run main.go
```
Congratulations! 
Under command line you will see this:
```
Hello World
```