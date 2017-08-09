# -*- coding: utf-8 -*-
# @Date    : 2017-08-09 20:05:32
# @Author  : lileilei
from app.views import (Indexview,LoginView,RegView,LogtView,InterfaceView,
    YongliView,AdminuserView,InterfaceaddView,EditInterfaceView,
    DeleinterView,AddtestcaseView,Deletecase,EditcaseView,DaoruinterView,
    DaorucaseView,AdduserView,SetadView,DeladView,FreadView,FrereView,
    RedpassView,SeruserView,SeryongliView,SerinterView,TestrepView,
    LoadView,MakeonecaseView,DuoyongliView,ProjectView,ModelView,
    AddmodelView,AddproView,DelemodelView,
    DeleproView,EditmoelView,EditproView)
from app import app
app.add_url_rule('/',view_func=Indexview.as_view('index'))
app.add_url_rule('/login',view_func=LoginView.as_view('login'))
app.add_url_rule('/reg',view_func=RegView.as_view('reg'))
app.add_url_rule('/logt',view_func=LogtView.as_view('logt'))
app.add_url_rule('/interface',view_func=InterfaceView.as_view('interface'))
app.add_url_rule('/interface/<int:page>',view_func=InterfaceView.as_view('interfaspa'))
app.add_url_rule('/yongli',view_func=YongliView.as_view('yongli'))
app.add_url_rule('/yongli/<int:page>',view_func=YongliView.as_view('yonglipage'))
app.add_url_rule('/adminuser',view_func=AdminuserView.as_view('adminuser'))
app.add_url_rule('/adminuser/<int:page>',view_func=AdminuserView.as_view('adminuserpage'))
app.add_url_rule('/interface_add',view_func=InterfaceaddView.as_view('interface_add'))
app.add_url_rule('/interfac_edit/<int:id>',view_func=EditInterfaceView.as_view('interfac_edit'))
app.add_url_rule('/dele_inter/<int:id>',view_func=DeleinterView.as_view('dele_inter'))
app.add_url_rule('/addtestcase',view_func=AddtestcaseView.as_view('addtestcase'))
app.add_url_rule('/delete_case/<int:id>',view_func=Deletecase.as_view('delete_case'))
app.add_url_rule('/edit_case/<int:id>',view_func=EditcaseView.as_view('edit_case'))
app.add_url_rule('/daoru_inter',view_func=DaoruinterView.as_view('daoru_inter'))
app.add_url_rule('/daoru_case',view_func=DaorucaseView.as_view('daoru_case'))
app.add_url_rule('/add_user',view_func=AdduserView.as_view('add_user'))
app.add_url_rule('/set_ad/<int:id>',view_func=SetadView.as_view('set_ad'))
app.add_url_rule('/del_ad/<int:id>',view_func=DeladView.as_view('del_ad'))
app.add_url_rule('/fre_ad/<int:id>',view_func=FreadView.as_view('fre_ad'))
app.add_url_rule('/fre_re/<int:id>',view_func=FrereView.as_view('fre_re'))
app.add_url_rule('/red_pass/<int:id>',view_func=RedpassView.as_view('red_pass'))
app.add_url_rule('/ser_user',view_func=SeruserView.as_view('ser_user'))
app.add_url_rule('/ser_yongli',view_func=SeryongliView.as_view('ser_yongli'))
app.add_url_rule('/ser_inter',view_func=SerinterView.as_view('ser_inter'))
app.add_url_rule('/test_rep',view_func=TestrepView.as_view('test_rep'))
app.add_url_rule('/test_rep/<int:page>',view_func=TestrepView.as_view('test_repppage'))
app.add_url_rule('/load/<string:filename>',view_func=LoadView.as_view('load'))
app.add_url_rule('/make_one_case/<int:id>',view_func=MakeonecaseView.as_view('make_one_case'))
app.add_url_rule('/duoyongli',view_func=DuoyongliView.as_view('duoyongli'))
app.add_url_rule('/project',view_func=ProjectView.as_view('project'))
app.add_url_rule('/model',view_func=ModelView.as_view('model'))
app.add_url_rule('/add_moel',view_func=AddmodelView.as_view('add_moel'))
app.add_url_rule('/add_pro',view_func=AddproView.as_view('add_pro'))
app.add_url_rule('/dele_moel/<int:id>',view_func=DelemodelView.as_view('dele_moel'))
app.add_url_rule('/dele_pro/<int:id>',view_func=DeleproView.as_view('dele_pro'))
app.add_url_rule('/edit_moel/<int:id>',view_func=EditmoelView.as_view('edit_moel'))
app.add_url_rule('/edit_pro/<int:id>',view_func=EditproView.as_view('edit_pro'))