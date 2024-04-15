from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    is_ready_to_publish = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self) -> str:
        return str(self.title)  # Convert title to string representation


class Meta:
    verbose_name_plural = "quizzes"


class Question(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey(
        Quiz, related_name="questions", on_delete=models.CASCADE)

    def __str__(self) -> str:
        # Convert question_text to string representation
        return str(self.text)


class Choice(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(
        Quiz, related_name="choices", on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    question = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE)

    def __str__(self) -> str:
        # Convert choice_text to string representation
        return str(self.text)


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    quizes = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    objects = models.Manager()


def __str__(self) -> str:
    # Convert user_response to string representation
    return f"{self.user.username}'s response to {self.question.text} in {self.quizes.title} is {self.choice.text}"


def calculate_score(self):
    total_score = sum(choice.socore for choice in self.choices.all())
    return total_score
