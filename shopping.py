import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    evidence = []
    labels = []
    with open(filename, mode ='r')as file:
        csvFile = csv.reader(file)
        next(csvFile)
        print(type(csvFile))
        for line in csvFile:
            ev = []
            ev.append(int(line[0]))
            ev.append(float(line[1]))
            ev.append(int(line[2]))
            ev.append(float(line[3]))
            ev.append(int(line[4]))
            ev.append(float(line[5]))
            ev.append(float(line[6]))
            ev.append(float(line[7]))
            ev.append(float(line[8]))
            ev.append(float(line[9]))
            month = 0 if line[10] == "Jan" else 1 if line[10] == "Feb" else 2 if line[10] == "Mar" else 3 if line[10] == "Apr" else 4 if line[10] == "May" else 5 if line[10] == "June" else 6 if line[10] == "Jul" else 7 if line[10] == "Aug" else 8 if line[10] == "Sep" else 9 if line[10] == "Oct" else 10 if line[10] == "Nov" else 11 if line[10] == "Dec" else 100
            ev.append(month)
            ev.append(int(line[11]))
            ev.append(int(line[12]))
            ev.append(int(line[13]))
            ev.append(int(line[14]))
            ev.append(0 if line[15] == "New_Visitor" else 1)
            ev.append(0 if line[16] == "FALSE" else 1)  
            evidence.append(ev)
            labels.append(0 if line[17] == "FALSE" else 1)
    return (evidence, labels)



def train_model(evidence, labels):

    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence,labels)
    return model


def evaluate(labels, predictions):
    sumSensivity = 0
    countSensivity = 0
    sumSpecificity = 0
    countSpecificity = 0
    for index in range(len(predictions)):
        if labels[index] == 1:
            countSensivity += 1
            if predictions[index] == 1:
                sumSensivity += 1
        if labels[index] == 0:
            countSpecificity += 1
            if predictions[index] == 0:
                sumSpecificity += 1
    
    return (float(sumSensivity/countSensivity), float(sumSpecificity/countSpecificity))


if __name__ == "__main__":
    main()
