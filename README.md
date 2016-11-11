![hw-logo](http://cs.wubook.net/hc/en-us/article_attachments/201676001/Horizontal-logo-Orange.png)CHALLENGE

The challenge proposed by Hostelworld is to build a recommendation engine for users. Recommendations can save travelers valuable time, improve their hostel experience, and increase user retention. This challenge will use user information, reviews, and hostel details.

Hostelworld currently lets users apply filters to their search. However, hostels with the same features and price range can still be very different. This is why hostelworld is proposing the challenge of building a recommendation engine that also takes into account review text and hostel descriptions.

[Register here to access the anonymized data set](https://ti.to/hackathon-conference/travel-meets-big-data/)

![meet-the-world](http://www.hirum.com.au/wp-content/uploads/2015/11/meet-the-world.png)

## Details
Your solution should be able to recommend hostels for a given user, and give numeric values for the recommendations. The recommendation values should relate to what a user would leave as a review score if they stayed at that hostel. Your solution should be able to give a recommendation score for any hostel user combination.

The data will include
-	User Information
-	User Reviews 
-	Hostel Details 

The final testing data set is a set of user reviews where we have withheld the scores. You will submit the following dataframes with you model:
- A dataframe including user and hostel ids from the final testing data reviews with your predicted review score.
- A dataframe containing user ids from the final testing data set with the hostel your model recommends highest for them and the recommendation score for that hostel. 

Your submission will be graded by 
- Summing up the difference between your predicted review scores and the actual review scores of the testing data set
- Comparing your recommendation hostel scores to your  predicted scores of the testing data 
- Overall construction of your recomendation engine  

## Questions?
 Please email your questions about the challenge to hwchallenge2016@entanon.com.
 
 [View project the challenge is based on for background.](https://caitlinmowdy.github.io/)
