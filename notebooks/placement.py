# can choose which columns to keep or drop
train = train[[
    'PassengerId', 
    'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
    'Parch', 'Ticket', 'Fare', 
    # 'Cabin', 
    'Embarked']].copy()

# rename the columns
train = train.rename(columns={
    'PassengerId': 'Id',
    'Pclass': 'Class'})

train = train.drop(columns=['AgeGroup', 'Title'])