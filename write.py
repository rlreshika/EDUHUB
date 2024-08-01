from preTrained import *
def makeTextFile(name, content):
    file = open(f"C:/Users/rlres/OneDrive/Desktop/VideoTranscriptSummarizer-main/Transcripts/{name}.txt","w",encoding="utf-8")
    file.write(f"{name} Transcript:\n")
    file.write(content)
    file.close()