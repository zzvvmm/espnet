
import gradio as gr
import time
import torch
import scipy.io.wavfile
from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none
from vietnamese_cleaner import vietnamese_cleaners

tagen = '/home/user123456/work/tts/train/espnet/egs2/vais1000/tts1/exp/tts_train_raw_phn_vietnamese_espeak_ng_vi_vn_x_south/90epoch.pth' 
vocoder_tagen = "/home/user123456/work/tts/ParallelWaveGAN/egs/vais1000/voc1/exp/train_nodev_parallel_wavegan.v1/checkpoint-150000steps.pkl" 

text2speechen = Text2Speech.from_pretrained(
    model_file=str_or_none(tagen),
    vocoder_file=str_or_none(vocoder_tagen),
    device="cpu",
    # Only for Tacotron 2 & Transformer
    threshold=0.5,
    # Only for Tacotron 2
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=False,
    backward_window=1,
    forward_window=3,
    # Only for FastSpeech & FastSpeech2 & VITS
    speed_control_alpha=1.0,
    # Only for VITS
    noise_scale=0.333,
    noise_scale_dur=0.333,
)

def inference(text):
    text = vietnamese_cleaners.vietnamese_cleaner(text)
    print(f"cleaned_text: {text}")
    with torch.no_grad():
        wav = text2speechen(text)["wav"]
        scipy.io.wavfile.write("out.wav",text2speechen.fs , wav.view(-1).cpu().numpy())

    return  "out.wav"
title = "Hainong-TTS"

examples=[['Hôm qua em tới trường mẹ dắt tay từng bước Hôm nay mẹ lên nương một mình em bước tiếp']]

gr.Interface(
    inference, 
    [gr.inputs.Textbox(label="Câu văn",lines=10)], 
    gr.outputs.Audio(type="filepath", label="Kết quả"),
    title=title,
    enable_queue=True,
    examples=examples
).launch(debug=True)

