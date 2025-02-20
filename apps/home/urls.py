# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import views
from django.urls import path, re_path
# from .views import save_and_check_data
# from .views import mongodb_test, save_to_mongo, find_in_mongo

urlpatterns = [
    # The home page
    # path('save_and_check_data/', save_and_check_data, name='save_and_check_data'),
    # path('mongodb_test', views.mongodb_test, name='mongodb_test'),
    # path('save_to_mongo', views.save_to_mongo, name='save_to_mongo'),
    path('find_in_mongo', views.find_in_mongo, name='find_in_mongo'),
    path('send_custom_data', views.send_custom_data, name='send_custom_data'),
    path('unique_id', views.unique_id, name='unique_id'),
    path('get_data', views.get_data, name='get_data'),
    # path('download-pdf', views.download_pdf, name='download_pdf'),
    path('pdfOcrDone', views.pdf_ocr_done, name='pdfOcrDone'),
    # path('extract_metadata', views.extract_metadata, name='extract_metadata'),
    path("", views.index, name="home"),
    # path("index", views.index, name="home"),
    path("imagetoText", views.imagetoText, name="imagetoText"),
    path("imagetoTextPan", views.imagetoTextPan, name="imagetoTextPan"),
    path("insertintoDatabase", views.insert_into_database, name="insertintoDatabase"),
    path("updateDatabase", views.update_database, name="updateDatabase"),
    path("verifyexists", views.verify_exists, name="verifyexists"),
    path("searchDatabase", views.search_database, name="searchDatabase"),
    path("audio_to_text", views.audioToText, name="audio_to_text"),
    path("deleterecord", views.delete_record, name="deleterecord"),
    path('autocomplete', views.AdharAutocomplete, name="adhar-autocomplete"),
    # path('generate-pdf', views.generate_pdf, name='generate_pdf'),
    path('pdfExtract', views.pdfExtract, name='pdfExtract'),
    path('delete_draft', views.delete_draft, name="delete_draft"),
    # path('upload', views.extract_text_from_pdf, name='extract_text_from_pdf'),
    
    path('extract_text_from_pdf', views.extract_text_from_pdf, name='extract_text_from_pdf'),
    # path('kmsDataView', views.kmsDataView, name="kmsDataView"),

    path("selectText", views.select_text, name="selectText"),
    path("selectTextCropper", views.select_cropper, name="selectTextCropper"),
    path("selectionOCR", views.select_ocr, name="selectionOCR"),
    path("pdfOCR", views.pdf_ocr, name="pdfOCR"),
    path("imageUpload", views.image_upload, name="imageUpload"),
    path("tool", views.tool, name = "tool"),
    path("speechToText", views.speech_to_text, name="speechToText"),
    path("speechToTextNew", views.speech_to_text_new, name="speechToTextNew"),
    path("help", views.help, name="help"),
    path("kms", views.KMS, name="kms"),
    path("myQueue", views.MyQueue, name="myQueue"),
    path("management", views.UserManagement, name="management"),
    path("dashboard", views.Dashboard, name="dashboard"),
    path("mahadiscomreg", views.mahadiscomreg, name="mahadiscomreg"),
    path("firform", views.fir, name="firform"),
    # Matches any html file
    re_path(r"^.*\.*", views.pages, name="pages"),
]
