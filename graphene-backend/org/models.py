# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class OrgDepartment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    manager_position = models.ForeignKey('OrgPosition', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('OrgDeptCategory', models.DO_NOTHING, blank=True, null=True)
 
    class Meta:
        managed = False
        db_table = 'org_department'
        
    def __str__(self):
        return self.name

class OrgPersonnelGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_personnel_group'
  
    def __str__(self):
        return self.name

class OrgTypeofPersonnel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_typeof_personnel'

    def __str__(self):
        return self.name

class OrgPosCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'org_pos_category'

    def __str__(self):
        return self.name

class OrgDeptCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'org_dept_category'

    def __str__(self):
        return self.name
    
class OrgPosition(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(OrgPosCategory, models.DO_NOTHING)
    is_singularized = models.BooleanField()
    salary_structure = models.ForeignKey('OrgSalaryStructure', models.DO_NOTHING, blank=True, null=True)
    typeof_personnel = models.ForeignKey('OrgTypeofPersonnel', models.DO_NOTHING, blank=True, null=True)
    provision_procedure = models.ForeignKey('OrgProvisionProcedure', models.DO_NOTHING)
    is_idle = models.BooleanField()
    personnel_group = models.ForeignKey(OrgPersonnelGroup, models.DO_NOTHING)
    qualification = models.ForeignKey('OrgQualifications', models.DO_NOTHING)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_position'


class OrgProvisionProcedure(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_provision_procedure'


class OrgQualifications(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_qualifications'


class OrgRemunerationItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_remuneration_item'


class OrgSalaryStructure(models.Model):
    id = models.IntegerField(primary_key=True)
    position_id = models.IntegerField(unique=True)
    remuneration_item = models.ForeignKey(OrgRemunerationItem, models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_salary_structure'
