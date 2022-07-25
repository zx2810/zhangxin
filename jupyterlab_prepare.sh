#Begin.

#Install jupyterlab.
cd ~
conda install -c conda-forge jupyterlab
jupyter notebook --generate-config
echo 'c.NotebookApp.use_redirect_file = False' >> .jupyter/jupyter_notebook_config.py
echo "export BROWSER='/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'" >> .bashrc
source .bashrc
jupyter lab
