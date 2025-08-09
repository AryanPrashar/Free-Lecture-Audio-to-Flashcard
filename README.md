# Lecture Audio to Flashcard Generator from PDF Files

This zip file will generate Flashcards for **FREE** with no additional costs or limitations:

The process has two main parts:
**Part 1: The One-Time Setup:** Installing all the necessary free software.
**Part 2: Your Reusable Workflow:** The simple steps you'll follow each time you want to create new flashcards.


# Part 1: The One-Time Setup
You only need to do these steps **ONCE**

## Install Anki:
__Anki is the flashcard application where you'll study your generated cards.__

1. **Download Anki:** Go to the official Anki website: https://apps.ankiweb.net/
2. **Install Anki:** Download and install the correct version for your operating system (Windows, Mac, or Linux). Follow the installation prompts.

## Set Up the AI Flashcard Generator

__Now use my free, open-source GitHub project which uses AI to automatically create flashcards from your PDF files__

1. **Install Python:** If you don't have Python installed, download and install it from https://www.python.org/downloads/. During installation, make sure to check the box that says "Add Python to PATH."
2. **Click the green "Code" button** above and select "Download ZIP."
3. **Extract** the downloaded ZIP file to a location you'll remember, like your Desktop or Documents folder.
4. **Place** this unzipped folder somewhere convenient, like your Desktop.

## Install and Set Up the Local AI (Ollama)

__This is the "brain" that will create your flashcards. It runs 100% on your own computer, so it's free and private.__

1. **Go** to the Ollama website: https://ollama.com/
2. **Download** and install Ollama for your operating system.
3. **After it's installed,** Ollama will run in the background. Now, you need to download a specific AI model for it to use.
4. **Open** your computer's command line tool:
            **Windows:** Press the Windows Key, type cmd, and press Enter.
            **Mac:** Press Command + Spacebar, type Terminal, and press Enter.
5. **In the black window** that appears, type the following command and press Enter. This downloads the "Mistral" AI model (it's a few gigabytes and may take a few minutes).

```shell
ollama run mistral
```

## Install the Required Python Libraries

1. Open a new command line window (cmd or Terminal).
2. Install the PDF reader library by running this command:
```shell
pip install PyMuPDF
```
3. Install the requests library by running this command:
```shell
pip install requests
```
Setup is complete! You are now ready to start creating flashcards.

#Part 2: Your Reusable Flashcard Workflow

## Make Sure the AI is Running

__The Ollama application must be running in the background. Check for its icon in your system tray (bottom-right on Windows) or menu bar (top-right on Mac). If it's not running, just launch the Ollama application.__

## Make Sure the AI is Running

1. Open the project folder you downloaded:
```shell
Free-Lecture-Audio-to-Flashcard
```
4. **Inside**, find the folder named **SOURCE_TRANSCRIPT**

#Stage 1: Transcribe Audio to Text
1. **Place** your lecture audio file (e.g., lecture1.mp3, class_recording.m4a) into your main project folder: Free_Anki_FlashCard_Generator-shared-use--main.
2. **Open** your command line (cmd or Terminal).
3. **Navigate** into the project folder using the cd command (you can drag and drop the folder icon after typing cd).
4. **Run** the Whisper command. Replace lecture1.mp3 with the exact name of your audio file.
```shell
whisper "lecture1.mp3"
```
5. **Wait.** Whisper will now process the audio. This can take some time. When it's done, you will see a new file in your folder: lecture1.mp3.txt. This is your full transcript.

#Stage 2: Generate Flashcards from the Transcript
1. **Move** the transcript file from the main project folder into the SOURCE_TRANSCRIPTS folder.
2. **Make** sure your Ollama application is running.
3. In the same command line window, **run** your new Python script:
```shell
whisper "lecture1.mp3"
```
4. The script will find your transcript, **send** it to the local AI, and create a new file named audio_flashcards.txt.
5. **Import** the audio_flashcards.txt file into Anki, making sure to set the separator to Semicolon.

#DONE
