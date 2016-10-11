# flink

##Technical

The entire project was built by myself in 2 weeks. The technologies used are Python, Angular, Material Design, and PosgreSQL. The website communicates with Google API for several reasons including user validation, connecting with friends' lists, and calendar information.


##The Project  
 
Flink is a straight forward web application which will help you connect better with all of your friends in your personal and professional lives. Flink aims to eliminate one of the most annoying yet real hurdles when it comes to meeting with friends or work related partners.  
 
For the times that you passed by your friend and agreed to get coffee at some point, but never did…  
For the times when you didn’t want to ask people to meet because you don’t have similar schedules or jobs… 
For all the times when meeting with friends didn’t have to be as hard as it was supposed to, enter Flink! The application which will take care of all the hassle. So all you have to do is push one button! 
 
The landing page is simple and has instructions for how to use the app, and explains the necessity of logging in through Google. In further development of this application, I would like to integrate with not only Google, but as will be discussed further, other platforms as well. 
 
*Note: certain pages have duplicate images to demonstrate the responsiveness 

<img width="1440" alt="screen shot 2016-10-05 at 12 02 20 pm" src="https://cloud.githubusercontent.com/assets/16547215/19266174/2959f724-8f5d-11e6-8b1a-c18979e556e8.png">


![screen shot 2016-10-10 at 9 37 40 pm](https://cloud.githubusercontent.com/assets/16547215/19266311/d9478656-8f5d-11e6-94d6-83a0ac5b4b45.png)

Once you register/sign in, you are brought to the home page of the app, which also is designed to be as simple as possible. The idea is that users will likely want to perform the task of sending an invite as quickly as possible. Thus, the full path from initial landing to successfully completing one of two possible tasks (invite or response) must be as short as possible. There will be a variety of ways to reach certain pages through which messaging is done. The first and easiest of these ways is through the main dashboard. This screen will give a summary of our current invitations, appointments, and other reminders.  
 
You may choose to follow the suggested links, or select one of the standard NavBar items. The "About Us" page brings you to a page similar to the landing page with information about myself and the app. 

<img width="1440" alt="screen shot 2016-10-05 at 12 08 45 am" src="https://cloud.githubusercontent.com/assets/16547215/19266173/2957b61c-8f5d-11e6-8bdd-9b1a48c863cb.png">

The "Friends" tab opens a simple page which lists all your Google contacts; I currently have very few, and they are all listed here. In further development of this application, I would like to integrate with not only Google contacts, but also Facebook, LinkedIn, etc. The two sections are for friends that already do and do not have Flink, respectively. From there, you can choose to send them a message and whatever other action may be integrated in the future.  

<img width="1440" alt="screen shot 2016-10-10 at 8 48 19 pm" src="https://cloud.githubusercontent.com/assets/16547215/19266213/4c7283a2-8f5d-11e6-89d7-7a661c1db6f2.png">

![screen shot 2016-10-10 at 9 40 16 pm](https://cloud.githubusercontent.com/assets/16547215/19266242/700a8210-8f5d-11e6-972a-0a3c6eeb2821.png)

This is one of the few ways to send a message. The other two are either through the homepage dashboard or directly through the "Messages" tab. Here, you have an inbox and outbox with a responsive sidenav. 
Upon sending an invitation to meet, Flink synchronizes the calendars of the parties involved to see when the best time to meet is, or if there is such a time at all. This is done through a simple messaging screen that can contains as much detail and additional content as desired through further development. In it's most basic form, this messaging board hold all the incoming and outgoing invitations, with detail regarding whether the appointment is set, when it is scheduled, what the occasion is (currently coffee), and a short message. 

<img width="1440" alt="screen shot 2016-10-05 at 12 09 08 am" src="https://cloud.githubusercontent.com/assets/16547215/19266175/295af368-8f5d-11e6-99cb-6d793db732f7.png">

![screen shot 2016-10-10 at 10 19 23 pm](https://cloud.githubusercontent.com/assets/16547215/19266276/a3c7b6b8-8f5d-11e6-890e-c73e786f8fea.png)

To send a new message from this screen you click on the "New Message." On this page, you select who you are sending the message to (this info is auto-filled if you get to this page through the "Friends" page), you select the occasion, write a brief message, and select the details of when you'd like to meet. You can leave this information blank or fill it out with maximum detail.  

![screen shot 2016-10-10 at 10 45 51 pm](https://cloud.githubusercontent.com/assets/16547215/19266274/a3bb455e-8f5d-11e6-9900-a4d7baadd860.png)

Finally, once an appointment is set in the application, it also gets saved to your Google calendar. Again, rather than using only Google, ideally, the application would allow to sync with multiple calendar applications. The appointments you set can be seen in the "Calendars" page, which will import info from the calendar(s) you specify (currently only main calendar in Google).  

<img width="1440" alt="screen shot 2016-10-10 at 8 48 27 pm" src="https://cloud.githubusercontent.com/assets/16547215/19266211/4c70e1b4-8f5d-11e6-9b30-8bbd5c3b35d1.png">

In the end, you are able to keep track of your appointments either through Flink itself, or simply use it as the booking agent, and follow up on your main calendar. Happy Flinking! 
