sudo apt update
sudo apt install python-pip
pip install -U pip setuptools wheel
pip install -r requirements.txt
python3 -m spacy download en_core_web_sm
