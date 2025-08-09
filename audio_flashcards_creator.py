import os
import requests

# This function reads the transcript

def read_transcript(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading text file: {e}")
        return None

#This function starts the generation of the ANKI Flashcards

def create_anki_cards(text_content, output_file):
    print("  > Sending transcript to local AI model (Ollama) for flashcard generation...")

    # Improvement From My PDF-Flashcards Generator
    # EDITABLE: The AI's Prompt for generating flashcards:
    
    prompt = f"""

    You are an expert Anki flashcard creator. Your task is to read the provided text and create EXACTLY 20 flashcards.

        OUTPUT RULES — You must follow these exactly:
        1. The output must be EXACTLY 20 lines.
        2. Each line must be in the format:
            front ; back
            - One space before and after the semicolon.
        3. DO NOT number, bullet, label, or prefix the lines in any way.
        4. DO NOT add any extra text before or after the 20 lines.
        5. Each "front" must be ONE of these styles:
             - **Fill-in-the-Blank:** A sentence with a missing key term represented by four underscores `____`. (Ex. The capital city of Japan is ____ ; Tokyo)
             - **Direct Question:** A short, clear question about a key concept, fact, or process. (What is the chemical symbol for gold? ; Au)
             - **Term/Definition:** A single important term. (Mitochondria ; Organelles that produce energy for the cell through respiration)
        6. Each "back" must:
             - For Fill-in-the-Blank: ONLY the missing term.
             - For Question: ONLY the precise, concise answer.
             - For Term/Definition: ONLY the definition of that term.
        7. Each flashcard must be unique, non-redundant, and based ONLY on the provided text. Try to cover a variety of important concepts from the text with a variety of difficulties.
        8. DO NOT include hints, explanations, examples, or commentary — ONLY the flashcards in the exact format.

        Now, create exactly 20 flashcards based ONLY on this text:
        
    Here is the transcript:
    {text_content}
    """
    try:

        # Derived From My PDF-Flashcards Generator
        # EDITABLE VARIABLE: AI Model Name (Ollama, Model Name: mistral, is currently in use. You must have this model)
        # Change model name if you have a different one installed.
        
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={'model': 'mistral', 'prompt': prompt, 'stream': False},
            timeout=900

            # EDITABLE VARIABLE: Request Timeout (maximum number of seconds the script will wait for the AI to respond)
            
        )
        response.raise_for_status()
        full_response = response.json().get('response', '')
        if full_response:
            lines = [line.strip() for line in full_response.split("\n") if line.strip()]

            # EDITABLE VARIABLE: Number of Flashcards (To get # flashcards instead of 20, change 'lines[:20]' to 'lines[:#])
            
            lines_to_keep = lines[:20]
            output_file.write("\n".join(lines_to_keep) + "\n\n")
            print(f"  > Successfully processed and added {len(lines_to_keep)} flashcards.")
        else:
            print("  > Warning: AI model returned an empty response.")
    except Exception as e:
        print(f"  > An error occurred: {e}")

        # Runs the main portion of the code (accesses SOURCE_TRANSCRIPT folder, reading transcripts, and creating flashcards)

if __name__ == "__main__":
    ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    source_folder_name = "SOURCE_TRANSCRIPTS"
    source_folder = os.path.join(ROOT_DIRECTORY, source_folder_name)

    try:
        transcript_files = [f for f in os.listdir(source2_folder) if f.lower().endswith('.txt')]
    except FileNotFoundError:
        print(f"ERROR: The '{source_folder_name}' folder was not found.")
        exit()

        # Error: No Video/Audio found
        
    if not transcript_files:
        print(f"No transcript files found in the '{source_folder_name}' folder.")
    else:
        print(f"Found {len(transcript_files)} transcript(s) to process: {', '.join(transcript_files)}")
        output_filename = "audio_flashcards.txt"
        with open(output_filename, "w", encoding='utf-8') as outfile:
            for txt_file in transcript_files:
                full_path = os.path.join(source_folder, txt_file)
                print(f"\n--- Processing: {txt_file} ---")
                text_content = read_transcript(full_path)
                if text_content:
                    create_anki_cards(text_content, outfile)
        print(f"\n--- ALL DONE! ---")
        print(f"All flashcards have been saved to '{output_filename}'.")

