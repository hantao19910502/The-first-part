from django.contrib import admin

# Register your models here.



from  models import UserType ,Admin,News,NewsType,Reply,Chats
admin.site.register( UserType )
admin.site.register( Admin)
admin.site.register( News)
admin.site.register( NewsType)
admin.site.register( Reply)
admin.site.register( Chats)
