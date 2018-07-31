from django.db import models


class user(models.Model):
    class Meta():
        verbose_name = '用户'
        verbose_name_plural = '所有用户'
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=20)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    age = models.CharField(max_length=5)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    job = models.CharField(max_length=20)
    creatdate = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.uid, self.uname, self.email, self.telephone, self.unit, self.job, self.creatdate


class report(models.Model):
    class Meta():
        verbose_name = '年报'
        verbose_name_plural = '所有年报'
    rid = models.AutoField(primary_key=True)
    rcp = models.ForeignKey('company', on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    text = models.TextField()
    filename = models.CharField(max_length=30)

    def __unicode__(self):
        return self.rid, self.year, self.rcp_id


class company(models.Model):
    class Meta():
        verbose_name = '公司'
        verbose_name_plural = '所有公司'
    cid = models.AutoField(primary_key=True)
    cnum = models.CharField(max_length=10)
    csname = models.CharField(max_length=10)
    cfname = models.CharField(max_length=30)
    website = models.URLField()

    def __unicode__(self):
        return self.cid, self.cnum, self.cfname, self.website


class new(models.Model):
    class Meta():
        verbose_name = '动态'
        verbose_name_plural = '所有动态'
    nid = models.AutoField(primary_key=True)
    ncp = models.ForeignKey('company', on_delete=models.CASCADE)
    newdate = models.DateField(auto_now_add=True)
    newtext = models.TextField()

    def __unicode__(self):
        return self.nid, self.newdate, self.ncp_id