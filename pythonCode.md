## 使用镜像源：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt5 
pip --no-cache-dir install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt5 不用本地缓存安装

## 通过requirement.txt安装
pip install   -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
pip freeze > requirements.txt

## 下载离线安装包到指定文件夹：
pip download PyQt5 -d C:\Users\sutut\Desktop\【非密】 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip download QScintilla -d C:\Users\sutut\Desktop\eric -i https://pypi.tuna.tsinghua.edu.cn/simple

## 安装离线whl包：cmd到whl包目录下：
pip install wheel PyQt5 

## 更新pip：
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip

## 更新所有库：
pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple pip
pip install --upgrade pip

## 设置全局镜像源
pip config --global set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config --global set install.trusted-host pypi.tuna.tsinghua.edu.cn


## pip卸载所有安装包
1. 导出所有包的名称pip freeze > requirements.txt
2. unistall 所有包pip uninstall -r requirements.txt -y 如果不加最后的-y就需要一个一个包输入y确认卸载