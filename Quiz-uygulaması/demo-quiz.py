#question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
        return self.answer == answer 


#Quiz

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print('-' + q)

        answer = input("cevap : ")
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

       
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
             self.displayProgress()
             self.displayQuestion()

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("quiz bitti")
        else:
            print(f"question {questionNumber} of {totalQuestion}".center(100, "*"))

    def showScore(self):
        print('score : ', self.score)

q1 = Question("en iyi programlama dili hangisidir ?", ['C#',"python", "javascript","C"], "python")
q2 = Question("en zor dil hangisidir ?", ['C#',"python", "javascript","C"], "C")
q3 = Question("frontend kısmında hangi dil kullanılır ?", ['C#',"python", "javascript","C"], "javascript")
questions = [q1,q2,q3]

quiz = Quiz(questions)
question = quiz.getQuestion()
quiz.loadQuestion()


