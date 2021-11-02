from django.db import models


class WebsiteInfo(models.Model):
    heading = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000)
    physical_address = models.CharField(max_length=1000, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to="images/logo", null=True, blank=True)
    youtube_video_url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "Website Information"
        verbose_name_plural = "Website Information"


class Package(models.Model):
    package_name = models.CharField(max_length=200)
    price = models.IntegerField()
    duration = models.CharField(max_length=100)
    feature_1 = models.CharField(max_length=200)
    feature_2 = models.CharField(max_length=200)
    feature_3 = models.CharField(max_length=200)
    feature_4 = models.CharField(max_length=200, null=True, blank=True)
    feature_5 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.package_name

    class Meta:
        verbose_name = "Packages"
        verbose_name_plural = "Packages"


class ExamPart1(models.Model):
    question = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to="images/question/")
    option_1 = models.CharField(max_length=500)
    option_2 = models.CharField(max_length=500)
    option_3 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Exam Part 1"
        verbose_name_plural = "Exam Part 1"


class ExamPart2(models.Model):
    question = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to="images/question/")
    option_1 = models.CharField(max_length=500)
    option_2 = models.CharField(max_length=500)
    option_3 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Exam Part 2"
        verbose_name_plural = "Exam Part 2"


class ExamPart3(models.Model):
    question = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to="images/question/")
    option_1 = models.CharField(max_length=500)
    option_2 = models.CharField(max_length=500)
    option_3 = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Exam Part 3"
        verbose_name_plural = "Exam Part 3"
