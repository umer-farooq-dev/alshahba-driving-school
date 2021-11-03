from django.shortcuts import render, redirect

from wsite.models import WebsiteInfo, Package, ExamPart1, ExamPart2, ExamPart3


def index(request):
    site_info = WebsiteInfo.objects.first()
    packages = Package.objects.all()
    context = {
        "site_info": site_info,
        "packages": packages,
    }
    return render(request, template_name="wsite/index.html", context=context)


def trial_exam_starter(request):
    return render(request, template_name="wsite/trial-starter.html")


def trial_exam(request):
    return render(request, template_name="quiz/quiz.html")


def dashboard(request):
    return render(request, template_name="wsite/admin/dashboard.html")


def site_info(request):
    web_info = WebsiteInfo.objects.first()
    if request.method == "POST":
        web_info.heading = request.POST.get("heading")
        web_info.description = request.POST.get("description")
        web_info.physical_address = request.POST.get("physical_address")
        web_info.email_address = request.POST.get("email_address")
        web_info.phone_number = request.POST.get("phone_number")
        web_info.introduction = request.Post.get("introduction")
        web_info.introduction_description = request.Post.get("introduction_description")
        web_info.logo = request.FILES["logo"]
        web_info.youtube_video_url = request.POST.get("youtube_video_url")
        web_info.save()

    context = {
        "web_info": web_info
    }
    return render(request, template_name="wsite/admin/site-info.html", context=context)


def packages(request):
    package = Package.objects.all()
    context = {
        "packages": package
    }
    return render(request, template_name="wsite/admin/packages.html", context=context)


def update_package(request, package_id):
    package = ""
    all_package = Package.objects.all()
    try:
        package = Package.objects.get(id=package_id)
        if request.method == "POST":
            package.package_name = request.POST.get("package_name")
            package.price = request.POST.get("price")
            package.duration = request.POST.get("duration")
            package.feature_1 = request.POST.get("feature_1")
            package.feature_2 = request.POST.get("feature_2")
            package.feature_3 = request.POST.get("feature_3")
            package.feature_4 = request.POST.get("feature_4")
            package.feature_5 = request.POST.get("feature_5")
            package.save()
            return redirect('packages')
    except:
        print("error")

    context = {
        "package": package,
        "packages": all_package,
    }
    return render(request, template_name="wsite/admin/packages.html", context=context)


def add_question_part_1(request):
    questions = ExamPart1.objects.all()
    if request.method == "POST":
        part_1 = ExamPart1.objects.create(
            question=request.POST.get("question"),
            picture=request.FILES["picture"],
            option_1=request.POST.get("option_1"),
            option_2=request.POST.get("option_2"),
            option_3=request.POST.get("option_3"),
            correct_answer=request.POST.get("correct_answer"),
        )
        part_1.save()

    context = {
        "questions": questions,
        "part": 1
    }
    return render(request, template_name="wsite/admin/exam-add-questions.html", context=context)


def update_question_part_1(request, q_id):
    questions = ExamPart1.objects.all()
    edit_question = ""

    try:
        edit_question = ExamPart1.objects.get(id=q_id)
        if request.method == "POST":
            edit_question.question = request.POST.get("question")
            edit_question.picture = request.FILES["picture"]
            edit_question.option_1 = request.POST.get("option_1")
            edit_question.option_2 = request.POST.get("option_2")
            edit_question.option_3 = request.POST.get("option_3")
            edit_question.correct_answer = request.POST.get("correct_answer")

            edit_question.save()
            return redirect('questions_part_1')
    except:
        print("question not found")

    context = {
        "questions": questions,
        "edit_question": edit_question,
        "part": 1
    }
    return render(request, template_name="wsite/admin/exam-add-questions.html", context=context)


def add_question_part_2(request):
    questions = ExamPart2.objects.all()
    if request.method == "POST":
        part_2 = ExamPart2.objects.create(
            question=request.POST.get("question"),
            picture=request.FILES["picture"],
            option_1=request.POST.get("option_1"),
            option_2=request.POST.get("option_2"),
            option_3=request.POST.get("option_3"),
            correct_answer=request.POST.get("correct_answer"),
        )
        part_2.save()

    context = {
        "questions": questions,
        "part": 2
    }
    return render(request, template_name="wsite/admin/exam-add-questions.html", context=context)


def update_question_part_2(request, q_id):
    questions = ExamPart2.objects.all()
    edit_question = ""

    try:
        edit_question = ExamPart2.objects.get(id=q_id)
        if request.method == "POST":
            edit_question.question = request.POST.get("question")
            edit_question.picture = request.FILES["picture"]
            edit_question.option_1 = request.POST.get("option_1")
            edit_question.option_2 = request.POST.get("option_2")
            edit_question.option_3 = request.POST.get("option_3")
            edit_question.correct_answer = request.POST.get("correct_answer")

            edit_question.save()
            return redirect('questions_part_2')

    except:
        print("question not found")

    context = {
        "questions": questions,
        "edit_question": edit_question,
        "part": 2
    }
    return render(request, template_name="wsite/admin/exam-add-questions.html", context=context)


def add_question_part_3(request):
    questions = ExamPart3.objects.all()
    if request.method == "POST":
        part_3 = ExamPart3.objects.create(
            question=request.POST.get("question"),
            picture=request.FILES["picture"],
            option_1=request.POST.get("option_1"),
            option_2=request.POST.get("option_2"),
            option_3=request.POST.get("option_3"),
            correct_answer=request.POST.get("correct_answer"),
        )
        part_3.save()
    print(questions)
    context = {
        "questions": questions,
        "part": 3
    }
    return render(request, template_name="wsite/admin/exam-add-questions.html", context=context)


def update_question_part_3(request, q_id):
    questions = ExamPart3.objects.all()
    edit_question = ""

    try:
        edit_question = ExamPart3.objects.get(id=q_id)
        if request.method == "POST":
            edit_question.question = request.POST.get("question")
            edit_question.picture = request.FILES["picture"]
            edit_question.option_1 = request.POST.get("option_1")
            edit_question.option_2 = request.POST.get("option_2")
            edit_question.option_3 = request.POST.get("option_3")
            edit_question.correct_answer = request.POST.get("correct_answer")

            edit_question.save()
            return redirect('questions_part_3')

    except:
        print("question not found")

    context = {
        "questions": questions,
        "edit_question": edit_question,
        "part": 3
    }
    return render(request, template_name="wsite/admin/exam-add-questions.html", context=context)
