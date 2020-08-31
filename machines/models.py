from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    wday = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128, null=False)
    objects = models.Manager()

    def __str__(self):
        return self.name


class TechLeader(models.Model):
    name = models.CharField(max_length=100)
    wday = models.DateField(auto_now_add=True)
    startday = models.DateField()
    email = models.EmailField(max_length=254, unique=True, default='to1@example.com')
    user = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='techleaders')

    def __str__(self):
        return self.name

class DiagResp(models.Model):
    name = models.CharField(max_length=100)
    wday = models.DateField(auto_now_add=True)
    startday = models.DateField()
    email = models.EmailField(max_length=254, unique=True)
    user = models.CharField(max_length=30, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='diagresps')

    def __str__(self):
        return self.name

class Machinery(models.Model):
    name = models.CharField(max_length=100)
    identnum = models.CharField(max_length=10, unique=True)
    wday = models.DateField(auto_now_add=True)
    buyday = models.DateField(null=False)
    run_unit = models.CharField(max_length=10)
    run_hist = models.IntegerField(null=True)
    fuel = models.CharField(max_length=10)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='machinerys')

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    wday = models.DateField(auto_now_add=True)
    startday = models.DateField()
    email = models.EmailField(max_length=254, unique=True)
    user = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE, related_name='drivers')

    def __str__(self):
        return self.name

class Fueling(models.Model):
    ftime = models.DateTimeField(auto_now_add=True)
    kmeter = models.IntegerField(null=True)
    liter =  models.SmallIntegerField()
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE, related_name='fuelings')

    

class OilChange(models.Model):
    ftime = models.DateTimeField(auto_now_add=True)
    kmeter = models.IntegerField(null=True)
    liter =  models.SmallIntegerField()
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE, related_name='oilchanges')

    

class Runing(models.Model):
    wtype = models.CharField(max_length=10)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_kmeter = models.IntegerField(null=True)
    end_kmeter = models.IntegerField(null=True)
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE, related_name='runings')

    

class OilSample(models.Model):
    minta_azonosito = models.CharField(max_length=10, unique=True)
    beerkezes_napja = models.DateField()
    mintaveetel_napja = models.DateField()
    viszkozitas_valtozas = models.SmallIntegerField(null=True)
    koromtartalom = models.FloatField(null=True)
    osszulledek = models.SmallIntegerField(null=True)
    vasm_osszulledek = models.SmallIntegerField(null=True)
    vastartalom = models.SmallIntegerField(null=True)
    viztartalom = models.FloatField(null=True)
    illoanyag = models.FloatField(null=True)
    lobbanaspont = models.SmallIntegerField(null=True)
    kep1 = models.ImageField(height_field=300, null=True)
    kep2 = models.ImageField(height_field=300, null=True)
    kep3 = models.ImageField(height_field=300, null=True)
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE, related_name='oilsamples')

    def __str__(self):
        return self.minta_azonosito


class AdminList(models.Model):
    user = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    comp = models.IntegerField(null=True)
    mach = models.IntegerField(null=True)
    samp = models.IntegerField(null=True)
    lead = models.IntegerField(null=True)

    def __str__(self):
        return self.user
