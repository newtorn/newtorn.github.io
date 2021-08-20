#!/bin/bash

branch=hexo
github=git@gitee.com:newtorn/newtorn.github.io.git
gitee=git@gitee.com:newtorn/newtorn.git

set -ue

git checkout hexo
git add .
git commit -m "backup"

for repo in github gitee; do
    git push origin $repo
done