from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/<vid>')
def ts(vid):
  transcriptArr = YouTubeTranscriptApi.get_transcript(vid)
  transcript = ""
  for i in transcriptArr:
    transcript += i['text'] + " "

  return {
    "transcript": transcript
  }

if __name__ == "__main__":
  app.run(port=3000)
