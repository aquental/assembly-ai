# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai
import constants

#aai.settings.api_key = "dd25316e983541d0857dcdbc0677f202"
aai.settings.api_key = constants.API_KEY_ASSEMBLY_AI
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)
