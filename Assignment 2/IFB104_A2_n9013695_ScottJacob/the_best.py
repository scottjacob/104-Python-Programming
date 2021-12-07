
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9013695
#    Student name: Scott Jacob
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  The Best, Then and Now
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to preview and print lists of
#  top-ten rankings.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.  YOU MAY NOT USE
# ANY NON-STANDARD MODULES SUCH AS 'Beautiful Soup' OR 'Pillow'.  ONLY
# MODULES THAT COME WITH A STANDARD PYTHON 3 INSTALLATION MAY BE
# USED.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import webbrowser to use .open and .get to open html natively
import webbrowser


from html.parser import HTMLParser
from urllib import parse


# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *
# Import tkinter extras
from tkinter import ttk
from tkinter import messagebox

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

# Import Regex module for searching strings
from re import *

# Import modules needed for directory changing
from os import chdir, getcwd
# Import platform to determine OS for chdir functionality
import platform

# Import time for sleep function
import time
from datetime import date
#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce a
# meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
''' def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_filename + "'")

    # Return the downloaded document to the caller
    return web_page_contents '''

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

##### DEVELOP YOUR SOLUTION HERE #####

###############################################################################
#                            Date Operations                                  #
###############################################################################
# months_date = [1,2,3,4,5,6,7,8,9,10,11,12]
# days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
# Attemting to set variable dates to lookup for date() but the function only takes single 
# integer arguments or two arguments via an or operator, OR AND operators
# both return the first available integer in the pattern

# Set program to append current date in downloaded files
the_date = date.today()

#any_date = date(year=2018 or 2019, month=int in months_date, day=int in days)
###############################################################################
#                           HTML - Updater - Offline                          #
###############################################################################
def html_update_all_offline():
    
    change_dir() # call and execute change directory function to ensure we are in /archive

    url = 'https://coinmarketcap.com/gainers-losers/'
    # Open the web document for reading
    web_page = urlopen(url)

    # Read its contents as a Unicode string
    web_page_contents = web_page.read().decode('UTF-8')

    # Write the contents to a text file (overwriting the file if it
    # already exists!)
    html_file = open('coinmarketcap.html', 'w', encoding = 'UTF-8')
    html_file.write(web_page_contents)
    html_file.close()
    time.sleep(float(0.75))

    url = 'https://store.steampowered.com/stats/'
    # Open the web document for reading
    web_page = urlopen(url)

    # Read its contents as a Unicode string
    web_page_contents = web_page.read().decode('UTF-8')

    # Write the contents to a text file (overwriting the file if it
    # already exists!)
    html_file = open('steamstats.html', 'w', encoding = 'UTF-8')
    html_file.write(web_page_contents)
    html_file.close()
    time.sleep(float(0.75))

    url = 'https://www.imdb.com/chart/tvmeter/'
    # Open the web document for reading
    web_page = urlopen(url)

    # Read its contents as a Unicode string
    web_page_contents = web_page.read().decode('UTF-8')

    # Write the contents to a text file (overwriting the file if it
    # already exists!)
    html_file = open('imdbtv.html', 'w', encoding = 'UTF-8')
    html_file.write(web_page_contents)
    html_file.close()
    time.sleep(float(0.75))



#*****************************************************************************#
#                        Live List Generator Function                         #
#*****************************************************************************#

''' These two functions build the lists for the live view in the GUI,
there are two as the regex for the second pulls extra data before the
needed list entries '''

def list_gen_one_four(listentry):
    list_elem_1 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][0], font=("Source Code Pro", 8))
    list_elem_1.pack(anchor=N)
    list_elem_1.place(x=190, y=265)

    list_elem_2 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][1], font=("Source Code Pro", 8))
    list_elem_2.pack(anchor=N)
    list_elem_2.place(x=190, y=295)

    list_elem_3 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][2], font=("Source Code Pro", 8))
    list_elem_3.pack(anchor=N)
    list_elem_3.place(x=190, y=325)

    list_elem_4 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][3], font=("Source Code Pro", 8))
    list_elem_4.pack(anchor=N)
    list_elem_4.place(x=190, y=355)

    list_elem_5 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][4], font=("Source Code Pro", 8))
    list_elem_5.pack(anchor=N)
    list_elem_5.place(x=190, y=385)

    list_elem_6 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][5], font=("Source Code Pro", 8))
    list_elem_6.pack(anchor=N)
    list_elem_6.place(x=190, y=415)

    list_elem_7 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][6], font=("Source Code Pro", 8))
    list_elem_7.pack(anchor=N)
    list_elem_7.place(x=190, y=445)

    list_elem_8 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][7], font=("Source Code Pro", 8))
    list_elem_8.pack(anchor=N)
    list_elem_8.place(x=190, y=475)

    list_elem_9 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][8], font=("Source Code Pro", 8))
    list_elem_9.pack(anchor=N)
    list_elem_9.place(x=190, y=505)

    list_elem_10 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][9], font=("Source Code Pro", 8))
    list_elem_10.pack(anchor=N)
    list_elem_10.place(x=190, y=535)

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#

def list_gen_five_six(listentry):
    list_elem_1 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][2], font=("Source Code Pro", 8))
    list_elem_1.pack(anchor=N)
    list_elem_1.place(x=190, y=265)

    list_elem_2 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][3], font=("Source Code Pro", 8))
    list_elem_2.pack(anchor=N)
    list_elem_2.place(x=190, y=295)

    list_elem_3 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][4], font=("Source Code Pro", 8))
    list_elem_3.pack(anchor=N)
    list_elem_3.place(x=190, y=325)

    list_elem_4 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][5], font=("Source Code Pro", 8))
    list_elem_4.pack(anchor=N)
    list_elem_4.place(x=190, y=355)

    list_elem_5 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][6], font=("Source Code Pro", 8))
    list_elem_5.pack(anchor=N)
    list_elem_5.place(x=190, y=385)

    list_elem_6 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][7], font=("Source Code Pro", 8))
    list_elem_6.pack(anchor=N)
    list_elem_6.place(x=190, y=415)

    list_elem_7 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][8], font=("Source Code Pro", 8))
    list_elem_7.pack(anchor=N)
    list_elem_7.place(x=190, y=445)

    list_elem_8 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][9], font=("Source Code Pro", 8))
    list_elem_8.pack(anchor=N)
    list_elem_8.place(x=190, y=475)

    list_elem_9 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][8], font=("Source Code Pro", 8))
    list_elem_9.pack(anchor=N)
    list_elem_9.place(x=190, y=505)

    list_elem_10 = Label(root, bg="white", justify=LEFT, height=1, width=30, text=listentry[0][9], font=("Source Code Pro", 8))
    list_elem_10.pack(anchor=N)
    list_elem_10.place(x=190, y=535)


#*****************************************************************************#
#                          Change Directory Function                          #
#*****************************************************************************#

''' This function changes the directory to /Archive in order to download pages
and perform regex expressions to scrape data. This function determines operating
system in use with platform.platform and checks for it using if statements.
MacOS can be used as an argument in this function and performs correctly, however
in the following generator functions "MacOS" does not return as an argument and
as such the argument is changed to "Darwin" '''

def change_dir():
    current_os = platform.platform()
    
    if "Windows" in current_os:
        if "Archive" not in getcwd():

            archive = r'/Archive/'
    
            cwd = getcwd()
            #print(cwd)

            newdir = cwd + archive
            chdir(newdir)
            #print(cwd)
        else:
            print("already in working directory")
    else:
        print("Trying Linux or MacOS")

    if "Linux" or "MacOS" in current_os:
        if "Archive" not in getcwd():
    
            archive = r'/Archive'
    
            cwd = getcwd()
            #print(cwd)

            newdir = cwd + archive
            chdir(newdir)
        else:
            print("already in working directory")
    else:
        print("unknown OS running")

#*****************************************************************************#
#                         Downloader functions                                #
#*****************************************************************************#
# This GUI uses similar downloader functions for each radio button
# The radio button executes the corresponding function for each item
# Offline downloader function does not access the internet
# Online downloaders access the internet, perform regex and display to the GUI
# as such there is some latency involved when executing especially on IMDB

''' Continue testing rate limiting via .sleep() method 
    current setting is set to 75ms via float()... 
    adjust as needed for performance
'''


# Downloader - Function was previously used in past IFB104 Assignments
def downloader_one():
    change_dir() # call and execute change directory function to ensure we are in /archive

    # Live View
    # Create canvas for live view
    preview_canvas = Canvas(root, bg="white", height="360", width="575")
    preview_canvas.pack()
    preview_canvas.place(x=190, y=200)

    preview_image = PhotoImage(master=root, width="255", height="240", file="../crypto_main.png")
    image = Label(justify=CENTER, image=preview_image)
    image.image = preview_image
    image.place(x=450, y=260)

    url = 'https://coinmarketcap.com/gainers-losers/'
    # Open the web document for reading
    web_page = urlopen(url)

    # Read its contents as a Unicode string
    web_page_contents = web_page.read().decode('UTF-8')

    # Write the contents to a text file (overwriting the file if it
    # already exists!)
    html_file = open('coinmarketcapnew'+str(the_date)+'.html', 'w', encoding = 'UTF-8')
    html_file.write(web_page_contents)
    html_file.close()
    time.sleep(float(0.75))

    top_ten_list_one = []
    # main regex statement uses "(.*?)" - wildcard to pull all data from inbetween arguments
    top_ten_list_one.append(findall('<a href="/currencies/(.*?)/#markets" class="volume" data-usd="[0-9]+[.]+[0-9]+">(.*?)</a>', web_page_contents)) # (.*?) quick regex which grabs everything
    
    #print(top_ten_list_one) # Test for correct regex
    preview_title = Label(root, bg="white", justify=LEFT, height=2, width=40, text="Top Crypto Gainers - Hourly Updated", font=("Source Code Pro", 14))
    preview_title.pack(anchor=N)
    preview_title.place(x=200, y=205)

    list_gen_one_four(top_ten_list_one)


def offline_view_one():
    change_dir() # call and execute change directory function to ensure we are in /archive

    # Live View
    # Create canvas for live view
    preview_canvas = Canvas(root, bg="white", height="360", width="575")
    preview_canvas.pack()
    preview_canvas.place(x=190, y=200)

    preview_image = PhotoImage(master=root, width="255", height="240", file="../crypto_main.png")
    image = Label(justify=CENTER, image=preview_image)
    image.image = preview_image
    image.place(x=450, y=260)

    html_file = open('coinmarketcap.html', 'r', encoding = 'UTF-8')
    html_contents = html_file.read()
    html_file.close()
    time.sleep(float(0.75))

    top_ten_list_one = []
    # main regex statement uses "(.*?)" - wildcard to pull all data from inbetween arguments
    top_ten_list_one.append(findall('<a href="/currencies/(.*?)/#markets" class="volume" data-usd="[0-9]+[.]+[0-9]+">(.*?)</a>', html_contents))
    
    #print(top_ten_list_one) # Test for correct regex
    preview_title = Label(root, bg="white", justify=LEFT, height=2, width=40, text="Top Crypto Gainers - Past", font=("Source Code Pro", 14))
    preview_title.pack(anchor=N)
    preview_title.place(x=200, y=205)

    list_gen_one_four(top_ten_list_one)



# Downloader - Function was previously used in past IFB104 Assignments
def downloader_two():
    change_dir() # call and execute change directory function to ensure we are in /archive


    # Live View
    # Create canvas for live view
    preview_canvas = Canvas(root, bg="white", height="360", width="575")
    preview_canvas.pack()
    preview_canvas.place(x=190, y=200)

    preview_image = PhotoImage(master=root, width="360", height="200", file="../steam_main.png")
    image = Label(justify=CENTER, image=preview_image)
    image.image = preview_image
    image.place(x=400, y=260)

    url = 'https://store.steampowered.com/stats/'
    # Open the web document for reading
    web_page = urlopen(url)

    # Read its contents as a Unicode string
    web_page_contents = web_page.read().decode('UTF-8')

    # Write the contents to a text file (overwriting the file if it
    # already exists!)
    html_file = open('steamstatsnew'+str(the_date)+'.html', 'w', encoding = 'UTF-8')
    html_file.write(web_page_contents)
    html_file.close()
    time.sleep(float(0.75))


    top_ten_list_two = []
    top_ten_list_two.append(findall('href="https://store.steampowered.com/app/[0-9]*/.*?">(.*?)</a>', web_page_contents))

    #print(top_ten_list_two) # Test for correct regex
    preview_title = Label(root, bg="white", justify=LEFT, height=2, width=40, text="Most Played Steam Games - Current", font=("Source Code Pro", 14))
    preview_title.pack(anchor=N)
    preview_title.place(x=200, y=205)

    list_gen_one_four(top_ten_list_two)


def offline_view_two():
    
    change_dir() # call and execute change directory function to ensure we are in /archive

    # Live View
    # Create canvas for live view
    preview_canvas = Canvas(root, bg="white", height="360", width="575")
    preview_canvas.pack()
    preview_canvas.place(x=190, y=200)

    preview_image = PhotoImage(master=root, width="360", height="200", file="../steam_main.png")
    image = Label(justify=CENTER, image=preview_image)
    image.image = preview_image
    image.place(x=400, y=260)


    html_file = open('steamstats.html', 'r', encoding = 'UTF-8')
    html_contents = html_file.read()
    html_file.close()
    time.sleep(float(0.75))


    top_ten_list_two = []
    top_ten_list_two.append(findall('href="https://store.steampowered.com/app/[0-9]*/.*?">(.*?)</a>', html_contents))
    
    #print(top_ten_list_two) # Test for correct regex
    preview_title = Label(root, bg="white", justify=LEFT, height=2, width=40, text="Most Played Steam Games - Past", font=("Source Code Pro", 14))
    preview_title.pack(anchor=N)
    preview_title.place(x=200, y=205)

    list_gen_one_four(top_ten_list_two)


def downloader_three():
    change_dir() # call and execute change directory function to ensure we are in /archive


    # Live View
    # Create canvas for live view
    preview_canvas = Canvas(root, bg="white", height="360", width="575")
    preview_canvas.pack()
    preview_canvas.place(x=190, y=200)

    preview_image = PhotoImage(master=root, width="325", height="260", file="../movie_main.png")
    image = Label(justify=CENTER, image=preview_image)
    image.image = preview_image
    image.place(x=440, y=260)

    url = 'https://www.imdb.com/chart/tvmeter/'
    # Open the web document for reading
    web_page = urlopen(url)

    # Read its contents as a Unicode string
    web_page_contents = web_page.read().decode('UTF-8')

    # Write the contents to a text file (overwriting the file if it
    # already exists!)
    html_file = open('imdbtvnew'+str(the_date)+'.html', 'w', encoding = 'UTF-8')
    html_file.write(web_page_contents)
    html_file.close()
    time.sleep(float(0.75))


    top_ten_list_three = []
    top_ten_list_three.append(findall('<a href=".*?"\ntitle=".*?" >(.*?)</a>', web_page_contents))

    #print(top_ten_list_three) # Test for correct regex
    preview_title = Label(root, bg="white", justify=LEFT, height=2, width=40, text="Top TV Shows IMDB - Current", font=("Source Code Pro", 14))
    preview_title.pack(anchor=N)
    preview_title.place(x=200, y=205)

    list_gen_five_six(top_ten_list_three)


def offline_view_three():
    change_dir() # call and execute change directory function to ensure we are in /archive

    # Live View
    # Create canvas for live view
    preview_canvas = Canvas(root, bg="white", height="360", width="575")
    preview_canvas.pack()
    preview_canvas.place(x=190, y=200)

    preview_image = PhotoImage(master=root, width="325", height="260", file="../movie_main.png")
    image = Label(justify=CENTER, image=preview_image)
    image.image = preview_image
    image.place(x=440, y=260)


    html_file = open('imdbtv.html', 'r', encoding = 'UTF-8')
    html_contents = html_file.read()
    html_file.close()
    time.sleep(float(0.75))


    top_ten_list_three = []
    top_ten_list_three.append(findall('<a href=".*?"\ntitle=".*?" >(.*?)</a>', html_contents))
    
    
    #print(top_ten_list_three) # Test for correct regex
    preview_title = Label(root, bg="white", justify=LEFT, height=2, width=40, text="Top TV Shows IMDB - Past", font=("Source Code Pro", 14))
    preview_title.pack(anchor=N)
    preview_title.place(x=200, y=205)

    list_gen_five_six(top_ten_list_three)

#*****************************************************************************#
#                             Save List                                       #
#*****************************************************************************#

def save_list():
    # Functionality not completed
    # Pressing button serves error box
    # Ran out of time and patience to complete this section
    # Current format for retrieving data would require re-write of regex strings
    # to complete this section
    """ # connect to database
    db_conn = connect('top_ten.db')
    c = db_conn.cursor()
    c.execute("INSERT INTO item FROM ") 
    """
       
    if var.get() == 1:
        print("Saving List One Offline")
        message_box = messagebox.showerror("Error", " Functionality Not Completed")

        # c.execute("INSERT INTO publication_date VALUES")
        # c.execute("INSERT INTO ranking VALUES")
        # c.execute("INSERT INTO item VALUES")
        # c.execute("INSERT INTO main_attribute VALUES")
        
    elif var.get() == 2:
        print("Saving List One Online")
        message_box = messagebox.showerror("Error", "Functionality Not Completed")

    elif var.get() == 3:
        print("Saving List One Offline")
        message_box = messagebox.showerror("Error", "Functionality Not Completed")

    elif var.get() == 4:
        print("Saving List One Offline")
        message_box = messagebox.showerror("Error", "Functionality Not Completed")

    elif var.get() == 5:
        print("Saving List One Offline")
        message_box = messagebox.showerror("Error", "Functionality Not Completed")

    elif var.get() == 6:
        print("Saving List One Offline")
        message_box = messagebox.showerror("Error", "Functionality Not Completed")

    else:
        print("No List Selected")


#*****************************************************************************#
#                             Exporter Function                               #
#*****************************************************************************#
''' This function is the main loop for the exporter button, this function
calls the generator functions for the html pages as well as spits messages
to stdout via print for troubleshooting '''

def exporter():
    print(var.get()) # this statement checks for button input and prints it (1-6)

    if var.get() == 1:
        print("Offline crypto export")
        html_generate_one_offline()
    
    elif var.get() == 2:
        print("Online crypto export")
        html_generate_one_online()

    elif var.get() == 3:
        print("Offline steam export")
        html_generate_two_offline()

    elif var.get() == 4:
        print("Online steam export")
        html_generate_two_online()

    elif var.get() == 5:
        print("Offline imdb export")
        html_generate_three_offline()

    elif var.get() == 6:
        print("Online imdb export")
        html_generate_three_online()

    else:
        print("Nothing selected")



#*****************************************************************************#
#                               Main App setup                                #
#*****************************************************************************#
''' This section initialises the main tkinter app as well as button and label
placement. '''


root = Tk() # Initialise tkinter

root.title("Just Another List - A Top Ten List Generator") # window title set
root.configure(bg="black") # Set background to black
root.resizable(width=False, height=False) # Disable resizing of window

logo_main = PhotoImage(height="150", width="800", file="justanotherlist.png") # place logo
image = Label(justify=CENTER, image=logo_main)
image.place(x=0, y=0)

inner_border = Canvas(root, bg="white", height="450", width="750") # canvas next to buttons for live display
inner_border.pack()
inner_border.place(x=25, y=175)

var = IntVar() # Allows for individual selections from radio buttons, referenced later in exporter function

list_one_label = Label(root, height=3, width=20, text="Crypto Currencies", font=("Source Code Pro", 8), bg="light grey", relief=FLAT, )
list_one_label.pack(anchor=W)
list_one_label.place(x=30 ,y=200)


list_two_label = Label(root, height=3, width=20, text="Steam Top Games", font=("Source Code Pro", 8), bg="light grey", relief=FLAT, )
list_two_label.pack(anchor=W)
list_two_label.place(x=30 ,y=300)


list_two_label = Label(root, height=3, width=20, text="IMDB Top TV Shows", font=("Source Code Pro", 8), bg="light grey", relief=FLAT, )
list_two_label.pack(anchor=W)
list_two_label.place(x=30 ,y=400)

# List one radio buttons
r1_past = Radiobutton(root, fg='blue', height=1, width=5, text="Past", font=("Source Code Pro", 8), variable=var, value=1, command=offline_view_one)
r1_past.pack()
r1_past.place(x=30, y=265)

r1_current = Radiobutton(root, fg='red', height=1, width=8, text="Current", font=("Source Code Pro", 8), variable=var, value=2, command=downloader_one)
r1_current.pack()
r1_current.place(x=90, y=265)

# List two radio buttons
r2_past = Radiobutton(root, fg='blue', height=1, width=5, text="Past", font=("Source Code Pro", 8), variable=var, value=3, command=offline_view_two)
r2_past.pack()
r2_past.place(x=30, y=365)

r2_current = Radiobutton(root, fg='red', height=1, width=8, text="Current", font=("Source Code Pro", 8), variable=var, value=4, command=downloader_two)
r2_current.pack()
r2_current.place(x=90, y=365)

# List three radio buttons
r3_past = Radiobutton(root, fg='blue', height=1, width=5, text="Past", font=("Source Code Pro", 8), variable=var, value=5, command=offline_view_three)
r3_past.pack()
r3_past.place(x=30, y=465)

r3_current = Radiobutton(root, fg='red', height=1, width=8, text="Current", font=("Source Code Pro", 8), variable=var, value=6, command=downloader_three)
r3_current.pack()
r3_current.place(x=90, y=465)

# Export Button
export_button = Button(root, height=3, width=8, text="Export", font=("Source Code Pro", 8, 'bold'), command=exporter)
export_button.pack()
export_button.place(x=30, y=520)

# Updater Button
updater_button = Button(root, height=3, width=8, text="Update-All-Offline", font=("Source Code Pro", 8, 'bold'), command=html_update_all_offline)
updater_button.pack()
updater_button.config(wraplength=50)
updater_button.place(x=100, y=520)

# Save Button
save_button = Button(root, height=2, width=18, text="Save List", font=("Source Code Pro", 8, 'bold'), command=save_list)
save_button.pack()
save_button.config(wraplength=50)
save_button.place(x=30, y=580)

# Live View Canvas Setup
# Create canvas for live view
preview_canvas = Canvas(root, bg="white", height="360", width="575")
preview_canvas.pack()
preview_canvas.place(x=190, y=200)

###############################################################################
#                           HTML - Page Setup                                 #
###############################################################################
the_date_html = str('<h2>Sourced on date: '+str(the_date)+' </h2>')
# Define the html environment for the archive
# html template for generating the daily reports
html_template_one = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    img {
        max-width: 100%
        height: auto;
    }
    </style>
    <style>
    .content {
        max-width: 500px;
        margin: auto;
    }
    </style>
    <style>
    table, th, td {
            border: 1px solid black;
    }
    </style>
    <img src="https://steemitimages.com/DQmbtMuPBbA7PAWqurJh5ALHdH8V9je6k5RTir8hshjz6JL/icon.png" alt="MainLogo" width="600" height="300">
    <title>Just, Another, List</title>
    <h1>Page Generated Automatically - Powered by Python</h1>
    </head>
    <p>Author: Scott Jacob</p>
    <a href="https://coinmarketcap.com/gainers-losers/">Source: COIN MARKET GAINERS</a><br>
    <body bgcolor="#CEECF5">
    
    <table cellpadding="10"
    '''


# Setting an end html variable to marry the two parts together
# Idea is to call and write the first part of the html
# Append any regex values and statements generating the articles
# and then write the closing html to form the document

html_template_one_end = '''
    </table>
    </body>
    </html>
    '''

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#

html_template_two = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    img {
        max-width: 100%
        height: auto;
    }
    </style>
    <style>
    .content {
        max-width: 500px;
        margin: auto;
    }
    </style>
    <style>
    table, th, td {
            border: 1px solid black;
    }
    </style>
    <img src="http://www.mojwindows.sk/wp-content/uploads/2016/04/steam-logo_story.jpg" alt="MainLogo" width="760" height="400">
    <title>Just, Another, List</title>
    <h1>Page Generated Automatically - Powered by Python</h1>
    </head>
    <p>Author: Scott Jacob</p>
    <a href="https://store.steampowered.com/stats/">Source: Steam Stats</a><br>
    <body bgcolor="#E0ECF8">
    <table cellpadding="10"
    '''


# Setting an end html variable to marry the two parts together
# Idea is to call and write the first part of the html
# Append any regex values and statements generating the articles
# and then write the closing html to form the document

html_template_two_end = '''
    </table>
    </body>
    </html>
    '''

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_#

html_template_three = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    img {
        max-width: 100%
        height: auto;
    }
    </style>
    <style>
    .content {
        max-width: 500px;
        margin: auto;
    }
    </style>
    <style>
    table, th, td {
            border: 1px solid black;
    }
    </style>
    <img src="http://icons.iconarchive.com/icons/danleech/simple/1024/imdb-icon.png" alt="MainLogo" width="1000" height="500">
    <title>Just, Another, List</title>
    <h1>Page Generated Automatically - Powered by Python</h1>
    </head>
    <p>Author: Scott Jacob</p>
    <a href="https://www.imdb.com/chart/tvmeter/?sort=rk,asc&mode=simple&page=1"> Source: IMDBTV</a><br>
    <body>
    <table
    '''


# Setting an end html variable to marry the two parts together
# Idea is to call and write the first part of the html
# Append any regex values and statements generating the articles
# and then write the closing html to form the document

html_template_three_end = '''
    </table>
    </body>
    </html>
    '''


###############################################################################
#                           HTML - Generators                                 #
###############################################################################

''' These functions are identical in layout and function but contain different
parameters to generate html pages, the main being different regex for some pages
as there were multiple tables on the page '''

def html_generate_one_online():

    html_file = open('one_exported.html', 'w', encoding='UTF-8')
    html_file.write(str(html_template_one))

    new = [] # Initialise new list for regex
    generated_file = open('coinmarketcapnew'+str(the_date)+'.html', 'r', encoding='UTF-8')
    contents = generated_file.read() # read contents from previously downloaded html
    generated_file.close()
    
    new.append(findall('<table (.*?)</table>', contents, DOTALL)) # regex to find main table to display
    
    html_file.write(str(new[0][0])) # parse only single entry as findall uses one string
    #print(new) # test parsing output

    html_file.write(str(the_date_html))
    
    html_file.write(str(html_template_one_end)) # write end of file to complete the webpage
    html_file.close() # close up page to be opened in browser

    chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
    url = "one_exported.html" # set urlname to open
    #webopen(url) # open in default browser

    ''' Due to webbrowser.open being buggy on macos the workaround is to use .get()
    to specify an application to open it as the launchpad service which tkinter usually
    tries to use will not open it correctly.
    
    The platform.platform() function does not return macOS in the string as macOS is "not" the actual
    name of the OS, Darwin is, this is changed accordingly. However where macOS is seen previously it does
    work to change directory so go figure... '''
    current_os = platform.platform()
    print(current_os)    
    if "Windows" or "Linux" in current_os:
        webbrowser.open(url)
    else:
        print("Trying MacOS")

    if "Darwin" in current_os:
        webbrowser.get(chrome_path_mac).open(url)
    else:
        print("Open Failed")




def html_generate_one_offline():
    
    html_file = open('one_exported_offline.html', 'w', encoding='UTF-8')
    html_file.write(str(html_template_one))

    new = []
    generated_file = open('coinmarketcap.html', 'r', encoding='UTF-8')
    contents = generated_file.read()
    generated_file.close()
    
    new.append(findall('<table (.*?)</table>', contents, DOTALL))
    
    html_file.write(str(new[0][0])) # parse only single entry as findall uses one string
    #print(new) # test parsing output

    
    html_file.write(str(html_template_one_end)) # write end of file to complete the webpage
    html_file.close() # close up page to be opened in browser

    chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
    url = "one_exported_offline.html" # set urlname to open
    #webbrowser.get(chrome_path_mac).open(url) # open in default browser
    #webbrowser.open(url)

    ''' Due to webbrowser.open being buggy on macos the workaround is to use .get()
    to specify an application to open it as the launchpad service which tkinter usually
    tries to use will not open it correctly.
    
    The platform.platform() function does not return macOS in the string as macOS is "not" the actual
    name of the OS, Darwin is, this is changed accordingly. However where macOS is seen previously it does
    work to change directory so go figure... '''
    current_os = platform.platform()
    print(current_os)    
    if "Windows" or "Linux" in current_os:
        webbrowser.open(url)
    else:
        print("Trying MacOS")

    if "Darwin" in current_os:
        webbrowser.get(chrome_path_mac).open(url)
    else:
        print("Open Failed")



def html_generate_two_online():
    
    html_file = open('two_exported.html', 'w', encoding='UTF-8')
    html_file.write(str(html_template_two))

    new = []
    generated_file = open('steamstatsnew'+str(the_date)+'.html', 'r', encoding='UTF-8')
    contents = generated_file.read()
    generated_file.close()
    
    new.append(findall('<div id="detailStats">(.*?)</table>', contents, DOTALL))
    
    html_file.write(str(new[0][0])) # parse only single entry as findall uses one string
    #print(new) # test parsing output

    html_file.write(str(the_date_html))
    
    html_file.write(str(html_template_two_end)) # write end of file to complete the webpage
    html_file.close() # close up page to be opened in browser

    chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s' # Path to open chrome since webbrowser.open is buggy
    url = "two_exported.html" # set urlname to open
    #webopen(url) # open in default browser

    ''' Due to webbrowser.open being buggy on macos the workaround is to use .get()
    to specify an application to open it as the launchpad service which tkinter usually
    tries to use will not open it correctly.
    
    The platform.platform() function does not return macOS in the string as macOS is "not" the actual
    name of the OS, Darwin is, this is changed accordingly. However where macOS is seen previously it does
    work to change directory so go figure... '''
    current_os = platform.platform()
    print(current_os)    
    if "Windows" or "Linux" in current_os:
        webbrowser.open(url)
        print('Success!!')
    else:
        print("Trying MacOS")

    if "Darwin" in current_os:
        webbrowser.get(chrome_path_mac).open(url)
        print('Success!!')
    else:
        print("Open Failed")


def html_generate_two_offline():
    
    html_file = open('two_exported_offline.html', 'w', encoding='UTF-8')
    html_file.write(str(html_template_two))

    new = []
    generated_file = open('steamstats.html', 'r', encoding='UTF-8')
    contents = generated_file.read()
    generated_file.close()
    
    new.append(findall('<div id="detailStats">(.*?)</table>', contents, DOTALL))
    
    html_file.write(str(new[0][0])) # parse only single entry as findall uses one string
    #print(new) # test parsing output

    
    html_file.write(str(html_template_two_end)) # write end of file to complete the webpage
    html_file.close() # close up page to be opened in browser

    chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
    url = "two_exported_offline.html" # set urlname to open
    #webopen(url) # open in default browser

    ''' Due to webbrowser.open being buggy on macos the workaround is to use .get()
    to specify an application to open it as the launchpad service which tkinter usually
    tries to use will not open it correctly.
    
    The platform.platform() function does not return macOS in the string as macOS is "not" the actual
    name of the OS, Darwin is, this is changed accordingly. However where macOS is seen previously it does
    work to change directory so go figure... '''
    current_os = platform.platform()
    print(current_os)    
    if "Windows" or "Linux" in current_os:
        webbrowser.open(url)
        print('Success!!')
    else:
        print("Trying MacOS")

    if "Darwin" in current_os:
        webbrowser.get(chrome_path_mac).open(url)
        print('Success!!')
    else:
        print("Open Failed")



def html_generate_three_online():
    
    html_file = open('three_exported.html', 'w', encoding='UTF-8')
    html_file.write(str(html_template_three))

    new = []
    generated_file = open('imdbtvnew'+str(the_date)+'.html', 'r', encoding='UTF-8')
    contents = generated_file.read()
    generated_file.close()
    
    new.append(findall('<table (.*?)</table>', contents, DOTALL))
    
    html_file.write(str(new[0][0])) # parse only single entry as findall uses one string
    #print(new) # test parsing output

    html_file.write(str(the_date_html))
    
    html_file.write(str(html_template_three_end)) # write end of file to complete the webpage
    html_file.close() # close up page to be opened in browser

    chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
    url = "three_exported.html" # set urlname to open
    #webopen(url) # open in default browser

    ''' Due to webbrowser.open being buggy on macos the workaround is to use .get()
    to specify an application to open it as the launchpad service which tkinter usually
    tries to use will not open it correctly.
    
    The platform.platform() function does not return macOS in the string as macOS is "not" the actual
    name of the OS, Darwin is, this is changed accordingly. However where macOS is seen previously it does
    work to change directory so go figure... '''
    current_os = platform.platform()
    print(current_os)    
    if "Windows" or "Linux" in current_os:
        webbrowser.open(url)
        print('Success!!')
    else:
        print("Trying MacOS")

    if "Darwin" in current_os:
        webbrowser.get(chrome_path_mac).open(url)
        print('Success!!')
    else:
        print("Open Failed")    


def html_generate_three_offline():
    
    html_file = open('three_exported_offline.html', 'w', encoding='UTF-8')
    html_file.write(str(html_template_three))

    new = []
    generated_file = open('imdbtv.html', 'r', encoding='UTF-8')
    contents = generated_file.read()
    generated_file.close()
    
    new.append(findall('<table (.*?)</table>', contents, DOTALL))
    
    html_file.write(str(new[0][0])) # parse only single entry as findall uses one string
    #print(new) # test parsing output

    
    html_file.write(str(html_template_three_end)) # write end of file to complete the webpage
    html_file.close() # close up page to be opened in browser

    chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
    url = "three_exported_offline.html" # set urlname to open
    #webopen(url) # open in default browser

    ''' Due to webbrowser.open being buggy on macos the workaround is to use .get()
    to specify an application to open it as the launchpad service which tkinter usually
    tries to use will not open it correctly.
    
    The platform.platform() function does not return macOS in the string as macOS is "not" the actual
    name of the OS, Darwin is, this is changed accordingly. However where macOS is seen previously it does
    work to change directory so go figure... '''
    current_os = platform.platform()
    print(current_os)    
    if "Windows" or "Linux" in current_os:
        webbrowser.open(url)
        print('Success!!')
    else:
        print("Trying MacOS")

    if "Darwin" in current_os:
        webbrowser.get(chrome_path_mac).open(url)
        print('Success!!')
    else:
        print("Open Failed")


###############################################################################
#                               MainLoop                                      #
###############################################################################

# Call Loop #
root.geometry("800x650") # Set window size
root.mainloop() # Call mainloop
