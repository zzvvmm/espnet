# from espnet2.bin.tts_inference import Text2Speech
from espnet_onnx import Text2Speech

import soundfile as sf
import os
from espnet_onnx.export import TTSModelExport
import espnet_onnx

vocoder = 'checkpoint-110000steps.pkl'
root = '/home/user123456/work/tts/ParallelWaveGAN/egs/vais1000/voc1/exp/train_nodev_parallel_wavegan.v1'
vocoder_file = os.path.join(root,vocoder)
print(vocoder_file)

text = "hôm qua em tới trường mẹ dắt tay từng bước hôm nay mẹ lên nương một mình em bước tiếp"
model_file="/home/user123456/work/tts/train/espnet/egs2/vais1000/tts1/result/exp-0307/exp/tts_train_raw_phn_vietnamese_espeak_ng_vi_vn_x_south/100epoch.pth"
# model_file="/home/user123456/work/tts/train/espnet/egs2/vais1000/tts1/exp/tts_train_raw_phn_vietnamese_espeak_ng_vi_vn_x_south/66epoch.pth"

# tts = Text2Speech.from_pretrained(model_file=model_file)
# tts = Text2Speech.from_pretrained(model_file=model_file,
#                                   vocoder_file=vocoder_file)
# wav = tts(text)["wav"]

m = TTSModelExport()
tag_name = 'kan-bayashi/ljspeech_vits'
m.export_from_pretrained(tag_name, quantize=True)
# m.export(tts, tag_name, quantize=True)
text2speech = Text2Speech(tag_name, use_quantized=False)

output_dict = text2speech(text) # inference with onnx model.
wav = output_dict['wav']
sf.write("out.wav", wav, 22050, "PCM_16")