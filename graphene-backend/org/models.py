from django.db import models
class OrgPersonnel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    current_position = models.ForeignKey('OrgPosition', models.DO_NOTHING, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org-personnel'

class OrgDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    manager_position = models.ForeignKey('OrgPosition', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('OrgDeptCategory', models.DO_NOTHING, blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_department'


class OrgDeptCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_implemented = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'org_dept_category'


class OrgPersonnelGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_personnel_group'


class OrgPosCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'org_pos_category'


class OrgPosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(OrgPosCategory, models.DO_NOTHING)
    is_singularized = models.BooleanField()
    salary_structure = models.ForeignKey('OrgSalaryStructure', models.DO_NOTHING, to_field='position_id', blank=True, null=True)
    typeof_personnel = models.ForeignKey('OrgTypeofPersonnel', models.DO_NOTHING)
    provision_procedure = models.ForeignKey('OrgProvisionProcedure', models.DO_NOTHING, db_comment='Selection process what candidates are submitted to')
    is_idle = models.BooleanField()
    personnel_group = models.ForeignKey(OrgPersonnelGroup, models.DO_NOTHING)
    qualification = models.ForeignKey('OrgQualifications', models.DO_NOTHING, db_comment='universitary degree or professional skills requiered for the position')
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_position'
        db_table_comment = 'Positions that make up the department'


class OrgProvisionProcedure(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_provision_procedure'


class OrgQualifications(models.Model):
    id = models.BigAutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_qualifications'


class OrgRemunerationItem(models.Model):
    id = models.BigAutoField(primary_key=True, blank=True, null=False)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_remuneration_item'


class OrgSalaryStructure(models.Model):
    id = models.BigAutoField(primary_key=True)
    position_id = models.BigIntegerField(unique=True)
    remuneration_item = models.ForeignKey(OrgRemunerationItem, models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_salary_structure'

class OrgScale(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=5)
    description = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'org_scale'


class OrgTypeofPersonnel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_typeof_personnel'
        db_table_comment = 'Funcionario, Laboral, Eventual, Directivo, Funcionario con habilitación especial'


