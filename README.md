# Rules

## 简介

自动合并**去广告、代理规则和网易云解锁规则**，适用于Shadowrocket，网易云解锁请结合[nondanee/UnblockNeteaseMusic](https://github.com/nondanee/UnblockNeteaseMusic)食用。

去广告、代理规则来自：[lhie1/Rules](https://github.com/lhie1/Rules)、[h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules)。

网易云解锁规则来自：[DesperadoJ/Rules-for-UnblockNeteaseMusic](https://github.com/DesperadoJ/Rules-for-UnblockNeteaseMusic)。

## 食用方法

### 1. 首先在shadowrocket上添加好网易云的解锁节点

首先根据[nondanee/UnblockNeteaseMusic](https://github.com/nondanee/UnblockNeteaseMusic)里的教程设置好解锁节点，然后在Shadowrocket里添加。（仔细阅读原项目issue: [iOS配置经验分享](https://github.com/nondanee/UnblockNeteaseMusic/issues/368)）

![2021-03-10T13:10:16](https://cdn.jsdelivr.net/gh/xiangsanliu/images@master/uPic/2021-03-10T13:10:16.jpeg)

节点名称需要和[UnblockNeteaseMusic.conf](UnblockNeteaseMusic.conf)里的名称相同。(Thank [Rules-for-UnblockNeteaseMusic](https://github.com/DesperadoJ/Rules-for-UnblockNeteaseMusic))

### 2. 添加规则链接到 Shadowrocket

| 规则           | 链接                                                                      | 备注       |
| -------------- | ------------------------------------------------------------------------- | ---------- |
| merge-h2y.conf | https://raw.githubusercontent.com/xiangsanliu/Rules/main/merge-h2y.conf   | github raw |
| merge-h2y.conf | https://cdn.jsdelivr.net/gh/xiangsanliu/Rules/merge-h2y.conf              | cdn 加速   |
| merge-lhie1    | https://raw.githubusercontent.com/xiangsanliu/Rules/main/merge-lhie1.conf | github raw |
| merge-lhie1    | https://cdn.jsdelivr.net/gh/xiangsanliu/Rules/merge-lhie1.conf            | cdn 加速   |

## 自定义开发

### 1. fork本项目

### 2. 设置自动更新

#### 2.1 设置GITHUB_TOKEN
到个人GitHub Setting > Developer settings > Personal access tokens > Generate new token,设置名字为GITHUB_TOKEN, 然后勾选repo, admin:repo_hook, workflow，最后点击Generate token即可。 (Thank [Github Actions教程](https://cloud.tencent.com/developer/article/1643440))

#### 2.2 运行一次workflow

点击仓库下面的`Actions` > `Auto update` > `Run workflow` > `Run workflow`

### 3. Do something.


> [merge-lhie1.conf](merge-lhie1.conf)合并自[lhie1/Rules](https://github.com/lhie1/Rules)。
> 
> [merge-h2y.conf](merge-h2y.conf)合并自[h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules)。

> 今天刚刚得知[h2y/Shadowrocket-ADBlock-Rules](https://github.com/h2y/Shadowrocket-ADBlock-Rules)项目已停止维护，故本项目中的[merge-h2y.conf](merge-h2y.conf)也只能停更了。 
>   --- 2021-04-13

> 纯python小白，写的脚本很简单，欢迎批评指正。

