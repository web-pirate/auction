import os
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *


def home(request):

    item_obj = reversed(Item.objects.all())
    allVehicles = reversed(Item.objects.filter(category="vehicles").all())
    alljewelry = reversed(Item.objects.filter(category="jewelry").all())

    icount = 0
    vcount = 0
    jcount = 0

    items = []
    vehicle = []
    jewelry = []

    for v in allVehicles:
        if vcount == 3:
            vcount = 0
            break
        else:
            ap = vehicle.append(v)
            vcount = vcount+1

    for v in alljewelry:
        if jcount == 3:
            jcount = 0
            break
        else:
            ap = jewelry.append(v)
            jcount = jcount+1

    for v in item_obj:
        if icount == 6:
            icount = 0
            break
        else:
            ap = items.append(v)
            icount = icount+1

    # print(item_obj)

    # if request.user.is_authenticated:
    #     current = request.user
    #     return render(request, 'index.html', {"current": current})
    return render(request, 'index.html', {'items': items, "vehicle": vehicle, "jewelry": jewelry})


def register(request):
    title = "Register"
    if request.method == "POST":
        uname = request.POST.get('userName')
        fname = request.POST.get('firstName')
        lname = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('cpassword')

        if password == password2:
            new_user = User.objects.create_user(
                username=uname, first_name=fname, last_name=lname, email=email, password=password)
            new_user.save()
        return redirect("home")

    return render(request, 'register.html')


def login(request):
    title = "Login"
    if request.method == "POST":
        uname = request.POST.get('userName')
        password = request.POST.get('password')

        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request, user)

        return redirect('home')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def user_details(request):
    user_obj = User.objects.filter(username=request.user).first()
    title = "User Details"
    if request.method == "POST":
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        addhar = request.POST.get('addhar')
        profile_img = request.FILES['profile_img']

        create_details = UserDetails(
            user=request.user, image=profile_img, addhar=addhar, dob=dob, address=address, phone=phone)
        create_details.save()
        return redirect('home')
    return render(request, 'user_details.html', {'user': user_obj})


def profile(request):
    UserDetails_obj = UserDetails.objects.filter(user=request.user).first()
    print(UserDetails_obj.image)
    print(UserDetails_obj.user.first_name)

    totalBid = Item.objects.all().count()
    mybid = Bid.objects.filter(name=request.user).count()
    info = {
        'bids': totalBid,
        'mybid': mybid
    }

    return render(request, 'profile.html', {'user': UserDetails_obj, 'info': info})


def update_profile(request):
    UserDetails_obj = UserDetails.objects.filter(user=request.user).first()
    if request.method == "POST":
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        addhar = request.POST.get('addhar')
        profile_img = request.FILES['profile_img']

        update_details = UserDetails(id=request.user.id,
                                     user=request.user, image=profile_img, addhar=addhar, dob=dob, address=address, phone=phone)
        update_details.save()

        if len(profile_img) > 0:
            os.remove(UserDetails_obj.image.path)
        return redirect('profile')

    return render(request, 'updateProfile.html', {'user_update': UserDetails_obj})


def bid(request, pk):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    item = Item.objects.filter(id=pk).first()
    bid = Bid.objects.filter(product=item).all().count()
    avg_bid = Bid.objects.filter(product=item).all()
    print(avg_bid)
    sum = 0

    for i in avg_bid:
        price = i.amout
        sum = sum + price

    if bid == 0:
        avg = 0
    else:
        avg = int(sum/bid)

    user_auth = User.objects.filter(username=request.user).first()
    print(user_auth.password)
    if request.method == "POST":
        amount = request.POST.get('amount')
        print(amount)
        password = request.POST.get('password')
        print(password)

        user = auth.authenticate(username=request.user, password=password)
        if user is not None:
            create_bid = Bid(product=item,
                             name=request.user, amout=amount)
            create_bid.save()
            return redirect("home")

    return render(request, 'bid.html', {'item': item, 'bid': bid, "avg": avg})


def productUpload(request):
    title = "Product Upload"
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES['item_img']
        price = request.POST.get('price')
        category = request.POST.get('category')

        if request.user.is_authenticated:
            create_item = Item(user=request.user, image=image,
                               name=name, price=price, category=category)
            create_item.save()
            return redirect("home")
        else:
            return redirect('login')

    return render(request, 'productUpload.html')


def productView(request, category):
    item_obj = reversed(Item.objects.all())
    allItems = reversed(Item.objects.filter(category=category).all())
    return render(request, 'productView.html', {"items": allItems, "category": category})


def contact(request):
    return render(request, 'contacts.html')
