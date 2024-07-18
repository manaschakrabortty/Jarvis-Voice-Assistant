JARVIS - VOICE-ACTIVATED VIRTUAL ASSISTANT 
Jarvis is a voice-activated virtual assistant designed to perform tasks such as web 
browsing, playing music, fetching news, and responding to user queries using OpenAI's 
GPT-3.5-turbo model. 

FEATURES 
• Voice Recognition 
• Utilizes the speech_recognition library to listen for and recognize voice commands. 
• Activates upon detecting the wake word "Jarvis." 
• Text-to-Speech 
• Converts text to speech using pyttsx3 for local conversion. 
• Uses gTTS (Google Text-to-Speech) and pygame for playback. 
• Web Browsing. 
• Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice 

commands. 
• Music Playback 
• Interfaces with a musicLibrary module to play songs via web links. 
• News Fetching 
• Fetches and reads the latest news headlines using NewsAPI. 
• OpenAI Integration 
• Handles complex queries and generates responses using OpenAI's GPT-3.5-turbo. 
• Acts as a general virtual assistant similar to Alexa or Google Assistant. 
• Activates upon detecting the wake word "Jarvis." 
• Text-to-Speech 

WORKFLOW 
1. Initialization 
2. Greets the user with "Initializing Jarvis...." 
3. Wake Word Detection 
4. Listens for the wake word "Jarvis." 
5. Acknowledges activation by saying "Ya." 
6. Command Processing. 
7. Processes commands to determine actions such as opening a website, playing 
music, fetching news, or generating a response via OpenAI. 
8. Speech Output. 
9. Provides responses using speak function with either pyttsx3 or gTTS. 
10. Greets the user with "Initializing Jarvis...." 
11. Wake Word Detection 
12. Acknowledges activation by saying "Ya." 
13. Processes commands to determine actions such as opening a website, playing 
music, fetching news, or generating a response via OpenAI.

LIBRARIES USED 
• speech_recognition 
• webbrowser 
• pyttsx3 
• musicLibrary 
• requests 
• openai 
• pygame 
• os
