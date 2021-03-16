# Rules

## 简介

自动合并[lhie1/Rules](https://github.com/lhie1/Rules)的代理规则和解锁网易云的规则。适用于Shadowrocket，请结合[nondanee/UnblockNeteaseMusic](https://github.com/nondanee/UnblockNeteaseMusic)食用。

## 食用方法

### 1. 首先在shadowrocket上添加好网易云的解锁节点

首先根据[nondanee/UnblockNeteaseMusic](https://github.com/nondanee/UnblockNeteaseMusic)里的教程设置好解锁节点，然后在Shadowrocket里添加。（仔细阅读原项目issue [iOS配置经验分享](https://github.com/nondanee/UnblockNeteaseMusic/issues/368)）

![2021-03-10T13:10:16](https://cdn.jsdelivr.net/gh/xiangsanliu/images@master/uPic/2021-03-10T13:10:16.jpeg)

节点名称需要和[UnblockNeteaseMusic.conf](UnblockNeteaseMusic.conf)里的名称相同。(Thank [Rules-for-UnblockNeteaseMusic](https://github.com/DesperadoJ/Rules-for-UnblockNeteaseMusic))

### 2. fork本仓库

### 3. 设置自动更新

#### 3.1 设置GITHUB_TOKEN
到个人GitHub Setting > Developer settings > Personal access tokens > Generate new token,设置名字为GITHUB_TOKEN, 然后勾选repo, admin:repo_hook, workflow，最后点击Generate token即可。 (Thank [Github Actions教程](https://cloud.tencent.com/developer/article/1643440))

#### 3.2 运行一次workflow

点击仓库下面的`Actions` > `Auto update` > `Run workflow` > `Run workflow`

### 4. 使用

把[merge.conf](merge.conf)的raw地址填到shadowrock中即可。

> 纯python小白，写的脚本很简单，欢迎批评指正。

