import assemblyai as aai
import constants

#aai.settings.api_key = "dd25316e983541d0857dcdbc0677f202"
aai.settings.api_key = constants.API_KEY_ASSEMBLY_AI

transcriber = aai.Transcriber()

audio_url = (
    "https://storage.googleapis.com/aai-web-samples/5_common_sports_injuries.mp3"
)

config = aai.TranscriptionConfig(speaker_labels=True)

transcript = transcriber.transcribe(audio_url, config)

print(transcript.text)

for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")
