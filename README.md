# Orgjunk
Some sorting program I wrote a couple of years ago, seeing as i am still using it to this day i thought it reasonable to upload it for public use for those who find it interesting or useful

##Installation
One can naturally use this through the command line and be very particular about what data you feed it. Alternatively and this is what follows you can decide that you might want to add it to your context menu instead.

![image](https://user-images.githubusercontent.com/25481607/233880107-3d6ac5f4-68c6-48d4-be41-4070328263d0.png)

It would look something akin to that.
Organise would be added as a function to your context menu. Nothing too scary really
However it is definitely worth nothing that this is a rather simple program, its not going to look through subfolders or anything like that. Functionally that would be a nightmare since sometimes I have full programs in folders myself. Considering the chaos that would unleash if this thing would go through all that its not even worth implementing.

Now lets get into brass tax.

1. For the uninitiated the first thing to do is to download the latest version of python https://www.python.org/. At the time of writing I have been using it with python 3.11
2. Next, the program needs to be place somewhere consistent. Personally I have it at C:/PythonPrograms, however it really can be placed anywhere.
3. Now, here is the more complicated bit, we're going to have to use the registry editor. Now im using Windows 11, but it works the same for Windows 10. After all this thing was originally written for Windows 10 so its whatever. The registry Editor will be used to alter the context menu itself. To this end, you should navigate to the following place: Computer\HKEY_CLASSES_ROOT\Directory\Background\shell\

![image](https://user-images.githubusercontent.com/25481607/233880863-3b5ea653-dcef-4265-a533-734ecc290bc6.png)

4. Now that you've reached this point we're going to start making keys, right click shell and make a key. I personally named mine Organise but realistically this particular name doesnt matter at all.

![image](https://user-images.githubusercontent.com/25481607/233881023-952b9bb8-6438-4cf8-bf7a-43aef96dcda1.png)

5. The first key should contain data that describes what the menu is going to display, I like to keep things consistent so i named it too organise, but you can name this what you would like to see when you clean up your folder

![image](https://user-images.githubusercontent.com/25481607/233881203-a2c9ebe6-6c05-4267-abf9-a95482b54100.png)

6. The second key needs to be nested within the Organise key itself, just repeat what you did before, rightclick Organise and add a key. This key NEEDS to be called *command*. All lower case
7. The contents of the command can be edited as well and should contain:
powershell.exe -noexit -command Set-Location -literalPath %V%; $loc = Get-Location; Set-Location "C:\PythonPrograms"; py Orgjunk.py $loc foldersort; Set-Location $loc; Start-Sleep -s 1; exit

This will open powershell, grab the location from which you right clicked and Set the new location to be the location of where you put the program (thats why its important to replace that C drive line there with whatever you have..). Now that its in the folder that you put the program in, its going to execute that program.
It has a couple of parameters, parameter 1 is non negotiable and gets the location with $loc, parameter 2 determines the foldersort. This is a functionality i built in that will grab unknown folders and throw them in a Folders map. Makes things very organised but leaves that particular folder somewhat chaotic, more of a out of sight out of mind functionality really. Afterwards it will sleep for 1 second, giving you a second to read the results and then exit the powershell.

##Alterations
I dont care what you do with this little program, honestly it probably isnt written particularly well seeing as i wrote it ages ago. But it serves its purpose at a reasoable pace. The most I did as a stress test is see how it would handle 1800 files of varying sizes for fun but it does it well enough. I dont really remember what I thought and what I was looking at when I wrote it.

Functionally, for those who aren't really programmers. It is possible to add recogniseable extensions to the program.
You simply edit CONSOLE_LOG and DIRECTORIES.

![image](https://user-images.githubusercontent.com/25481607/233882526-fd7005c7-5996-4729-84a6-d334e7f8477f.png)
![image](https://user-images.githubusercontent.com/25481607/233882627-4d7818b7-a0cd-4594-8e61-3284f680e086.png)

If you add your new folder to both of these your extensions should be recognised as a new folder and their respective extensions will be added.

I honestly already spent more time on this than I thought I would, should you stumble upon this I hope it helps you as much as it has me



