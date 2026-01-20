import matplotlib.pyplot as plt

'''
plt.scattr(x,y, color = "color_name", marker = "*", label="Label")
'''

hours_studies = [1,2,3,4,5,6,7,8]
exam_scores = [50,55,60,65,70,75,80,85]

plt.scatter(hours_studies, exam_scores, marker = "*", color = "blue", label = "study pattern")
plt.show()
