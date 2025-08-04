readme_content = """# 🧘‍♂️ Japanese LoFi Study – Automated Focus Ritual

![LoFi Background](https://wallpapers.com/images/hd/lo-fi-desktop-n7xhiluyi3nkxcju.jpg)

A Python automation project that recreates my ideal study environment: calm lighting, LoFi beats, and zero distractions. This project was built to both improve my focus and sharpen my Python, API, and automation skills.

--_

## 🧠 What It Does

This tool simulates my personal study ritual using automation:

- Turns on a Govee smart lamp via the Govee API
- Activates Windows Night Light to reduce blue light
- Turns off the second monitor to eliminate distractions like Discord/Twitch
- Launches a curated LoFi playlist via Spotify Web API
- Prepares me to queue up Pomodoro sessions

---

## 🛠 Technologies Used

- **Python 3**
- [Govee API](https://developer.govee.com/)
- [Spotify Web API](https://developer.spotify.com/)
- `spotipy`, `requests`, `pyautogui`, `pydirectinput`
- Windows Task Scheduler
- Environment variable configuration for secure keys

---

## 💡 Why I Built It

I was learning Python and APIs and wanted a project that had personal meaning and immediate impact. This automation lets me switch into “study mode” at the push of a button (or on a schedule). From smart lighting to focus music, it sets the tone for productive evenings — especially when learning technical skills.

> Shoutout to [freeCodeCamp’s Python course](https://www.youtube.com/watch?v=WXsD0ZgxjRw&ab_channel=freeCodeCamp.org) for the jump start!

---

## 🖥️ System Requirements

> **Note:** This is currently tailored for Windows devices.

- Monitor settings must be set to “Extend”
- Night Light must be off by default
- Windows Task Scheduler is recommended for automation
- .bat file included for scheduled execution

---

## 🔐 Environment Variables

Be sure to configure the following variables before running the scripts:

### `spotifyStudy.py`
- `SPOTIPY_CLIENT_ID`
- `SPOTIPY_CLIENT_SECRET`
- `SPOTIFY_USERNAME`

### `govee_turn_on.py`
- `GOVEE_API_KEY`
- `DEVICE_MAC_ADDRESS`
- `DEVICE_MODEL`

---

## 🧪 How I Use It

I run the full stack via Task Scheduler at **7 PM, Monday–Friday** to kick off my evening study sessions. It’s only interrupted my gaming once 😅

---

## 🚀 Next Steps

- Add Pomodoro timer integration
- Include monitor dimming/night light toggles cross-platform
- Option to set the playlist dynamically

---

## 📸 Demo

*(Coming soon — GIF or video of the automation in action)*
"""

readme_path = "/mnt/data/README.md"
with open(readme_path, "w") as f:
    f.write(readme_content)

readme_path
