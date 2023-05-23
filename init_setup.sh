echo [$(date)]: "START"
echo [$(date)]: "creating new python virtual environment with python=3.8"
conda create --prefix ./venv python=3.8 -y
echo [$(date)]: "activating virtual environment"
source activate ./venv
echo [$(date)]: "installing the project required libraries"
pip install -r requirements.txt
echo [$(date)]: "END"