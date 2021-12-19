'''
Consider a quiz game where a person is given two questions and must decide which question to answer first. Question 1 will be answered correctly with probability 0.8, 
and the person will then receive as prize $100, while question 2 will be answered correctly with probability 0.5, and the person will then receive as prize $200. 
If the first question attempted is answered incorrectly, the quiz terminates, i.e., the person is not allowed to attempt the second question. 
If the first question is answered correctly, the person is allowed to attempt the second question. 
Which question should be answered first to maximize the expected value of the total prize money received?
'''

def maximize_prize(p1, p2):
  #If Question 1 is answered first
  p1_100 = p1*(1-p2) #question 1 correct, question 2 incorrect
  p1_300 = p1*p2 #question 1 & 2 correct
  mean_q1 = (p1_100*100) + (p1_300*300)
  
  #If Question 2 is answered first
  p2_200 = p2*(1-p1) #question 2 correct, question 1 incorrect
  p2_300 = p2*p1 #question 1 & 2 correct
  mean_q2 = (p2_200*200) + (p2_300*300)
  
  return f'Q1: {mean_q1}' if mean_q1 > mean_q2 else f'Q2: {mean_q2}'
