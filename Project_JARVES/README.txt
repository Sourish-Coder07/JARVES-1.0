************************************************************
👨‍💻 Project by: SOURISH  
🎓 Electronics & Telecommunication Engineering Student  
************************************************************

🚀 JARVES - Your Personal AI Desktop Assistant

JARVES is a Python-powered personal voice assistant that can perform various tasks like playing music, managing to-dos, reading Wikipedia, sending emails, and more — all controlled by your voice.

------------------------------------------------------------

✅ Features

- 🎤 Voice-controlled assistant  
- 🗣 Text-to-speech (TTS)  
- 📅 Tells time & date  
- 🎶 Plays music from YouTube  
- 📚 Wikipedia summaries  
- 📝 Task manager (add, speak, show tasks)  
- 🌐 Google search  
- ⚙️ Open installed apps  
- 📧 Send emails (via Gmail)  
- 💬 Send WhatsApp messages (via web)  
- 📁 Fully customizable via user_config.py  
- ❌ No OpenAI / Internet APIs required for chat or image generation  

------------------------------------------------------------

🛠 Setup Instructions

1. Unzip the `.rar` file  
   Open the extracted folder in VS Code or your preferred IDE.

2. Create a Virtual Environment  
   Command:  
   `python -m venv env_jarvis`

3. Activate the Environment  
   Command:  
   `.\env_jarvis\Scripts\activate`

4. Install All Dependencies  
   Command:  
   `pip install -r requirements.txt`

5. Configure Your Details in `user_config.py`  
   Open `user_config.py` and update these values:

   - `user_name` → Your name (e.g., "Sourish")  
   - `email_sender` → Your Gmail address  
   - `email_receiver` → Recipient's Gmail address  
   - `email_password` → Gmail **App Password**  
   - `whatsapp_number` → WhatsApp number (e.g., "+91XXXXXXXXXX")  
   - `music_links` → Add your favorite YouTube links  
   - `voice_id` → Choose `0` for male or `1` for female voice  
   - `speech_rate` → Adjust voice speed (e.g., 170)

6. Run the Assistant  
   Command:  
   `python main.py`

------------------------------------------------------------

🗣 How to Talk to JARVES – Example Commands

Say these aloud after starting the program:

- “Hello” → Greets you  
- “Say time” → Tells current time  
- “Say date” → Tells today’s date  
- “New task finish electronics project” → Adds a task  
- “Speak task” → Reads your tasks  
- “Show work” → Shows task notification  
- “Play music” → Opens random YouTube music  
- “Wikipedia Nikola Tesla” → Gives short summary  
- “Open notepad” → Opens Notepad  
- “Search Google Python tutorials” → Searches on browser  
- “Send WhatsApp” → Sends a message  
- “Send email” → Sends email via Gmail  
- “Clear chat” → Clears memory (placeholder)

⚠️ Speak clearly in English (Indian accent supported)

------------------------------------------------------------

🧩 File Structure

main.py              → Main assistant logic  
speech.py            → Text-to-speech control  
user_config.py       → Personal settings (must configure this)  
command_input.py     → Handles voice input  
todo.txt             → Your task list  
requirements.txt     → Required packages  
README.txt           → Project overview and usage instructions

------------------------------------------------------------

📝 Customize Your Assistant

- Change voice type and rate in `user_config.py`  
- Add/remove music links  
- Rename “JARVES” to your custom assistant name  
- Add more commands in `main.py`

------------------------------------------------------------

🌐 Internet Notes

- ✅ Most features work without any external AI APIs  
- 🌐 YouTube, Google, Gmail, WhatsApp need an internet connection  
- ❌ No OpenAI key or HuggingFace model required

------------------------------------------------------------

👨‍💻 Made with ❤️ by SOURISH  
Electronics & Telecommunication Engineering Student  
🔗 GitHub: https://github.com/Sourish-Coder07  
📧 Email: sourishnayek07@gmail.com
