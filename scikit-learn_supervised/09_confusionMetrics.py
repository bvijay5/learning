'''
                Act_pass  Act_Fail
Predict Pass    [TN      |      FP]
Predict Pass    [FN      |      TP]

-> True Postive(TP)
        M = Pass
        S = Pass
        Correct Guess(CG)

-> TN
        M = Fail
        S = Fail
        (CG)
-> False Positive(FP)
        M = Pass
        S = Fail
        Wrong Guess(WG)

-> FN
        M = Fail
        s = Pass
        (WG)
'''

from sklearn.metrics import confusion_matrix

y_true = [1,0,1,1,0,1,0,0,1,0]
y_predict = [1,0,1,0,0,1,1,0,1,0]

cm = confusion_matrix(y_true, y_predict)
print(cm)
