# /bin/env python3.8

import IPython.display as ipd
from huggingface_hub import notebook_login
from datasets.builder import ReadInstruction
from datasets import load_dataset


notebook_login()

# ri = ReadInstruction('train', to=10, unit='%') # only split 10% of training data
dataset = load_dataset("mozilla-foundation/common_voice_13_0", "en", split="train", streaming=True)

print(next(iter(dataset)))


sample = next(iter(dataset))
audio = sample["audio"]

print(sample["sentence"])
ipd.Audio(data=audio["array"], autoplay=True, rate=audio["sampling_rate"])