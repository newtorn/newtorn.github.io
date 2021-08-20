#!/bin/bash

branch=hexo
github=git@github.com:newtorn/newtorn.github.io.git
gitee=git@gitee.com:newtorn/newtorn.git

set -ue

git checkout $branch
git add .
git commit -m "backup"

git push $github --force
git push $gitee --force