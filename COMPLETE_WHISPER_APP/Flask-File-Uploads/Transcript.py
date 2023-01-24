import whisper

class Transcript:
    @classmethod
    def get_transcript(self, audio):
        
        #return
        model = whisper.load_model("base")
        result = model.transcribe(audio, fp16=False)
        return result["text"]