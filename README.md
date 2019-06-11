<p align="center">
  status of this github repo: <b>incomplete</b> <br/>
  (will update status when complete)
</p>

<h2 align="center">STAT 418: Final Project</h1> 
<h3 align= "center">Reddit Data Analysis</h3> 
<p> <b>Background</b> </br>
In Reddit’s 2017 transparency report,  a list of 944 accounts suspected to have originated from the Russian Internet Research Agency (IRA). The agency has employed fake accounts to register on major social networking sites to influence the 2016 United States presidential elections. More than 1000 employees are reportedly worked in a single building of the agency in 2015. </br>

<b>Exploratory Data Analysis</b> </br>
First I looked at the top 10 subreddits that the Russiana accounts were posting in.

<p align="center"><img src="figures/top10subreddit.png" alt="drawing" width="800"/></p>

I choose to collect submissions from the subreddit Bad_Cop_No_Donut from Janurary 1, 2016 to December 31, 2016. My dataset had 12,272 submissions total (11,688 from normal accounts and 584 from Russian accounts). Approximately 4.4% of the submissions were made by suspect accounts. 

Then I looked at the top 20 most frequently used words by Russian and normal accounts.

<p align="center"><img src="figures/top20words.png" alt="drawing" width="550" /></p> 

The top 4 words in both lists (i.e. police, cop, man, officer) are the same. Also, the 5th most frequently, "black", used word in the Russian user list is the 17th most frequently used word in the normal user list.</br>

I also compared the number of submissions per week and the number of submissions at each hour of the day for Russian and normal users.
<p align="center"><img src="figures/Hourly.png" alt="drawing" width="750"/></p>
<p align="center"><img src="figures/Weekly.png" alt="drawing" width="750"/></p>

<b>Data Collection</b> </br>
I used PushShift.io to collect submission ids from the subreddit Bad_Cop_No_Donut . With the collected submission ids I used PRAW to get:
* **id**: submission id
* **author**: submission’s author
* **created_utc**: the Unix time the submission was created
* **is_self**: whether or not the submission is a selfpost (a post you’ve created on reddit, meaning it doesn't link outside of reddit, aka 'text post’)
* **name**: fullname of the submission (same as id but preceded by "t3_")
* **selftext**: submission’s selftext
* **title**: submission's title
* **url**: the URL the submission links to, or the permalink if a self post
</br>

<b>Preprocessing Text</b> </br>
For each submission title, I removed stop words and punctuation, converted all words to lower case and lemmatized and tokenized each word. </br>

<b>Text Frequency - Inverse Document Frequency (TF-IDF)</b> </br>
<b>PCA</b> </br>
<b>Model Selection</b> </br>
<b>Cross Validation</b></br></p>

<!-- + ![](figures/top10subreddit.png)
<p align="center">
  status of this github repo: <b>incomplete</b> <br/>
  (will update status when complete)
</p> + -->
<img src="figures/screePlot.png" alt="drawing" width="850"/>

http://52.27.3.193:8050/
