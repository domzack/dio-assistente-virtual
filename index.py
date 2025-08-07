# Assistente Virtual - Estrutura Inicial

missing = []

try:
    import speech_recognition as sr
except ImportError:
    missing.append("SpeechRecognition")

try:
    import pyttsx3
except ImportError:
    missing.append("pyttsx3")

try:
    import pyaudio
except ImportError:
    missing.append("pyaudio")

import webbrowser

if missing:
    print(
        f"Dependências não encontradas: {', '.join(missing)}.\n"
        f"Instale com: pip install {' '.join(missing)}"
    )
    exit(1)


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except Exception as e:
        print("Não foi possível reconhecer a fala.")
        return ""


def executar_comando(comando):
    comando = comando.lower()
    if "wikipedia" in comando:
        text_to_speech("Abrindo pesquisa no Wikipedia.")
        webbrowser.open("https://pt.wikipedia.org")
    elif "youtube" in comando:
        text_to_speech("Abrindo o Youtube.")
        webbrowser.open("https://www.youtube.com")
    elif "farmácia" in comando:
        text_to_speech("Buscando farmácia mais próxima no Google Maps.")
        webbrowser.open("https://www.google.com/maps/search/farmácia+próxima")
    else:
        text_to_speech("Comando não reconhecido.")


if __name__ == "__main__":
    comandos_disponiveis = (
        "Eu entendo os seguintes comandos: "
        "abrir Wikipedia, abrir Youtube, mostrar farmácia mais próxima, "
        "ou você pode dizer sair, encerrar ou parar para finalizar."
    )
    text_to_speech("Olá! Eu sou seu assistente virtual. Como posso ajudar?")
    text_to_speech(comandos_disponiveis)
    try:
        while True:
            comando = speech_to_text()
            if comando:
                if any(
                    palavra in comando.lower()
                    for palavra in ["sair", "encerrar", "parar"]
                ):
                    text_to_speech("Encerrando o assistente virtual. Até logo!")
                    break
                executar_comando(comando)
    except KeyboardInterrupt:
        print("\nAssistente encerrado pelo usuário.")
        text_to_speech("Assistente encerrado pelo usuário. Até logo!")
