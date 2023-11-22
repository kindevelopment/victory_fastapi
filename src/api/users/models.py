from sqlalchemy import String, Text, Integer, ARRAY, Boolean, Float, DateTime, Time, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from src.api.common.models import BaseModel


class User(BaseModel):
    username = mapped_column(String)
    password = mapped_column(String)
    token = mapped_column(Text)
    fio = mapped_column(String)
    premissions = mapped_column(Integer)
    group = mapped_column(Integer)
    projects = mapped_column(ARRAY(Integer))
    sites = mapped_column(ARRAY(Integer))
    archive = mapped_column(Boolean, default=False)
    active_operator_session = mapped_column(Boolean, default=False)
    tg_id = mapped_column(Integer)
    balance = mapped_column(Float)
    role_id = mapped_column(Integer)
    department = mapped_column(String)
    position = mapped_column(String)
    assigned = mapped_column(String)
    assigned_id = mapped_column(Integer)
    group_id = mapped_column(Integer)
    uis_login = mapped_column(String)
    uis_password = mapped_column(String)
    rtc_on = mapped_column(Boolean, default=False)
    phone_number = mapped_column(String)

    __tablename__ = 'users'


class Sites2(BaseModel):
    site = mapped_column(String)
    token = mapped_column(Text)
    dealer = mapped_column(Text)
    pre_final_noanswer = mapped_column(Text)
    pre_final_exp = mapped_column(Text)

    __tablename__ = 'sites2'


class Groups_cc(BaseModel):
    name = mapped_column(String)
    archive = mapped_column(Boolean, default=False)
    call_norm = mapped_column(Integer)
    price_success = mapped_column(Float)
    price_call = mapped_column(Float)
    listening = mapped_column(Boolean, default=False)

    __tablename__ = 'groups_cc'


class ApiResults2(BaseModel):
    """Результат апи (заявки)"""
    date = mapped_column(DateTime)
    mobile_tel = mapped_column(String)
    email = mapped_column(String)
    site = mapped_column(String, index=True)
    utm_source = mapped_column(Text)
    utm_campaing = mapped_column(Text)
    utm_medium = mapped_column(Text)
    utm_term = mapped_column(Text)
    utm_content = mapped_column(Text)
    status = mapped_column(String, index=True)
    name = mapped_column(String)
    assigned = mapped_column(String)
    assigned_id = mapped_column(Integer, index=True)
    checked = mapped_column(Boolean, default=False)
    date_created = mapped_column(DateTime)
    date_updated = mapped_column(DateTime)
    success_date = mapped_column(DateTime)
    project_id = mapped_column(Integer)
    income_in = mapped_column(Integer)
    income_out = mapped_column(Integer)
    bitrix_id = mapped_column(Integer)
    loaded_sheets = mapped_column(Boolean, default=False)
    in_queque = mapped_column(Boolean, default=False)
    avito = mapped_column(Boolean, default=False)
    phone_id = mapped_column(Integer)
    brand = mapped_column(String)
    model = mapped_column(String)
    cuz = mapped_column(String)
    color = mapped_column(String)
    ad_id = mapped_column(Integer)
    year = mapped_column(String)
    photo_pack_link = mapped_column(Text)
    penalty_check = mapped_column(Boolean, default=False)
    penalty_status = mapped_column(String)
    listener1_id = mapped_column(Integer)
    listener2_id = mapped_column(Integer)
    listener1_datetime = mapped_column(DateTime)
    listener2_datetime = mapped_column(DateTime)
    tr_nomer = mapped_column(Float)
    tr_oper = mapped_column(Float)
    tr_suc = mapped_column(Float)
    tr_pros = mapped_column(Float)
    tr_ruk = mapped_column(Float)
    full_tr = mapped_column(Float)
    status_before_success = mapped_column(String)
    success_id = mapped_column(Integer)
    children = relationship("Success_stat", back_populates="api_result2")

    __tablename__ = 'apiresults2'


class Comments2(BaseModel):
    answerid = mapped_column(Integer)
    date = mapped_column(DateTime)
    comment = mapped_column(Text)
    updated = mapped_column(DateTime)
    author = mapped_column(String)
    user_id = mapped_column(Integer)

    __tablename__ = 'comments2'


class Projects2(BaseModel):
    name = mapped_column(String)
    sites = mapped_column(ARRAY(Integer))
    description = mapped_column(Text)
    token = mapped_column(Text)
    car_condition = mapped_column(Text)
    bt = mapped_column(Boolean, default=False)
    bitrixroute = mapped_column(Text)
    status_id = mapped_column(String)
    tg_users_id = mapped_column(ARRAY(Integer))
    timezone = mapped_column(Integer)
    archive = mapped_column(Boolean, default=False)
    amo = mapped_column(Boolean, default=False)
    income_in = mapped_column(Integer)
    income_out = mapped_column(Integer)
    sites_name = mapped_column(ARRAY(String))
    sheets = mapped_column(Text)
    list = mapped_column(Text)
    answer_cost = mapped_column(Integer)
    avito = mapped_column(Boolean, default=False)
    bitrix_title = mapped_column(Text)
    numbers = mapped_column(Boolean, default=False)
    experiment = mapped_column(Integer)
    uniq = mapped_column(Integer)
    utm_status = mapped_column(Text)
    name_for_operator = mapped_column(String)
    managers_id = mapped_column(ARRAY(Integer))
    vdl = mapped_column(Boolean, default=False)
    group_id = mapped_column(Integer)
    status = mapped_column(String)
    needed_price = mapped_column(Float)
    vdl_tz = mapped_column(Text)
    pre_final_noanswer = mapped_column(Text)
    pre_final_exp = mapped_column(Text)
    script_lvl = mapped_column(Integer)
    days_to_reset = mapped_column(Integer)
    rtc_transfer = mapped_column(Boolean, default=False)
    status_change_date = mapped_column(DateTime)

    __tablename__ = 'projects2'


class Oper_Stat_New(BaseModel):
    """ Логи оператора - каждое изменение - одна строка """
    user_id = mapped_column(Integer)
    answer_id = mapped_column(Integer)
    status = mapped_column(String)
    status_before = mapped_column(String)
    date = mapped_column(DateTime)
    time = mapped_column(Time)
    project_id = mapped_column(Integer)
    site = mapped_column(String)

    __tablename__ = 'operator_stat_new'


class Success_stat(BaseModel):
    answer_id = mapped_column(ForeignKey("apiresults2.id"))
    answer = relationship('ApiResults2', back_populates="success_stat")
    site_id = mapped_column(Integer)
    project_id = mapped_column(Integer)
    assigned_id = mapped_column(Integer)
    site_name = mapped_column(String)
    project_name = mapped_column(String)
    assigned_name = mapped_column(String)
    datetimef = mapped_column(DateTime)

    __tablename__ = 'success_stat'


class Withdraws(BaseModel):
    user_id = mapped_column(Integer)
    balance_before = mapped_column(Float)
    withdraw = mapped_column(Float)
    balance_after = mapped_column(Float)
    date = mapped_column(DateTime)
    time = mapped_column(Time)
    assigned_id = mapped_column(Integer)
    type_id = mapped_column(Integer)
    type_name = mapped_column(String)
    type = mapped_column(String)
    comment = mapped_column(Text)
    status = mapped_column(String)

    __tablename__ = 'withdraws'


class Withdraw_types(BaseModel):
    name = mapped_column(String)
    type = mapped_column(String)

    __tablename__ = 'withdraw_types'
