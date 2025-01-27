# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LuckyAddress(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='主键id')
    user_id = models.IntegerField(db_comment='用户id')
    address = models.CharField(max_length=255, db_comment='详细地址')
    phone = models.IntegerField(db_comment='收货手机号')

    class Meta:
        managed = False
        db_table = 'lucky_address'
        db_table_comment = '地址库'


class LuckyAdmin(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='主键id')
    name = models.CharField(max_length=255, db_comment='用户姓名')
    phone = models.IntegerField(db_comment='手机号')
    admin_pass = models.CharField(max_length=255, db_comment='密码')
    user_status = models.IntegerField(db_comment='用户状态：0失效、1有效')
    create_time = models.DateTimeField(db_comment='创建时间')
    update_time = models.DateTimeField(db_comment='更新时间')

    class Meta:
        managed = False
        db_table = 'lucky_admin'
        db_table_comment = '后台管理'


class LuckyBrand(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='主键')
    name = models.CharField(max_length=255, db_comment='品牌名称')
    status = models.IntegerField(db_comment='品牌状态：0失效、1有效')

    class Meta:
        managed = False
        db_table = 'lucky_brand'
        db_table_comment = '品牌表'


class LuckyDetailsImg(models.Model):
    sku_id = models.IntegerField(primary_key=True, db_comment='skuid')
    img = models.CharField(max_length=255, db_comment='图片地址')
    sort_num = models.IntegerField(db_comment='排序')

    class Meta:
        managed = False
        db_table = 'lucky_details_img'
        db_table_comment = '商品详情图'


class LuckyOrder(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='主键id')
    user_id = models.IntegerField(db_comment='用户id')
    parent_order_no = models.IntegerField(db_comment='父订单号')
    order_no = models.IntegerField(db_comment='子订单号')
    status = models.IntegerField(db_comment='订单状态')
    spu_id = models.IntegerField(db_comment='spuid')
    sku_id = models.IntegerField(db_comment='skuid')
    num = models.IntegerField(db_comment='数量')
    pay_price = models.DecimalField(max_digits=10, decimal_places=2, db_comment='实际支付金额')
    total_original_price = models.DecimalField(max_digits=10, decimal_places=2, db_comment='供货价合计')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, db_comment='销售价合计')
    serial_no = models.IntegerField(db_comment='流水号')
    brand_id = models.IntegerField(db_comment='品牌id')
    supplier_id = models.IntegerField(db_comment='供应商id')
    ship_bak = models.CharField(max_length=255, blank=True, null=True, db_comment='备注信息')
    address_id = models.IntegerField(db_comment='地址id')
    create_time = models.DateTimeField(db_comment='创建时间')
    update_time = models.DateTimeField(db_comment='更新时间')

    class Meta:
        managed = False
        db_table = 'lucky_order'
        db_table_comment = '订单表'


class LuckyPaymentUser(models.Model):
    user_id = models.IntegerField(primary_key=True, db_comment='用户id')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_comment='余额')
    freeze_price = models.DecimalField(max_digits=10, decimal_places=2, db_comment='冻结金额')

    class Meta:
        managed = False
        db_table = 'lucky_payment_user'
        db_table_comment = '余额构成'


class LuckyPrimaryImg(models.Model):
    sku_id = models.IntegerField(primary_key=True, db_comment='skuid')
    img = models.CharField(max_length=255, db_comment='图片地址')
    sort_num = models.IntegerField(db_comment='排序')

    class Meta:
        managed = False
        db_table = 'lucky_primary_img'
        db_table_comment = '商品头图'


class LuckyShoppingTrolley(models.Model):
    user_id = models.IntegerField(primary_key=True, db_comment='用户id')
    spu_id = models.IntegerField(db_comment='SPUid')
    sku_id = models.IntegerField(db_comment='SKUid')
    num = models.IntegerField(db_comment='数量')
    brand_id = models.IntegerField(db_comment='品牌id')
    sku_status = models.IntegerField(db_comment='可售状态：0不可售、1可售')

    class Meta:
        managed = False
        db_table = 'lucky_shopping_trolley'
        db_table_comment = '购物车'


class LuckySku(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='SKU商品id')
    spu_id = models.IntegerField(db_comment='SPU商品id')
    sku_status = models.IntegerField(db_comment='sku商品状态：0不可售、1可售')
    specification = models.CharField(max_length=255, db_comment='规格')
    bar_code = models.CharField(max_length=255, db_comment='供应商编码')
    original_price = models.DecimalField(max_digits=10, decimal_places=2, db_comment='供货价')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_comment='销售价')
    display_price = models.DecimalField(max_digits=10, decimal_places=2, db_comment='原价')
    rate = models.DecimalField(max_digits=10, decimal_places=2, db_comment='利润率')
    discount = models.IntegerField(db_comment='折扣')
    stock = models.IntegerField(db_comment='库存')
    sales = models.IntegerField(db_comment='销量')
    create_time = models.DateTimeField(db_comment='创建时间')
    update_time = models.DateTimeField(db_comment='更新时间')

    class Meta:
        managed = False
        db_table = 'lucky_sku'
        db_table_comment = 'SKU商品信息'


class LuckySpu(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='SPU商品id')
    title = models.CharField(max_length=255, db_comment='商品名称 ')
    img = models.CharField(max_length=255, db_comment='头图地址')
    spu_status = models.IntegerField(db_comment='商品状态：0不可售、1可售')
    sort_num = models.IntegerField(db_comment='排序')
    supplier_id = models.IntegerField(db_comment='供应商id')
    brand_id = models.IntegerField(db_comment='品牌id')
    create_time = models.DateTimeField(db_comment='创建时间')
    update_time = models.DateTimeField(db_comment='更新时间')

    class Meta:
        managed = False
        db_table = 'lucky_spu'
        db_table_comment = 'SPU商品信息'


class LuckySupplier(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='主键')
    name = models.CharField(max_length=255, db_comment='供应商名称')
    status = models.IntegerField(db_comment='供应商状态：0失效、1有效')

    class Meta:
        managed = False
        db_table = 'lucky_supplier'
        db_table_comment = '供应商表'


class LuckyUser(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='主键id')
    name = models.CharField(max_length=20, db_comment='姓名')
    phone = models.IntegerField(db_comment='手机号')
    user_pass = models.CharField(max_length=255, db_comment='密码')
    status = models.IntegerField(db_comment='状态：0无效、1有效')
    create_time = models.DateTimeField(db_comment='创建时间')
    update_time = models.DateTimeField(db_comment='更新时间')

    class Meta:
        managed = False
        db_table = 'lucky_user'
        db_table_comment = '用户表'
