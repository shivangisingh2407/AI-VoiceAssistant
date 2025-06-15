    import pyttsx3
    import pyautogui  #screenshot
    import speech_recognition as sr
    import datetime
    import pywhatkit #send message / youtube /google
    import pyjokes
    import wikipedia
    import os  #system command --lock
    import subprocess  # run external python file
    import tkinter as tk #make gui calculator
    from tkinter import messagebox
    import threading  #multiple work at a time
    import time as t
    import sys   # For shutdown and restart commands
    import jarvis_gui # Assuming your GUI script is named 'jarvis_gui.py'
    import requests # api
    import random #for random answer


    GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis",
                "time to work jarvis", "hey jarvis", "ok jarvis", "are you there"]

    GREETINGS_RES = ["always there for you mam", "i am ready mam",
                    "your wish my command", "how can i help you mam?",
                    "i am online and ready mam"]

    # Add the greeting check right below these constants
    def run_jarvis():
        load_reminders_from_file()
        threading.Thread(target=check_reminders, daemon=True).start()
        wish_me()

        while True:
            query = take_command()





    #================remainder====================

    REMINDER_FILE = "reminders.txt"




    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1)


    def speak(text):
        print("JARVIS:", text)
        engine.say(text)
        engine.runAndWait()


    def wish_me():
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            speak("Good Morning Shivangi!")
        elif 12 <= hour < 18:
            speak("Good Afternoon Shivangi!")
        else:
            speak("Good Evening Shivangi!")
        speak("Initializing Jarvis")
        speak("Starting all systems applications")
        speak("Installing and checking all drivers")
        speak("Caliberating and examining all the core processors")
        speak("Checking the internet connection")
        speak("Wait a moment mam")
        speak("All drivers are up and running")
        speak("All systems have been activated")
        speak("Now I am online")
        speak("Mam, How can I help you today?")


    def take_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎙 Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("🧠 Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"🗣 You said: {query}")
        except Exception:
            print("❌ Could not understand. Say that again...")
            return "None"
        return query.lower()




    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


    # Function to set volume level
    def set_volume(volume_level):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, 1, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)

        # Convert volume level (0-100 scale) to the acceptable scale (0.0-1.0)
        volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)
        speak(f"Volume set to {volume_level}%")


    # Function to mute/unmute
    def mute_unmute():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, 1, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)

        # Toggle mute/unmute
        mute_state = volume.GetMute()
        volume.SetMute(not mute_state, None)
        speak("Muted" if not mute_state else "Unmuted")





    #===============Photo======================

    import cv2
    import numpy as np
    from PIL import Image, ImageEnhance, ImageFilter

    # Global variable to store last photo path
    last_photo_path = ""

    def camera_control(command):
        global last_photo_path
        if "take my photo" in command:
            speak("Opening camera. Please smile!")
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('Press Space to Capture', frame)
                if cv2.waitKey(1) & 0xFF == ord(' '):
                    photo_name = "my_photo.jpg"
                    cv2.imwrite(photo_name, frame)
                    speak("Photo taken and saved as my_photo.jpg")
                    last_photo_path = photo_name
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "add a filter" in command:
            if last_photo_path != "":
                speak("Adding filter to your photo.")
                image = Image.open(last_photo_path)
                # Example: blur + brightness increase
                image = image.filter(ImageFilter.BLUR)
                enhancer = ImageEnhance.Brightness(image)
                image = enhancer.enhance(1.5)
                filtered_photo = "my_photo_filtered.jpg"
                image.save(filtered_photo)
                speak(f"Filter applied and saved as {filtered_photo}")
                image.show()
            else:
                speak("No photo found. Please take a photo first.")

        elif "show my photo" in command:
            if last_photo_path != "":
                speak("Showing your photo.")
                image = Image.open(last_photo_path)
                image.show()
            else:
                speak("No photo to show. Please take a photo first.")





    #=============Weather===============

    def get_weather(city_name):
        api_key = ""  # <-- Apni OpenWeatherMap wali API key yahan paste karna
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            weather_data = data["main"]
            temperature = weather_data["temp"]
            pressure = weather_data["pressure"]
            humidity = weather_data["humidity"]
            weather_description = data["weather"][0]["description"]

            speak(f"The temperature in {city_name} is {temperature} degrees Celsius.")
            speak(f"The weather is {weather_description}.")
            speak(f"Humidity is {humidity} percent.")
            speak(f"Pressure is {pressure} hectopascal.")
        else:
            speak("Sorry, I couldn't find that city.")



    # ==================== Screenshot section========================

    def take_screenshot():
        speak("Taking a screenshot.")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"
        screenshot_folder = "Screenshots"
        os.makedirs(screenshot_folder, exist_ok=True)
        path = os.path.join(screenshot_folder, filename)
        pyautogui.screenshot(path)
        speak(f"Screenshot saved as {filename} in Screenshots folder.")



    #===================News Headlines====================

    # import requests

    NEWS_API_KEY = ""  # Replace with your actual API key

    def get_news():
        speak("Fetching the latest headlines from Times of India.")
        url = f"={NEWS_API_KEY}"

        try:
            response = requests.get(url)
            data = response.json()

            if data["status"] == "ok":
                articles = data["articles"]
                if not articles:
                    speak("Sorry, I couldn't find any news at the moment.")
                    return

                speak("Here are the top 5 news headlines from Times of India:")
                for i, article in enumerate(articles[:5], 1):
                    speak(f"Headline {i}: {article['title']}")
            else:
                speak("Sorry, I was unable to fetch the news.")
        except Exception as e:
            print("Error:", e)
            speak("Something went wrong while trying to fetch the news.")



    # ===================== Reminder Section ========================
    reminders = []


    def save_reminders_to_file():
        with open(REMINDER_FILE, "w") as f:
            for reminder in reminders:
                f.write(f"{reminder[0].hour}:{reminder[0].minute}|{reminder[1]}\n")


    def load_reminders_from_file():
        if not os.path.exists(REMINDER_FILE):
            return
        with open(REMINDER_FILE, "r") as f:
            for line in f:
                try:
                    time_part, task = line.strip().split("|")
                    hour, minute = map(int, time_part.split(":"))
                    reminders.append((datetime.time(hour, minute), task))
                except Exception as e:
                    print("Error loading reminder:", e)
                    continue


    def set_reminder():
        speak("What should I remind you about?")
        task = take_command()
        if task == "None":
            speak("I didn't catch that. Please tell me again.")
            return

        speak("When should I remind you? Please say the time in 24-hour format, like 14 30 for 2:30 PM or 1350 for 13:50")
        time_input = take_command()
        if time_input == "None":
            speak("I didn't catch that. Please tell me the time again.")
            return

        try:
            # Check if time_input has 4 digits (e.g., 1350), split it into hour and minute
            if len(time_input) == 4 and time_input.isdigit():
                hour = int(time_input[:2])
                minute = int(time_input[2:])
            else:
                hour, minute = map(int, time_input.split())

            # Validate time range
            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                raise ValueError("Invalid time format")

            reminder_time = datetime.time(hour, minute)
            reminders.append((reminder_time, task))
            save_reminders_to_file()
            speak(f"Reminder set for {hour}:{minute:02d} to {task}")
        except ValueError:
            speak("Sorry, I couldn't understand the time format. Please try again.")


    def check_reminders():
        while True:
            now = datetime.datetime.now().time()
            for reminder in reminders[:]:
                if now.hour == reminder[0].hour and now.minute == reminder[0].minute:
                    speak(f"It's {now.strftime('%H:%M')}, time to {reminder[1]}")  # Announcing time and task
                    reminders.remove(reminder)  # Remove the reminder once it's done
                    save_reminders_to_file()  # Save the updated reminder list
            t.sleep(30)  # Check every 30 seconds


    # ======================send whatsapp message=======================

    def send_whatsapp_message():
        speak("Please tell me the phone number with country code")
        phone_number = take_command().replace("","").strip()
        speak("What message should I send?")
        message = take_command()
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1
        speak(f"Sending your message to {phone_number} at {hour}:{minute}")
        try:
            pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
            speak("Message scheduled successfully!")
        except Exception as e:
            print("Error:", e)
            speak("Failed to send message. Please try again.")



    #=================Youtube & Google==============================

    # import speech_recognition as sr
    # import pywhatkit

    # Initialize recognizer class (for recognizing speech)
    recognizer = sr.Recognizer()

    def listen():
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)  # Capture audio from the microphone
            try:
                print("Recognizing...")
                query = recognizer.recognize_google(audio)  # Recognize speech using Google Web Speech API
                print(f"You said: {query}")
                return query.lower()  # Return the query in lowercase for consistency
            except sr.UnknownValueError:
                print("Sorry, I could not understand what you said.")
                return ""
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
                return ""

    def open_google_or_youtube(query):
        if 'open google' in query:
            speak("What should I search on Google?")
            search_query = listen()  # Get the user's search query
            if search_query:
                speak(f"Searching for {search_query} on Google")
                pywhatkit.search(search_query)

        elif 'open youtube' in query:
            speak("What should I search on YouTube?")
            search_query = listen()  # Get the user's search query
            if search_query:
                speak(f"Searching for {search_query} on YouTube")
                pywhatkit.search(search_query)


    #====================notepad=======================


    def open_notepad():
        speak("Opening your custom notepad.")
        subprocess.Popen(["python", "jarvis_notepad.py"])



    #======================Calculator======================


    def calculator(query):
        try:
            expression = query.replace("plus", "+").replace("minus", "-").replace("times", "*").replace("divided by", "/")
            result = eval(expression)
            speak(f"The result is {result}")
        except Exception:
            speak("Sorry, I couldn't calculate that. Please check your expression.")


    def open_gui_calculator():
        def on_button_click(value):
            current_text = display.get()
            display.delete(0, tk.END)
            display.insert(tk.END, current_text + value)

        def on_clear():
            display.delete(0, tk.END)

        def on_equal():
            try:
                result = eval(display.get())
                display.delete(0, tk.END)
                display.insert(tk.END, str(result))
            except Exception:
                display.delete(0, tk.END)
                display.insert(tk.END, "Error")

        window = tk.Tk()
        window.title("JARVIS Calculator")

        display = tk.Entry(window, width=20, font=("Arial", 24), borderwidth=2, relief="solid")
        display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 18),
                            command=lambda t=text: on_button_click(
                                t) if t != "=" and t != "C" else on_equal() if t == "=" else on_clear())
            button.grid(row=row, column=col)

        window.mainloop()


    # ==================== Lock, Shutdown, Restart ======================

    def lock_system():
        speak("Locking the system.")
        os.system("rundll32.exe user32.dll,LockWorkStation")  # Lock system using Windows command

    def shutdown_system():
        speak("Shutting down the system.")
        os.system("shutdown /s /f /t 1")  # Force shutdown with 1 second delay

    def restart_system():
        speak("Restarting the system.")
        os.system("shutdown /r /f /t 1")  # Force restart with 1 second delay


    # =====================================================================

    def run_jarvis():
        load_reminders_from_file()
        threading.Thread(target=check_reminders, daemon=True).start()
        wish_me()
        while True:
            query = take_command()

            if any(greeting in query for greeting in GREETINGS):
                response = random.choice(GREETINGS_RES)
                speak(response)
                continue

            elif 'who are you' in query:
                speak(
                    "I am JARVIS, your personal assistant created by shivangi singh. I am here to help you with various tasks like setting reminders, opening apps, playing music, and much more. How can I assist you today?")
                continue


            elif 'time' in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak(f"The time is {time}")

            elif 'date' in query:
                date = datetime.datetime.now().strftime('%B %d, %Y')
                speak(f"Today's date is {date}")

            elif 'shutdown' in query:
                shutdown_system()

            elif 'restart' in query:
                restart_system()

            elif 'lock system' in query:
                lock_system()

            elif 'open youtube' in query:
                speak("What should I search on YouTube?")
                search_query = listen()  # Get the user's search query
                if search_query:
                    speak(f"Searching for {search_query} on YouTube")
                    pywhatkit.playonyt(search_query)  # Directly plays the video on YouTube

            elif 'open google' in query:
                speak("What should I search on Google?")
                search_query = listen()  # Get the user's search query
                if search_query:
                    speak(f"Searching for {search_query} on Google")
                    pywhatkit.search(search_query)

            elif 'play song' in query:
                speak("What song should I play?")
                song = take_command()
                pywhatkit.playonyt(song)

            elif 'who is' in query:
                person = query.replace("who is", "").strip()
                if person:
                    try:
                        info = wikipedia.summary(person, sentences=2)
                        speak(info)
                    except:
                        speak("Sorry, I couldn't fetch the information.")
                else:
                    speak("Whom do you want to search for? Please say again.")

            elif 'joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'open command prompt' in query or 'open cmd' in query:
                speak("Opening Command Prompt")
                os.system('start cmd')

            elif 'send whatsapp message' in query:
                send_whatsapp_message()

            elif 'notepad' in query:
                open_notepad()

            elif 'calculator' in query or 'calculate' in query:
                speak("Do you want to use the text-based calculator or a GUI calculator?")
                response = take_command()
                if 'gui' in response:
                    open_gui_calculator()

                elif 'text' in response or 'command' in response:
                    speak("What calculation would you like me to perform?")
                    expression = take_command()
                    calculator(expression)
                else:
                    speak("Sorry, I didn't understand. Please choose either GUI or text-based.")

            elif 'set reminder' in query or 'remind me' in query:
                set_reminder()

            elif 'take screenshot' in query or 'screenshot' in query:
                take_screenshot()

            elif 'set volume to' in query:
                volume_level = [int(word) for word in query.split() if word.isdigit()]
                if volume_level:
                    set_volume(volume_level[0])

            elif 'mute' in query or 'unmute' in query:
                mute_unmute()

            elif 'read pdf' in query or 'open pdf' in query:
                read_pdf()

            elif 'news' in query or 'headlines' in query:
                get_news()

            elif 'weather' in query :
                speak("Which city's weather do you want to know?")
                city  = take_command()
                get_weather(city)



            elif "take my photo" in query or "add a filter" in query or "show my photo" in query:
                camera_control(query)



            elif 'exit' in query or 'stop' in query or 'good night' in query:
                speak("Goodbye! Have a nice day.")
                sys.exit()


            else:
                speak("Sorry, I didn't catch that. Can you say it again?")


    if __name__ == "__main__":
        run_jarvis()









