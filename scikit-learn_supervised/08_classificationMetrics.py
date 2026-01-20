'''
accurace = correct_pred/total_pred
precision = 
recall = 
F1 score = smart balance between precision and recall
'''

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# True Answers (what acturally happend/ correct answers)
y_true = [1,0,1,1,0,1,0]

# Model's prediction
y_pred = [1,0,1,0,0,1,1]

print("Accuracy: ", accuracy_score(y_true, y_pred))
print("Precision: ", precision_score(y_true, y_pred))
print("Recall Score: ", recall_score(y_true, y_pred))
print("F1 Score: ", f1_score(y_true, y_pred))