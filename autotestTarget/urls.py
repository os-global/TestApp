from django.contrib import admin
from django.urls import path, include
from tcm.views import testnrun, auth, demo

urlpatterns = [
    path('api/', include('api.urls')),

    path('admin/', admin.site.urls),

    path('register/', auth.register, name='register'),
    path('login/', auth.login_view, name='login'),
    path('logout/', auth.logout_view, name='logout'),

    path('', testnrun.dashboard, name='home'),
    path('rating/', testnrun.rating, name='rating'),
    path('tests/', testnrun.test_cases, name='tests'),
    path('runs/', testnrun.test_runs, name='runs'),
    path('test/new/', testnrun.new_test, name='new_test'),

    path('getstat/', testnrun.refresh_stats, name='refresh'),
    path('topauthors/', testnrun.refresh_top_user_stats, name='refresh_authors'),
    path('tests/<int:test_id>', testnrun.update_test, name='update'),
    path('tests/<int:test_id>/delete', testnrun.delete_test, name='delete'),
    path('tests/<int:test_id>/status', testnrun.update_test_status, name='set_status'),
    path('tests/upload', testnrun.upload_tests, name='upload'),
    path('tests/download', testnrun.download_tests, name='download'),

    path('lazytest/', testnrun.lazy_load_tests, name='lazy_test'),
    path('lazyrun/', testnrun.lazy_load_runs, name='lazy_run'),

    path('demoPages/', demo.demo_pages, name='demo_pages'),
    path('demoControls/', demo.demo_controls, name='demo_controls'),
    path('demoPages/testLocation', demo.test_location, name='test_location'),
    path('demoPages/waitPage', demo.wait_page, name='wait_page'),
    path('demoPages/waitAjax', demo.wait_ajax, name='wait_ajax'),
    path('demoPages/crash', demo.crash, name='crash'),
]
