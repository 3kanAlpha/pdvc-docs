import json, os

from faster_whisper import WhisperModel
from tqdm import tqdm

MODEL_SIZE = "distil-large-v3"

def generate_caption_from_audio(audio_path: str):
  """指定したパスの音声ファイルから、文字起こしデータを生成する。"""
  print("Loading Whisper model...")
  model = WhisperModel(MODEL_SIZE, device="cuda", compute_type="float16")
  segments, info = model.transcribe(audio_path, language="en")
  
  total_duration = round(info.duration, 2)
  current_time = 0.0
  
  print("Running Whisper...")
  
  transcriptions = []
  with tqdm(total=total_duration, unit=" audio sec") as pbar:
    for segment in segments:
      raw_text = segment.text
      t = raw_text.strip()
      
      item: dict = {
        "start_time": segment.start,
        "end_time": segment.end,
        "text": t,
      }
      transcriptions.append(item)
      
      new_ts = round(segment.end - current_time, 2)
      pbar.update(new_ts)
      current_time = segment.end
  
  print("Exporting result...")
  basename = os.path.basename(audio_path)
  root, ext = os.path.splitext(basename)
  parent_dir = os.path.dirname(audio_path)
  output_path = os.path.join(parent_dir, f"{root}_caption.json")
  with open(output_path, "w") as f:
    json.dump(transcriptions, f, indent=2)

def main():
  audio_path = r"H:\esslab_works\data\vct\clip3\audio_clip3.m4a"
  generate_caption_from_audio(audio_path)

if __name__ == "__main__":
  main()