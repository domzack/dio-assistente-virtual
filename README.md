# Assistente Virtual - DIO

Este projeto é um sistema de assistência virtual desenvolvido em Python, utilizando técnicas de Processamento de Linguagem Natural (PLN) e bibliotecas para reconhecimento de fala e síntese de voz.

## Funcionalidades

- **Text to Speech**: Converte texto em áudio usando a biblioteca `pyttsx3`.
- **Speech to Text**: Converte fala do usuário em texto usando `speech_recognition` e `pyaudio`.
- **Comandos automatizados por voz**:
  - Abrir pesquisa no Wikipedia
  - Abrir o Youtube
  - Apresentar a localização da farmácia mais próxima (Google Maps)
  - Encerrar o assistente virtual com comandos de voz: "sair", "encerrar" ou "parar"

## Como usar

1. Instale as dependências:
   ```
   pip install SpeechRecognition pyttsx3 pyaudio
   ```
   > Obs: Em alguns sistemas, pode ser necessário instalar o `pyaudio` via gerenciador de pacotes do sistema.

2. Execute o arquivo principal:
   ```
   python index.py
   ```

3. O assistente irá informar os comandos que entende e aguardar sua fala.

## Comandos reconhecidos

- **abrir Wikipedia**: Abre o site do Wikipedia.
- **abrir Youtube**: Abre o site do Youtube.
- **mostrar farmácia mais próxima**: Abre o Google Maps buscando farmácias próximas.
- **sair / encerrar / parar**: Encerra o assistente virtual.

## Requisitos

- Python 3.x
- Microfone configurado no sistema

## Créditos

Desenvolvido para o desafio DIO - Assistente Virtual com PLN.
