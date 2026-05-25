import pandas as pd;
import matplotlib.pyplot as lib;
import seaborn as sb;

iris_data=sb.load_dataset('iris');
print(type(iris_data));               
print(iris_data.head());      #return top 5 rows
print(iris_data.shape);       #structure and size of dataset
print(iris_data.columns);
print(iris_data.info());
print(iris_data.describe())


# scatterplot
sb.scatterplot(data=iris_data,
               x='petal_length',
               y='petal_width',
               hue='species')

#add title and labels
lib.title('petal length vs petal width of iris species')
lib.xlabel('petal length(cm)')
lib.ylabel('petal width(cm)')
lib.show()

sb.scatterplot(data=iris_data,
               x='sepal_length',
               y='sepal_width',
               hue='species')
lib.title('sepal length vssepal width')
lib.xlabel('sepal length(cm)')
lib.ylabel('sepal width(cm)')
lib .show()

sb.scatterplot(data=iris_data,
               x='sepal_length',
               y='petal_length',
               hue='species')
lib.title('sepal length vs petal length')
lib.xlabel('sepal length(cm)')
lib.ylabel('petal length(cm)')
lib.show()

#histogram visualization (A histogram is a bar chart that shows how often different values appear in your data)
lib.hist(data=iris_data, x='petal_length', bins=15, color='green', edgecolor='black')
lib.title('Distribution of petal length in iris flowers')
lib.xlabel('petal length(cm)')
lib.ylabel('Frequency(number of flowers)')
lib.show()

#box plot 
sb.boxplot(data=iris_data,x='species',y='petal_length')
lib.title('Box Plot: Petal Length Distribution by Iris Species')
lib.xlabel('Iris Species')
lib.ylabel('Petal Length (cm)')
lib.show()