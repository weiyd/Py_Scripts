# 基于Python的cmd脚本与exe管理器

## 命令配置
### cmd命令配置
在根目录下的tasks目录下有一个path_cmd目录，在该目录下有一个path_cmd.yaml,这是一个yaml格式的文件，打开yaml文件配置：
```yaml
#cmd: args
ping: www.baidu.com -t
``` 
冒号前面是命令，冒号后边跟的是命令的参数
### py脚本配置
在根目录下的tasks目录下有一个python目录，直接将要运行的脚本放下该目下既可。

## 命令运行
在根目录下的cmd中运行``python run.py``既可

## 日志查看
在根目录下会有一个log目录，不同命令会有不同的log对应文件。
注意：
1. cmd命令要配置好环境变量
2. python在命令行是可以运行的
3. 目前不支持yaml中相同命令不同参数
4. 确保py脚本是可执行的，目前不对py脚本进行错误检测