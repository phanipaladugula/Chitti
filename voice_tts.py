import asyncio
import edge_tts

VOICE="te-IN-ShrutiNeural"

async def _speak(text,output_file):
    tts=edge_tts.Communicate(text,VOICE)
    await tts.save(output_file)

def text_to_speech(text,output_file="out.mp3"):
    asyncio.run(_speak(text,output_file))
    return output_file