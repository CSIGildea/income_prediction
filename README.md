# Income Prediction for CSU44061 

Competition Link: https://www.kaggle.com/c/tcdml1920-income-ind/

Finished in top 1%...somehow :muscle: :muscle: :muscle:

# Install
1.virtualenv env

2.source env/bin/activate

3.pip install -r requirements.txt


# What I did, learnt and thoughts
I didn't have that much ML background going into this competition. Had compeleted a course on anaconda libraries which definitely helped. My solution finished 2nd (excluding test submission made by lecturer - Professor Beel) out of 302 total submissions participants, on the complete leaderboard. In public leaderboard it was 19th before the private test data was released on the other 70% of data.

Resources I recommend:
- Lectures were really good baseline
- [The Hundred-Page Machine Learning Book displays topics really well in a short amount of time (would recommend buying, it is worth it - Is available on read now buy later principle too).](http://themlbook.com/)
- [Did part of a udemy course (can like half recommend - is a good starting place)](https://www.udemy.com/course/machinelearning/)
- Stackoverflow all the things...


## Special tricks to make a model useful
### Graph all the things and feature selection
Graphing each variable with respect to the income was extremely informative. Along with viewing with pearson coefficients and a bit of backward elimination really helped see what features mattered. I ran backwards elimination on code without professions and countries added at one stage (I treated these as dummy variables and those made the col size be 1400+), this running backwards elimination on this was too much and just overfit the data.

### Questioning the data
I spent SO long trying to figure out how to make a reasonable guess for job titles not present in test data, I even had a super hacky measure at one put to measure the length of a job title in characters and use that as an input to the ML model, the logic was that:

"Chief Executive Officer" - Paid a big salary

"Teacher" - Not as big as CEO (sidenote: really underpaid for the impact their work has)


BUT this was kinda useless as it turns out the job titles had been assigned a totally random salary each. In fairness my total fault not researching this more beforehand, I should have questioned the data earlier.

### Rich People in Small Cities
From graphing this is super clear. Rich people had a tendency to live in cities with less than 3000 population, this was really really clear in the data which made it look intentional. Make a boolean if a size of city size is less than 3000. Then get rid of size of cities as seems totally useless. Yet again this was a synthetic dataset feature, I'm not sure how realistic it is.

### Adjusting Income Scale
If you log the income value it dramatically helped the outcome, then exp() the prediction before saving to CSV. I wish I had paid attention to this earlier as spent soooo soo soo long in the 78-80k range.

### Data Preprocessing is super powerful
I was running XGBoost for so long absolutely killing my beefy laptop but ultimately having well processed data trumps all. Final submitted solution was totally basic scikit learn lin reg took 15-20 secs to run in comparison to 20-30 minutes on my laptop for XGBoost which ended up giving a worst result - Note this is likely the fault of me the inexperienced machine learning developer, I'm certain an XGBoost made program could perform even better.

## Given extra time what would I have done
I totally disregarded any rows of data missing important features from my training data, I really wanted to use an IterativeImputer (basically a model to run on the training data to predict missing values based on the other training data). Sadly was time constraint and felt basic editing of the data would have a bigger impact than adding this feature, but was super cool to learn and read about for the future. Ultimately happy with this decision given the timeframe.
