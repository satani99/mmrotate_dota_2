# mmrotate_dota_2
# Finetune RTMDet on DOTA 2.0 dataset using mmrotate. 

conda create -n dota python==3.8 -y
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
pip install -U openmim
git clone https://github.com/satani99/mmrotate_dota_2.git
cd mmrotate_dota_2
pip install -v -e .
wget https://github.com/ultralytics/yolov5/releases/download/v1.0/DOTAv2.zip 
unzip DOTAv2.zip

python tools/data/dota/split/img_split.py --base-json \
  tools/data/dota/split/split_configs/ss_train.json

python tools/data/dota/split/img_split.py --base-json \
  tools/data/dota/split/split_configs/ss_val.json
  
python tools/data/dota/split/img_split.py --base-json \
  tools/data/dota/split/split_configs/ss_test.json
  
python filter_labels.py

Run dota_finetuning.ipynb in demo folder