sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo echo '# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse' > /etc/apt/sources.list /etc/apt/sources.list
sudo apt-get update && sudo apt-get upgrade
sudp apt-get install git cmake g++ libhdf5-dev libpng-dev pip 
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r openmc_requirements.txt
git clone https://gitclone.com/github.com/openmc-dev/openmc.git
cd openmc
pip install . && cmake .
pip install jupyterlab
cd ~
#mkdir .jupyter && echo > .jupyter/jupyter_notebook_config.py
#echo 'c.NotebookApp.use_redirect_file = False' >> .jupyter/jupyter_notebook_config.py
#echo "export BROWSER='/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'" >> .bashrc
#sorce .bashrc
