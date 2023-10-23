import graphene
from graphene_django.types import DjangoObjectType
from .models import (
    OrgDepartment,
    OrgPersonnelGroup,
    OrgTypeofPersonnel,
    OrgPosCategory,
    OrgDeptCategory,
    OrgPosition,
    OrgProvisionProcedure,
    OrgQualifications,
    OrgRemunerationItem,
    OrgSalaryStructure,
)

class OrgDepartmentType(DjangoObjectType):
    class Meta:
        model = OrgDepartment

class OrgPersonnelGroupType(DjangoObjectType):
    class Meta:
        model = OrgPersonnelGroup

class OrgTypeofPersonnelType(DjangoObjectType):
    class Meta:
        model = OrgTypeofPersonnel

class OrgPosCategoryType(DjangoObjectType):
    class Meta:
        model = OrgPosCategory

class OrgDeptCategoryType(DjangoObjectType):
    class Meta:
        model = OrgDeptCategory

class OrgPositionType(DjangoObjectType):
    class Meta:
        model = OrgPosition

class OrgProvisionProcedureType(DjangoObjectType):
    class Meta:
        model = OrgProvisionProcedure

class OrgQualificationsType(DjangoObjectType):
    class Meta:
        model = OrgQualifications

class OrgRemunerationItemType(DjangoObjectType):
    class Meta:
        model = OrgRemunerationItem

class OrgSalaryStructureType(DjangoObjectType):
    class Meta:
        model = OrgSalaryStructure

class Query(graphene.ObjectType):
    
    #Lists
    
    all_org_departments = graphene.List(OrgDepartmentType)
    all_org_personnel_groups = graphene.List(OrgPersonnelGroupType)
    all_org_typeof_personnel = graphene.List(OrgTypeofPersonnelType)
    all_org_pos_categories = graphene.List(OrgPosCategoryType)
    all_org_dept_categories = graphene.List(OrgDeptCategoryType)
    all_org_positions = graphene.List(OrgPositionType)
    all_org_provision_procedures = graphene.List(OrgProvisionProcedureType)
    all_org_qualifications = graphene.List(OrgQualificationsType)
    all_org_remuneration_items = graphene.List(OrgRemunerationItemType)
    all_org_salary_structures = graphene.List(OrgSalaryStructureType)
    
 
    def resolve_all_org_departments(self, info):
        return OrgDepartment.objects.all()

    def resolve_all_org_personnel_groups(self, info):
        return OrgPersonnelGroup.objects.all()

    def resolve_all_org_personnel_types(self, info):
        return OrgTypeofPersonnel.objects.all()

    def resolve_all_org_pos_categories(self, info):
        return OrgPosCategory.objects.all()

    def resolve_all_org_dept_categories(self, info):
        return OrgDeptCategory.objects.all()

    def resolve_all_org_positions(self, info):
        return OrgPosition.objects.all()

    def resolve_all_org_provision_procedures(self, info):
        return OrgProvisionProcedure.objects.all()

    def resolve_all_org_qualifications(self, info):
        return OrgQualifications.objects.all()

    def resolve_all_org_remuneration_items(self, info):
        return OrgRemunerationItem.objects.all()

    def resolve_all_org_salary_structures(self, info):
        return OrgSalaryStructure.objects.all()
    
   
    
    #Fields
    
    org_department = graphene.Field(OrgDepartmentType, id=graphene.ID(required=True))
    org_position = graphene.Field(OrgPositionType, id=graphene.ID(required=True))
    org_pos_category = graphene.Field(OrgPosCategoryType, id=graphene.ID(required=True))
    org_dept_category = graphene.Field(OrgDeptCategoryType, id=graphene.ID(required=True))
    
    def resolve_org_department(self, info, id):
        return OrgDepartment.objects.get(id=id)
    
    def resolve_org_position(self, info, id):
        return OrgPosition.objects.get(id=id)
    
    def resolve_org_pos_category(self, info, id):
        return OrgPosCategory.objects.get(id=id)
    
    def resolve_oreg_dept_category(self, info, id):
        return OrgDeptCategory.objects.get(id=id)
    

schema = graphene.Schema(query=Query)
