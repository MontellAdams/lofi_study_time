# Japanese LoFi Study

![Test picture](https://www.japannakama.co.uk/wp-content/uploads/2021/09/aesthetic-anime-purple-lo-fi-backgrounds.jpg)

<h2>My study ritual: </h2>

I've always enjoyed listening to LoFi music while studying technical things and found that I have a "study ritual" that just seems to happen to improve my focus, so I figured I could automate it


<html>
<body>

<ul>
<li>Turn off my room light (unfortunately not included here)</li>
<li>Turn on my Govee lamp </li>
<li>Turn on night light on my computer to reduce blue light</li>
<li>Turn off my second monitor so I'm not distracted by Discord or Twitch</li>
<li>Set up some tasks in the Pomodoro app -- usually 5+ Pomodoros</li>
<li>Que the Lofi!</li>
</ul>  

</body>
</html>



<h2>Why Python?</h2> 

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNUNPFhhzbSCpEuXeYAFUQtsszTYopFbQ29g_fReo&usqp=CAE&s)

I really wanted to work on my Python skills and learn about APIs to automate more of my tasks for work. Figured a project that increased my productivity studying Python would be a win-win.[Shout out to FreeCodeCamp](https://www.youtube.com/watch?v=WXsD0ZgxjRw&ab_channel=freeCodeCamp.org)

Then went from the Govee API to Spotify to learning about the pyautogui library 

This project lets me automate my study ritual and when configured with a task schedule I never forget it's time to start studying when my monitor turns off and I start hearing Eternal Youth



<h2>To Install: </h2>

<b> Currently this would only work for Windows machines </b>

The batch file needs to path to the applications and python scripts and the assumption is made that your Monitor project settings are currently set to 'Extend' and that Night Light is not enabled. 

Once the batch script has the correct paths, you can set up a task scheduler to automate the bash script. I currently force it to run at 7 PM M-F to ensure I get a few hours of study in.

It's only interrupted gaming once haha You will need to make sure you configure environment variables for the following variables:

<b>japaneseLoFiStudy.py</b>

<li>'SPOTIPY_CLIENT_ID'</li>
<li>'SPOTIPY_CLIENT_SECRET'</li>
<li>'SPOTIFY_USERNAME'</li>

<b>govee_turn_on.py</b>

<li>'GOVEE_API_KEY'</li>
<li>'DEVICE_MAC_ADDRESS'</li>
<li>'DEVICE_MODEL'</li>





