# 📁 C:\Users\Alexader\smart_cart_backend\voz_test.py

from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json

# Ruta del modelo descargado
model_path = "C:\\Users\\Alexader\\OneDrive\\Desktop\\vosk-model-small-es-0.42"

# Cola para capturar audio
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print("⚠️ Estado:", status)
    q.put(bytes(indata))

def main():
    print("🔄 Inicializando modelo Vosk...")
    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    print("🎙️ Hablá algo (Ctrl+C para salir)")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                resultado = json.loads(recognizer.Result())
                print("📝 Texto reconocido:", resultado.get("text", ""))
            else:
                parcial = json.loads(recognizer.PartialResult())
                print("⏳ Parcial:", parcial.get("partial", ""))

if __name__ == "__main__":
    main()
