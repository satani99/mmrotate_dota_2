# mmrotate_dota_2
# Finetune RTMDet on DOTA 2.0 dataset using mmrotate. 

Create a conda environment named dota.

```bash
conda create -n dota python==3.8 -y
conda activate dota
```

Then install pytorch, torchvision, mmdet, mmcv, and mmrotate libraries.

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
pip install -U openmim
mim install mmdet
git clone https://github.com/satani99/mmrotate_dota_2.git
cd mmrotate_dota_2
pip install -v -e .
```

Download dataset.

```bash
wget https://github.com/ultralytics/yolov5/releases/download/v1.0/DOTAv2.zip 
unzip DOTAv2.zip
```

Below commands crops the images into 1024x1024 pixels and create the annotation files according to the crops.

```bash
python tools/data/dota/split/img_split.py --base-json \
  tools/data/dota/split/split_configs/ss_train.json
python tools/data/dota/split/img_split.py --base-json \
  tools/data/dota/split/split_configs/ss_val.json
python tools/data/dota/split/img_split.py --base-json \
  tools/data/dota/split/split_configs/ss_test.json
```

Since we want to fine-tune the model on only five classes ```filter_labels.py``` removes the classes we don't need from the annotation files.

```bash
cd demo
python filter_labels.py
```

After completing the above steps run ```dota_finetuning.ipynb``` in the demo folder.

# Result

For fine-tuning for only three epochs we can achieve 28.5% mAP and training for more epochs would yield better results. It took around 1.5 hours for three epochs to complete on RTX 3060.

![alt text](https://github.com/satani99/mmrotate_dota_2/blob/main/demo/result.png?raw=true)

