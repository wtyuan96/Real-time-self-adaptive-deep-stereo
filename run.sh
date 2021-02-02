LIST="scared.csv" #the one described at step (1)
OUTPUT="Output/"
WEIGHTS="Pretrained/MADNet/kitti/weights.ckpt"
MODELNAME="MADNet"
BLOCKCONFIG="block_config/MadNet_full.json"

export CUDA_VISIBLE_DEVICES=1

python3 Stereo_Online_Adaptation.py \
    -l ${LIST} \
    -o ${OUTPUT} \
    --weights ${WEIGHTS} \
    --modelName MADNet \
    --blockConfig ${BLOCKCONFIG} \
    --mode FULL \
    --sampleMode PROBABILITY \
    --logDispStep 1