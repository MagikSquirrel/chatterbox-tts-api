import torch
from chatterbox.tts_turbo import ChatterboxTurboTTS

print("Torch:", torch.__version__)
print("GPU available:", torch.cuda.is_available())
model = ChatterboxTurboTTS.from_pretrained(device="cuda")
print("Model loaded on:", next(model.parameters()).device)