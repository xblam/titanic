# chose the columns that we want to keep
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


# first we change sex into binary
train['Sex'] = train['Sex'].map({'male':1, 'female':0})

# only grab features that I want
train = train[[ 'Survived', 'Class',  'Sex', 'Age', 'SibSp', 'Parch',
    'Fare', 'Embarked']]
train['Embarked'] = train['Embarked'].astype('category')

train.head()

df_numeric = pd.get_dummies(train, columns=['Class', 'Embarked', ], drop_first=True).copy()