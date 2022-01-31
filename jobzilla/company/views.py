from django.http import request
from django.shortcuts import redirect, render
import random
from company.models import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django .views .decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    if 'companyemail' in request.session:
        uid=user.objects.get(email=request.session['companyemail'])
        cid= company.objects.get(user_id = uid)
        call=company_gallary.objects.filter(company_id=cid)
        jall=jobpost.objects.filter(company_id=cid).order_by('-created_at')
        print("-------> jall",jall)
        context={
                                'uid':uid,
                                'cid':cid,
                                'call':call,
                                'jall':jall,
                            }
        return render(request,"company/company-profile.html",context)

    elif 'customeremail' in request.session:
        uid=user.objects.get(email=request.session['customeremail'])
        crid= customer.objects.get(user_id = uid)
        crall=customer_gallary.objects.filter(customer_id=crid)
        
        jall=jobpost.objects.all().order_by('-created_at')
        print("-------> jall",jall)
       
        context={
                                'uid':uid,
                                'crid':crid,
                                'jall':jall,
                                'crall':crall,
                                
                            }

        return render(request,"company/user-profile.html",context)
    else:
        return render(request,"company/sign-in.html")

def company_signup(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        if uid.role == "company":
            cid=company.objects.get(user_id=uid)
            jall=jobpost.objects.all().order_by('-created_at')

            
            context={
                                'uid':uid,
                                'cid':cid,
                                'jall':jall,
                            }
            return render(request,"company/company-profile.html",context)
        else:
            uid.role == "customer"
            crid=customer.objects.get(user_id=uid)

            
            context={
                                'uid':uid,
                                'cid':crid,
                            }
            return render(request,"company/company-profile.html",context)

    else: 
        try:
            if request.POST:
                if request.POST['role'] == "company":


                    print("----------------submit button pressed------------")
                    company_name=request.POST['company name']
                    company_email=request.POST['company email']
                    company_contact=request.POST['company contact']
                    company_city=request.POST['company city'] 
                    company_category=request.POST['company category']

                    

                    data=['add3','swrt33','erwt234','hjkg90']
                    password=random.choice(data) + company_contact[-3:] + company_email[3:]
                    terms=""
                    try:
                        
                        terms = request.POST['terms']
                        print("terms",terms)
                    except Exception as e:
                        print(type(terms))
                    if terms!="":


                        uid= user.objects.create( email = company_email, password = password , role = request.POST['role'])
                        
                        cid =company.objects.create(user_id=uid,
                                                    company_name=company_name,
                                                    company_address=company_city,
                                                    company_contact=company_contact,
                                        
                                                    company_type=company_category)
                        if cid:
                            print("_______________________sucessfully registered---------------------")

                            s_msg="registerd plese check your email for password"
                            send_mail("confermation mail","welcome to jobzilla portal plese check email for password"+password,"anjali.20.learn@gmail.com",[company_email])
                    
                            return render(request,"company/sign-in.html",{'s_msg':s_msg })
                            
                        else:
                            e_msg="something went wrong"
                            return render(request,"company/sign-in.html",{'e_msg':e_msg})
                    else:
                        e_msg="terms and condition must be agree"
                        return render(request,"company/sign-in.html",{'e_msg':e_msg})

                
                else:
                    pass
                   
        except Exception as e:
            print("---->exception :",e)
            e_msg="email alredy exist"
            return render(request,"company/sign-in.html",{'e_msg':e_msg})
def customer_signup(request):
    print("inside te customer")
    try:
            if request.POST:
                if request.POST['role'] == "customer":
                    print("----------------submit button pressed------------")
                    customer_name=request.POST['customername']
                    customer_email=request.POST['customeremail']
                    customer_qualification=request.POST['customerqualification']
                    customer_contact=request.POST['customercontact']
                    customer_address=request.POST['customeraddress']

                    data=['add3','swrt33','erwt234','hjkg90']
                    password=random.choice(data) + customer_contact[-3:] + customer_email[3:]
                    
                    if request.POST['terms']:
                        uid= user.objects.create( email = customer_email, password = password , role = request.POST['role'])
                        crid=customer.objects.create(user_id=uid,
                                                    customer_name=customer_name,
                                                    customer_contact=customer_contact,
                                                    customer_qualification=customer_qualification,
                                                    customer_address=customer_address)
                        if crid:
                                print("_______________________sucessfully registered---------------------")
                                s_msg="registerd plese check your email for password"
                                send_mail("confermation mail","welcome to jobzilla portal plese check email for password"+password,"anjali.20.learn@gmail.com",[customer_email])             
                                return render(request,"company/sign-in.html",{'s_msg':s_msg })
                        else:
                                 e_msg="something went wrong"
                                 return render(request,"company/sign-in.html",{'e_msg':e_msg})
                    else:
                                e_msg="terms and condition must be agree"
                                return render(request,"company/sign-in.html",{'e_msg':e_msg})
                else:
                    return render(request,"company/sign-in.html")

            else:
                return render(request,"company/sign-in.html")


    except Exception as e:
            print("---->exception :",e)
            e_msg="email alredy exist"
            return render(request,"company/sign-in.html",{'e_msg':e_msg})

def company_profile(request):
    if "email" in request.session:
        uid = user.objects.get(email = request.session['email'])
        cid = company.objects.get(user_id = uid)
        call=company_gallary.objects.filter(company_id=cid)
        jall=jobpost.objects.filter(company_id=cid).order_by('-created_at')
        context = {
                            'uid':uid,
                            'cid':cid,
                            'call':call,
                            'jall':jall,
        }  
        return render(request,"company/company-profile.html",context)
    else:

        return  redirect('company-signin')
@csrf_exempt
def company_signin(request):
    if 'companyemail' in request.session:
        uid=user.objects.get(email=request.session['companyemail'])
        cid= company.objects.get(user_id = uid)
        call=company_gallary.objects.filter(company_id=cid)
        jall=jobpost.objects.filter(company_id=cid).order_by('-created_at')
        
        context={
                                'uid':uid,
                                'cid':cid,
                                'call':call,
                                'jall':jall,
                            }
        return render(request,"company/company-profile.html",context)

    elif 'customeremail' in request.session:
        uid=user.objects.get(email=request.session['customeremail'])
        crid= customer.objects.get(user_id = uid)
        call=company_gallary.objects.filter(company_id=crid)
        crall=customer_gallary.objects.filter(customer_id=crid)
        jall=jobpost.objects.filter(user_id=uid).order_by('-created_at')
        context={
                                'uid':uid,
                                'crid':crid,
                                'jall':jall,
                                'call':call,
                                'crall':crall,
                            }
        return render(request,"company/user-profile.html",context)
       
        
    else:
        try:
            if request.POST:

                email = request.POST['email']
                password = request.POST['password']

            # uid=user.objects.get(email = email)
                #print("------email ",email)
                #print("-------pw is",password)
                uid=user.objects.filter(email = email)
                if uid:
                    if uid[0].password==password:
                        if uid[0].role=="company":

                            uid=user.objects.get(email=email)
                            cid=company.objects.get(user_id=uid)
                            request.session['companyemail']=uid.email
                            return redirect('home')
                            
                        else:
                            uid=user.objects.get(email=email)
                            crid=customer.objects.get(user_id=uid)
                            request.session['customeremail']=uid.email
                            return redirect('home')

                    else:
                        e_msg="invalid password"
                        return render(request,"company/sign-in.html",{'e_msg':e_msg})
                else:
                    e_msg="email does not exist"
                    return render(request,"company/sign-in.html",{'e_msg':e_msg})
            else:
                return render(request,"company/sign-in.html")

        except:
            e_msg="something went wrong"
            return render(request,"company/sign-in.html",{'e_msg':e_msg})
def company_logout(request):
    if 'companyemail' in request.session:
        del request.session['companyemail']
        return redirect('company-signin')

    else:
        if 'customeremail' in request.session:
            del request.session['customeremail']
            return redirect('company-signin')
def update_companydetails(request):
    if 'companyemail' in request.session:
        uid=user.objects.get(email=request.session['companyemail'])
        cid= company.objects.get(user_id = uid)
        call=company_gallary.objects.filter(company_id=cid)
        if request.POST:
            company_name=request.POST['company-name']
            company_established=request.POST['company-establishes']
            company_information=request.POST['company-information']
            company_address=request.POST['company-address']
            cid.company_name=company_name
            cid.company_established=company_established
            cid.company_info=company_information
            cid.company_address=company_address
            cid.save()
            print("sucessfully updated")
            
            context={
                                    'uid':uid,
                                    'cid':cid,
                                    'call':call,
                                }
            return render(request,"company/company-profile.html",context)
    else:
        return redirect('company-signin')

            

def forgot_password(request):
    return render(request,"company/forgotpassword.html")

def send_otp(request):
    try:
        if request.POST:
            email = request.POST['email']
            uid = user.objects.get(email = email)
            otp=random.randint(1111,9999)
            
            
            if uid:
                send_mail("forgott password mail","use otp for reset password"+str(otp),"anjali.20.learn@gmail.com",[uid.email])
                print("uid",uid)
                uid.otp = otp
                uid.save()
                return render(request,"company/reset-password.html",{'email':email})

        else:
            return render(request,"company/forgotpassword.html")
    except:
        e_msg="something went wrong - please check your email"
        return render(request,"company/forgotpassword.html",{'e_msg':e_msg})
    

def reset_password(request):
    try:
        if request.POST:
            email = request.POST['email']
            newpassword = request.POST['newpassword']
            repassword = request.POST['repassword']
            otp=request.POST['otp']
            uid = user.objects.get(email=email)
            print("---------------->",uid)
            print("newpassword---->",newpassword)
            print("repassword---->",repassword)
            print("email---->",email)
            if uid:
                print("-------------uid ---->",uid)
                if newpassword == repassword:
                    # update new password password 
                    print("---> password change ")
                    print("----> inside the msg ")
                    print("-------------uid ---->",uid)
                    if str(uid.otp) == otp:
                        uid.password = newpassword 
                        uid.save()
                        s_msg="sucsessfully password changed" 
                        return render(request,"company/sign-in.html",{'s_msg' :s_msg})
                    else:
                        e_msg="invalid otp"
                        return render(request,"company/reset-password.html",{'e_msg':e_msg,'email':email})
                else:
                    e_msg = "password does not match !!!"
                    print("-----> error msg ",e_msg)
                    return render(request,"company/reset-password.html",{'e_msg':e_msg,'email':email})
        else:
            return render(request,"company/forgotpassword.html")
    except Exception as e:
        print("errorr22-------------> ",e)
        e_msg="something went wrong - please check your email"
        return render(request,"company/reset-password.html",{'e_msg':e_msg})
def companies(request):
    if "companyemail"in request.session:
        uid=user.objects.get(email= request.session['companyemail'])
        cid=company.objects.get(user_id = uid)
        call = company.objects.exclude(user_id=uid)
        print(call)
        context ={
            "uid":uid,
            "cid":cid,
            "company_all" : call
        }
        return render(request,"company/companies.html",context)
    elif "customeremail"in request.session:
        call = company.objects.all
        print(call)
        context ={
            
            "company_all" : call
        }
        return render(request,"company/companies.html",context)
    else:
        return redirect('company-signin')

def user_profiles(request):
    if "companyemail"in request.session:
        uid=user.objects.get(email= request.session['companyemail'])
        cid=company.objects.get(user_id = uid)
        user_all=customer.objects.all
        print(user_all)
        context ={
            "uid":uid,
            "cid":cid,
            "user_all":user_all,
        }
        return render(request,"company/profiles.html",context)
    elif "customeremail"in request.session:
        uid=user.objects.get(email= request.session['customeremail'])
        crid=customer.objects.get(user_id = uid)
        user_all=customer.objects.exclude(user_id=uid)
        print(user_all)
        context ={
            "uid":uid,
            "crid":crid,
            "user_all" : user_all,
        }
        return render(request,"company/profiles.html",context)
    else:
        return render(request,"company/profiles.html")

def profile_setting(request):
    if "companyemail" in request.session:
        uid=user.objects.get(email= request.session['companyemail'])
        cid=company.objects.get(user_id = uid)
        context ={
            'uid':uid,
            'cid':cid,
        }
        return render(request,"company/profile-account-setting.html",context)
    else:
        if "customeremail" in request.session:

            uid=user.objects.get(email= request.session['customeremail'])
            crid=customer.objects.get(user_id = uid)
            crall=customer_gallary.objects.filter(customer_id=crid)
            context ={
                'uid':uid,
                'crid':crid,
                'crall':crall,
            }
            return render(request,"company/user-profileacount-setting.html",context)
def company_password_change(request):
    
    if "companyemail" in request.session:
        uid=user.objects.get(email= request.session['companyemail'])
        cid=company.objects.get(user_id = uid)
        
        if request.POST:
            old_password=request.POST['old-password']
            new_password=request.POST['new-password']
            repeat_password=request.POST['repeat-password']
            if uid.password==old_password:
                print("password match")
                if new_password==repeat_password:
                    print("update password")
                    context ={
                        'uid':uid,
                        'cid':cid,
                        's_msg':"password successfully updated"
                    }
                    uid.password=new_password
                    uid.save()
                    return render(request,"company/profile-account-setting.html",context)
                else:
                    context ={
                        'uid':uid,
                        'cid':cid,
                        'e_msg':"password did not match"
                    }
                    return render(request,"company/profile-account-setting.html",context)
            else:
                context ={
                            'uid':uid,
                            'cid':cid,
                            'e_msg':"old password did not match"
                        }
                return render(request,"company/profile-account-setting.html",context)
        else:
            context ={
                    'uid':uid,
                    'cid':cid,
                }
            return render(request,"company/profile-account-setting.html",context)
def user_password_change(request):
    if "customeremail" in request.session:
        uid=user.objects.get(email= request.session['customeremail'])
        crid=customer.objects.get(user_id = uid)
        
        if request.POST:
            old_password=request.POST['old-password']
            new_password=request.POST['new-password']
            repeat_password=request.POST['repeat-password']
            if uid.password==old_password:
                print("password match")
                if new_password==repeat_password:

                    print("update password")
                    context ={
                        'uid':uid,
                        'crid':crid,
                        's_msg':"password successfully updated"
                    }
                    uid.password=new_password
                    uid.save()
                    return render(request,"company/user-profileacount-setting.html",context)
                else:
                    context ={
                        'uid':uid,
                        'crid':crid,
                        'e_msg':"password did not match"
                    }
                    return render(request,"company/user-profileacount-setting.html",context)
            else:

                context ={
                            'uid':uid,
                            'crid':crid,
                            'e_msg':"old password did not match"
                        }
                return render(request,"company/user-profileacount-setting.html",context)
        else:
            context ={
                    'uid':uid,
                    'crid':crid,
                    }
            return render(request,"company/user-profileacount-setting.html",context)
    

def upload_company_logo(request):
    if "companyemail" in request.session:
        uid=user.objects.get(email= request.session['companyemail'])
        cid=company.objects.get(user_id = uid)
        if 'company_logo' in request.FILES:
            company_logo=request.FILES['company_logo']
            cid.company_logo =company_logo
            cid.save()
        if 'company_cover_pic' in request.FILES:
            company_cover=request.FILES['company_cover_pic']
            cid.company_cover =company_cover
            cid.save()
        context ={
            'uid':uid,
            'cid':cid,
        }
        return render(request,"company/company-profile.html",context)
    else:
       if "customeremail" in request.session:

            uid=user.objects.get(email= request.session['customeremail'])
            crid=customer.objects.get(user_id = uid)
            if 'customer_logo' in request.FILES:
                customer_logo=request.FILES['customer_logo']
                crid.customer_logo =customer_logo
                crid.save()
            if 'customer_cover' in request.FILES:
                customer_cover=request.FILES['customer_cover']
                crid.customer_cover =customer_cover
                crid.save()
            context ={
                'uid':uid,
                'crid':crid,
            }
            return render(request,"company/company-profile.html",context)
def view_othercompany_profile(request,pk):
    cid=company.objects.get(id=pk)
    call=company_gallary.objects.filter(company_id=cid)
    context={
        'cid':cid,
        'call':call,
    }
    return render(request,"company/view-othercompany-profile.html",context)

def view_otheruser_profile(request,pk):
    crid=customer.objects.get(id=pk)
    call=company_gallary.objects.filter(company_id=crid)
    context={
        'crid':crid,
        'call':call,
    }
    return render(request,"company/view_user-profile.html",context)

def update_company_portfolio(request):
    if "companyemail" in request.session:
        uid=user.objects.get(email= request.session['companyemail'])
        cid=company.objects.get(user_id = uid)

        if request.FILES:
            pic=request.FILES['portfolio']
            cid_pic=company_gallary.objects.create(company_id=cid ,picture=pic)
            call=company_gallary.objects.filter(company_id=cid)
            if cid_pic:
                context ={
                    'uid':uid,
                    'cid':cid,
                    'call':call,
                    }
                return render(request,"company/company-profile.html",context)
            else:
                context ={
                'uid':uid,
                'cid':cid,
                }
                return render(request,"company/profile-account-setting.html",context)
        else:
            context ={
            'uid':uid,
            'cid':cid,
            }
            return render(request,"company/profile-account-setting.html",context)

def update_userportfolio(request):
    if "customeremail" in request.session:
        uid=user.objects.get(email= request.session['customeremail'])
        crid=customer.objects.get(user_id = uid)

        if request.FILES:
            pic=request.FILES['userportfolio']
            crid_pic=customer_gallary.objects.create(customer_id=crid ,picture=pic)
            crall=customer_gallary.objects.filter(customer_id=crid)
            if crid_pic:
                context ={
                    'uid':uid,
                    'crid':crid,
                    'crall':crall,
                    }
                return render(request,"company/user-profile.html",context)
            else:
                context ={
                'uid':uid,
                'crid':crid,
                }
                return render(request,"company/user-profileaccount-setting.html",context)
        else:
            context ={
            'uid':uid,
            'crid':crid,
            }
            return render(request,"company/user-profileaccount-setting.html",context)
    

def job_post(request):
    if "companyemail" in request.session:
        uid=user.objects.get(email= request.session['companyemail'])
        cid=company.objects.get(user_id = uid)
        jall=jobpost.objects.filter(company_id=cid).order_by('-created_at')
        if request.POST:
            print("in tis job")
            jid=jobpost.objects.create(
                company_id=cid,
                job_title=request.POST['job_title'],
                job_description=request.POST['job_description'],
                job_type=request.POST['job_type'],
                job_salary=request.POST['job_salary'],
                emp_requirement=request.POST['emp_requirement'],
                job_tags=request.POST['job_tags'],
            )
            jall=jobpost.objects.filter(company_id=cid).order_by('-created_at')

            if jid:
                context={
                    'uid':uid,
                    'cid':cid,
                    'jall':jall,
                }
                return render(request,"company/company-profile.html",context)
            else:
                context={
                    'uid':uid,
                    'cid':cid,
                    'jall':jall,
                }
                return render(request,"company/company-profile.html",context)

        else:
            return redirect('home')
    else:
        return redirect('home')
def like_jobpost(request,pk):
    if 'companyemail' in request.session:
        uid=user.objects.get(email=request.session['companyemail'])
        cid= company.objects.get(user_id = uid)
        call=company_gallary.objects.filter(company_id=cid)

        jall=jobpost.objects.filter(company_id=cid).order_by('-created_at')
        print("-------> jall",jall)
        context={
                                'uid':uid,
                                'cid':cid,
                                'call':call,
                                'jall':jall,
                            }
        return render(request,"company/company-profile.html",context)

    elif 'customeremail' in request.session:
        uid=user.objects.get(email=request.session['customeremail'])
        crid= customer.objects.get(user_id = uid)
        jall=jobpost.objects.all().order_by('-created_at')
        print("--------pk",pk)
        jid=jobpost.objects.get(id=pk)
        likejobs=postlike.objects.filter(jobpost_id=pk)
        if likejobs:
            pall=postlike.objects.all()
            all_customers=[]

            for i in pall:
                all_customers.append(i.customer_id)

            if crid in all_customers:
                print("you have alredy like this post")
            else:

                like_id=postlike.objects.create(jobpost_id=jid,customer_id=crid,likes=likejobs[0].likes+1)
                print("alredy like")
        else:
            like_id=postlike.objects.create(jobpost_id=jid,customer_id=crid,likes=1)

        jall=jobpost.objects.all().order_by('-created_at')
        for job in jall:
            print("_------job like",job.job_title)
            all_likes=postlike.objects.filter(jobpost_id=job.id)
            print("------all likes",all_likes)
            for iteam in all_likes:
                print("------all likes",iteam.likes)
        context={
                                'uid':uid,
                                'crid':crid,
                                'jall':jall,
                            }

        return render(request,"company/user-profile.html",context)
def post_like(request,pk):
    if 'companyemail' in request.session:
        uid=user.objects.get(email=request.session['companyemail'])
        cid= company.objects.get(user_id = uid)
        call=company_gallary.objects.filter(company_id=cid)

        jall=jobpost.objects.filter(company_id=cid).order_by('-created_at')
        print("-------> jall",jall)
        jid=jobpost.objects.get(id=pk)
        p_likes_by=postlike.objects.filter(jobpost_id=jid)
        context={
                                'uid':uid,
                                'cid':cid,
                                'call':call,
                                'jall':jall,
                                'p_likes_by':p_likes_by,
                            }
        
        return render(request,"company/post-like.html",context)

def follow(request,pk):
    if 'customeremail' in request.session:
        uid=user.objects.get(email=request.session['customeremail'])
        crid= customer.objects.get(user_id = uid)
        cid= company.objects.get(id=pk)
        
        company_all=company.objects.all()
        fall=companyfollowers.objects.all()
        all_companies=[]
        all_customers=[]
        for i in fall:
            all_companies.append(i.company_id)
            all_customers.append(i.customer_id)

        if cid in all_companies and crid in all_customers:
            print("alredy followed this company")

        else:
            fid=companyfollowers.objects.create(customer_id=crid,company_id=cid)
            print("following request added")

        print("----all companies=",all_companies)
        print("-----all customers=",all_customers)
        context={
                                'uid':uid,
                                'cid':cid,
                                'company_all':company_all,
                            }
        
        return render(request,"company/companies.html",context)

def delete_post(request,pk):
    if 'companyemail' in request.session:
        jall_id=jobpost.objects.get(id=pk)
        print("-------> jall",jall_id)
        jall_id.delete()
        return redirect('home')
    else:
        return redirect('home')

def close_post(request,pk):
    if 'companyemail' in request.session:
        jall_id=jobpost.objects.get(id=pk)
        jall_id.status="close"
        jall_id.save()
        return redirect('home')
    else:
        return redirect('home') 
    