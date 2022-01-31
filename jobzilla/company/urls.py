from django.contrib import admin
from django.urls import path
from company import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('company-signup', views.company_signup, name='company-signup'),
    path('company-signin',views.company_signin,name='company-signin'),
    path('customer-signup',views.customer_signup,name='customer-signup'),
    path('company-profile',views.company_profile,name="company-profile"),
    path('company-logout',views.company_logout,name="company-logout"),
    path('update-companydetails',views.update_companydetails,name='update-companydetails'),
    
    path('forgotpassword/',views.forgot_password,name="forgotpassword"),
    path('send-otp/',views.send_otp,name="send-otp"),
    
    path('reset-password/',views.reset_password,name="reset-password"),
    path('companies/',views.companies,name="companies"),
    path('user-profiles',views.user_profiles,name="user-profiles"),
    path('profile-account-setting',views.profile_setting,name='profile-account-setting'),
    path('upload-company-logo',views.upload_company_logo,name='upload-company-logo'),
    path('company-password-change',views.company_password_change,name='company-password-change'),
    path('user-password-change',views.user_password_change,name='user-password-change'),
    path('view-othercompany-profile/<int:pk>/',views.view_othercompany_profile,name='view-othercompany-profile'),
    
    path('update-company-portfolio',views.update_company_portfolio,name='update-company-portfolio'),
    path('update-customer-portfolio',views.update_userportfolio,name='update-customer-portfolio'),
    path('job-post/',views.job_post,name="job-post"),
    path('like-jobpost/<int:pk>/',views.like_jobpost,name="like-jobpost"),
    path('post-like/<int:pk>/',views.post_like,name="post-like"),
    path('follow/<int:pk>/',views.follow,name="follow"),
    path('delete-post/<int:pk>/',views.delete_post,name='delete-post'),
    path('close-post/<int:pk>/',views.close_post,name='close-post'),
    path('view-otheruserprofile/<int:pk>/',views.view_otheruser_profile,name='view-otheruserprofile'),
    
]
