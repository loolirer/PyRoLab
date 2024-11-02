from faster_whisper import WhisperModel
from collections import deque
import speech_recognition as sr

commands = deque()
model = None
def callback(_,audio:sr.AudioData):
    global model
    data = audio.get_raw_data()
    result, info = model.transcribe(data)
    speech = list(result)[0].text
    #TODO:
    # llm_result = llama.process(speech)
    for line in llm_result.split("\n"):
        commands.append((line.split(" ")))
    

def sysCall_init():
    # create whisper model 
    global model
    model = WhisperModel("base",compute_type="int8")
    # configure recorder
    recorder = sr.Recognizer()
    recorder.energy_threshold = 1000
    recorder.dynamic_energy_threshold
    # configure microphone
    source = sr.Microphone(sample_rate=16000)
    with source:
        recorder.adjust_for_ambient_noise(source)
    # start voice detection
    recorder.listen_in_background(source, callback, phrase_time_limit=2)

def sysCall_actuation():
    if commands:
      command,ammount,duration = commands.popleft()
      #TODO:  
      # run[command](ammount,duration)
