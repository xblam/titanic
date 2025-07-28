# titanic
trying out different types of classification algorithms on the titanic dataset

ISSUES WITH DATA
* missing values for age, cabin (LOTS), embarked
* 38% survival
* cheapest fare is 0, highest is 512 might have to log it later
* distribution of fare is probably highly skewed.



USEFUL FEATURES
* put survived into categorical
* class in categorical
* cabin has many missing values
* embarked should be one hot encoded
* crapton of different cabins and tickets, even though most of the cabin values are 
missing
* shitton of differen cabins and shitton of different tickets


TECHNIQUES:
* info
* describe
* shape
* df.duplicated().sum()
*df[].nunique()
* df[].value_counts()
* df[].isnull().sum()
* df[].dropna()
* df[['col1', 'col2']]
* df.select_dtype(include=['int64'])
* df[df['col1']==0]
* plt.hist(df['col'], bins=df['col'].nunique())
* df[].value_counts().plot(kind='bar')
* pd.pivot(df, index='rows', columns='cols', values='val', aggfunc=['func'])
* df = df.copy()
* df[] = pd.to_numeric(df[])
* df = df.rename(columns={'col1': 'col1'})
* df.loc[df.duplicated(subset=['colname'])]
* ~df.query('colname' == 'setname')
* df.reset_index(drop=True)
* backslashes to break up lines

# Understanding the data
* make sure data is loaded in properly
* make sure I understand what each column means
* make sure the data types are what I expect them to be
* get some quick insights in the ditribution of numerical data

# Cleaning the data
* drop the rows that we do not need/have too many missing values
* rename the columns as needed
* check for missing values
* check for duplicated rows/only keep first of the duplicated rows
* check for fault values

# Feature underestanding
* 



accuracy

precision - out of all labeled positives how many were real positives

recall - out of all real positives how many were labeled

use these two together

explain how thresholds relate to the models and other metrics - when I make and evaluate
 a model, I should use predict probas to tweak and assess the performance of the model, 
 since this is an easier number to minizer (not really binary). On the other hand, when 
 i am actually trying to get answers out of the models it will have to go through a 
 trheshold to get the binary answer. In most cases, the model will be built in such a 
 way that the threshold of 0.5 will give the best answer. However, this is still 
 something that I can change based on requiements, even though in theory it will always 
 mean that the accuracy of my model will be going down.


multi class - average these values across classes
- can weight the results

f1 score - precision and recall toghether - use with other methods

how do i use these features if there are multiple classes?

the metrics and the curves give a better understanding of the types of errors the model 
is making, and what the tradeoffs are at each threshold level

when evaluating a model we should evaluate it on the raw performance, so make sure that 
we run predict_proba on the models that just output the binary categories

Control shift G to do to git diff mode to see what changes were made in between versions

control shift e to go back to explorer view

how do we handle class imbalances?


how does gridsearch differ between different types of models?

when should i use grid searcha nd when should i use random search?

what does the roc-auc curve and PR curves say about what i should do to imporve my models?

what is threshold tuning and where do i change it on the models creation pipeline?

what is lightgmb and catboost?

what does model calibration mean

what is cross validation? is it k-fold validation or is it just normal validation

what is ridge regression and what is lasso regression

what toher forms of vector embeddings are there, when do i use them?

what are interaction items, and how do i go about chosing which feautres to use them with 



# PANDAS
practice['']
practice('')


