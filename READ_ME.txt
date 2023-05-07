File Q&A
(note) make sure to update the .env and .yaml files with your personal openai and pincone apis
(note) run the following instructions in the powershell or command prompt

Server Setup:
python -m venv venv
.\venv\Scripts\activate.bat
cd openai-cookbook-main\apps\file-q-and-a\nextjs-with-flask-server\server
pip install openai
npm install openai
pip install -r .\requirements.txt
python .\app.py

Client Setup:
cd openai-cookbook-main\apps\file-q-and-a\nextjs-with-flask-server\client
python -m venv venv
.\venv\Scripts\activate.bat
pip install openai
npm install openai
npm install
npm run dev
http://localhost:3000

----------------------------------------------------------------------------------------------

Web Crawl Q&A
(note) make sure to update the .env file with your personal openai api
(note) run the following instructions in the powershell or command prompt

General Setup:
python -m venv venv
.\venv\Scripts\activate.bat
pip install -r .\requirements.txt
python .\web-qa.py

----------------------------------------------------------------------------------------------

Traffic Light Controller
The program will require the following libraries:
-time
-pynq

Additionally, the hardware is based on these components:
-one button
-six LEDs
-seven segment display

The code is based on a countdown module and a finite state machine.
To run, simply have the KRIA board invoke the "traffic_controller.py" file.