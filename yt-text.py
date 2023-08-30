import spacy
from youtube_transcript_api import YouTubeTranscriptApi

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

def format_transcript(transcript_data):
    formatted_script = ""
    for entry in transcript_data:
        formatted_script += f"{entry['text']} "
    return formatted_script

def extract_main_content(text):
    doc = nlp(text)
    
    # Calculate sentence lengths and store them in a list
    sentence_lengths = [len(sent) for sent in doc.sents]
    
    # Determine a threshold for sentence lengths to consider as main content
    avg_length = sum(sentence_lengths) / len(sentence_lengths)
    threshold = avg_length * 0.8
    
    # Select sentences with lengths above the threshold as main content
    main_content_sentences = [sent for sent, length in zip(doc.sents, sentence_lengths) if length > threshold]
    main_content = " ".join(str(sentence) for sentence in main_content_sentences)
    
    return main_content

video_id = "5F32KdQ0yvU&list=PLePbzYpjlB24ELainHpfGFV9qagiN3x1Y"
transcript = YouTubeTranscriptApi.get_transcript(video_id)

formatted_script = format_transcript(transcript)
main_content = extract_main_content(formatted_script)

# Write the main content to a text file
with open("yt_main_content.txt", "w", encoding="utf-8") as file:
    file.write(main_content)

print("Main content has been extracted and written to yt_main_content.txt")
