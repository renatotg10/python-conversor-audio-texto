# 🎧 Conversor de Áudio para Texto - Whisper + Tkinter

Este é um aplicativo simples com interface gráfica (GUI) feito em Python usando [Tkinter](https://docs.python.org/3/library/tkinter.html) que utiliza o modelo [Whisper](https://github.com/openai/whisper) da OpenAI para transcrever arquivos de áudio para texto em português.

## 📌 Funcionalidades

* Seleção de arquivo de áudio (.mp3, .wav, .m4a, .flac)
* Escolha entre diferentes modelos Whisper (tiny, base, small, medium, large)
* Transcrição com marcação de tempo (timestamp)
* Salvamento automático da transcrição em um arquivo `.txt`
* Interface gráfica simples e intuitiva

---

## 🛠️ Requisitos

Antes de executar o aplicativo, certifique-se de ter:

* Python 3.8 ou superior
* O arquivo `ffmpeg-7.1.1-essentials.zip` extraído e configurado corretamente no PATH do sistema
* Os seguintes pacotes Python:

```bash
pip install openai-whisper tkinter
```

> 💡 O `tkinter` geralmente já vem instalado com o Python em sistemas Windows e Linux.

---

## Clone o repositório ou baixe o arquivo `.py`:

   ```bash
   git clone https://github.com/renatotg10/python-conversor-audio-texto.git
   cd converte-voz-texto
   ```

## ⚙️ Instalando o `ffmpeg`

O Whisper requer que o `ffmpeg` esteja instalado e configurado corretamente no seu sistema. Você já deve ter o arquivo `ffmpeg-7.1.1-essentials.zip` na raiz do projeto. Siga as instruções abaixo para configurar o `ffmpeg` no PATH do sistema.

### **Windows**

1. Extraia o conteúdo do arquivo `ffmpeg-7.1.1-essentials.zip`:

   * Clique com o botão direito no arquivo `ffmpeg-7.1.1-essentials.zip` e escolha **Extrair Aqui** ou use um programa como [7-Zip](https://www.7-zip.org/) para extrair o conteúdo para a pasta `ffmpeg`.

2. Adicione o `ffmpeg` ao PATH do sistema:

   * Abra o **Prompt de Comando** como administrador.
   
   * Adicione o caminho ao PATH:
   
    Exemplo:

     ```bash
     setx PATH "%PATH%;C:\meus-projetos\converte-voz-texto\ffmpeg\bin"
     ```

3. Verifique se o `ffmpeg` foi instalado corretamente:

   * Saia do **Prompt de Comando** e abra um novo **Prompt de Comando** (para garantir que as alterações no PATH foram aplicadas).
   * Digite:

     ```bash
     ffmpeg -version
     ```
   * Você deverá ver a versão do `ffmpeg` instalada.

---

### **Linux (Ubuntu/Debian)**

1. Extraia o conteúdo do arquivo `ffmpeg-7.1.1-essentials.zip`:

   * Navegue até a pasta onde o arquivo `ffmpeg-7.1.1-essentials.zip` está localizado.
   * Extraia o conteúdo:

     ```bash
     unzip ffmpeg-7.1.1-essentials.zip
     ```

2. Adicione o `ffmpeg` ao PATH do sistema:

   * Copie o caminho para a pasta `bin` dentro da pasta `ffmpeg`. Por exemplo, se a pasta `ffmpeg` estiver na raiz do seu projeto, o caminho será algo como:
     
     Exemplo:

     ```bash
     /meus-projetos/converte-voz-texto/ffmpeg/bin
     ```

   * Abra o terminal e edite o arquivo `.bashrc` (ou `.zshrc` para Zsh):

     ```bash
     nano ~/.bashrc
     ```
   * Adicione a seguinte linha no final do arquivo:

     Exemplo:

     ```bash
     export PATH=$PATH:/meus-projetos/converte-voz-texto/ffmpeg/bin
     ```

   * Salve e feche o arquivo (`Ctrl + X`, depois pressione `Y` para confirmar e `Enter`).

3. Atualize o PATH:

   ```bash
   source ~/.bashrc
   ```

4. Verifique se o `ffmpeg` foi instalado corretamente:

   * Digite no terminal:

     ```bash
     ffmpeg -version
     ```
   * Você deverá ver a versão do `ffmpeg` instalada.

---

## 🚀 Como usar

1. Execute o script:

   ```bash
   python transcritor_gui.py
   ```

2. Na interface:

   * Clique em **Selecionar Arquivo** e escolha um arquivo de áudio suportado.
   * Escolha um modelo Whisper (quanto maior o modelo, melhor a qualidade, mas mais lento).
   * Clique em **Transcrever Áudio**.
   * O texto transcrito aparecerá na tela e será salvo no mesmo diretório do áudio original, com o sufixo `_transcricao.txt`.

---

## 🧠 Modelos suportados

| Modelo   | Tamanho | Velocidade   | Precisão    |
| -------- | ------- | ------------ | ----------- |
| `tiny`   | 39 MB   | Muito rápida | Baixa       |
| `base`   | 74 MB   | Rápida       | Média-baixa |
| `small`  | 244 MB  | Média        | Boa         |
| `medium` | 769 MB  | Lenta        | Muito boa   |
| `large`  | 1550 MB | Muito lenta  | Excelente   |

> Recomendado: `small` para bom equilíbrio entre desempenho e qualidade.

---

## 📝 Exemplo de saída

```
[00:00:00 - 00:00:04] Olá, este é um teste de transcrição com o modelo Whisper.
[00:00:04 - 00:00:07] O objetivo é converter fala em texto automaticamente.
```

---

## ❗ Observações

* O primeiro uso de um modelo irá fazer download do mesmo (pode demorar alguns minutos).
* O desempenho e a precisão dependem do modelo escolhido e da qualidade do áudio.

---

## 📄 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais informações.
