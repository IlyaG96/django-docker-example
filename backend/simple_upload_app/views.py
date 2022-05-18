from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fss = FileSystemStorage()
        filename = fss.save(image_file.name, image_file)
        image_url = fss.url(filename)
        print(image_url)
        return render(request, "index.html", {
            "image_url": image_url
        })
    return render(request, "index.html")
