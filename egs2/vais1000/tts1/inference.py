from espnet2.bin.tts_inference import Text2Speech
import soundfile as sf
import os

vocoder = 'checkpoint-20000steps.pkl'
root = '/home/user123456/work/tts/ParallelWaveGAN/egs/vais1000/voc1/exp/train_nodev_parallel_wavegan.v1'
vocoder_file = os.path.join(root,vocoder)
print(vocoder_file)

model_file="/home/user123456/work/tts/train/espnet/egs2/vais1000/tts1/exp/tts_train_raw_phn_vietnamese_espeak_ng_vi_vn_x_south/100epoch.pth"
# tts = Text2Speech.from_pretrained(model_file=model_file)
tts = Text2Speech.from_pretrained(model_file=model_file,
                                  vocoder_file=vocoder_file)
wav = tts("hôm qua em tới trường , mẹ dắt tay từng bước . hôm nay mẹ lên nương , một mình em bước tiếp")["wav"]

sf.write("out.wav", wav.numpy(), tts.fs, "PCM_16")