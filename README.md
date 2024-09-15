First do a few things.

Make sure in your Musicbee settings that in preferences>library>playlists that both library and exported playlists use the format M3U. None of the boxes below that should be checked.

Now, make sure you have a way to run, view, and edit python files, I just use visual studio code with python installed.



Now in visual studio code, open the file and you will see line 43 that reads  line.replace("ENTERMUSICOLETPATHHERE", r"ENTERWINDOWSPATHHERE")

Now how I have things organized, I have the same files on my computer and phone at once. So i have the same folder with subfolders of different types of music.

So due to this structure, it allows to only replace the path up to in my case "Ej' Music" and before it.

Assuming you have this same structure, enter your paths into the corresponding parentheses. I would recommend not uneccesarily including the last backslash in the replacement, as python does not seem to like it.

After your add your file paths, in vs code, I run and debug.

After running and debugging, A window should pop up with the ability to select m3us to be processed. Select as many as you like and once they are processed, they will appear in the same folder as the original m3u files with "-win" added to them

you can change the extension in the code if you care, i just used it to differentiate between the two files.

But after that you should be done, shoot me a message on discord if you have questions, ill do my best to help ya :) discord-ej5s
