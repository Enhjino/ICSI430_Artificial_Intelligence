from dep import *

spam, ham = init()

spams = classify(spam, ham, "./spam_data/dev/spam/")
hams = classify(spam, ham, "./spam_data/dev/ham/")

del spam
del ham

confusion = [
    ["", "Predicted Ham", "Predicted Spam"],
    ["Actual Ham", hams[0] - hams[1], hams[1]],
    ["Actual Spam", spams[0] - spams[1],  spams[1]]
]

print("---------------------REPORT--------------------------")

line = "+-----------------+-----------------+-----------------+"

print("Confusion Matrix")
for row in confusion:
    print("| {:<15} | {:<15} | {:<15} |".format(*row))
print(line)

TP = spams[1]                   # spam mails classified spam
FP = hams[1]                    # spam mails classified ham
TN = hams[0] - hams[1]          # ham mails classified spam
FN = spams[0] - spams[1]        # ham mails classified ham

print("     TP      TN      FP      FN      ")
print("     ---     ---     ---     ---     ")
print(f"     {TP}     {TN}     {FP}      {FN}      ")
print(line)

print("Classification Measure\n")
accuracy = (TP + TN) / (TP + TN + FP + FN)
print(f"Accuracy: {accuracy:.2%}")

precision = TP / (TP + FP) if (TP + FP) > 0 else 0
print(f"Precision: {precision:.2%}")

recall = TP / (TP + FN) if (TP + FN) > 0 else 0
print(f"Recall: {recall:.2%}")


f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0  # Avoid division by zero
print(f"F1 Score: {f1_score:.2%}")


false_alarm = FP / (TN + FP) if (TN + FP) > 0 else 0
print(f"False alarm rate: {false_alarm:.2%}")


missed_detection = FN / (TN + FN) if (TN + FN) > 0 else 0
print(f"Missed detection rate: {missed_detection:.2%}")
