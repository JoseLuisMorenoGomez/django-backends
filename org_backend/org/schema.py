# schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import OrgPersonnel, OrgDepartment, OrgDeptCategory, OrgPersonnelGroup, OrgPosCategory, OrgPosition, OrgProvisionProcedure, OrgQualifications, OrgRemunerationItem, OrgSalaryStructure, OrgScale, OrgTypeofPersonnel

class OrgPersonnelType(DjangoObjectType):
    class Meta:
        model = OrgPersonnel

class OrgDepartmentType(DjangoObjectType):
    class Meta:
        model = OrgDepartment

class OrgDeptCategoryType(DjangoObjectType):
    class Meta:
        model = OrgDeptCategory

class OrgPersonnelGroupType(DjangoObjectType):
    class Meta:
        model = OrgPersonnelGroup

class OrgPosCategoryType(DjangoObjectType):
    class Meta:
        model = OrgPosCategory

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

class OrgScaleType(DjangoObjectType):
    class Meta:
        model = OrgScale

class OrgTypeofPersonnelType(DjangoObjectType):
    class Meta:
        model = OrgTypeofPersonnel
        
class ManagerInfoType(graphene.ObjectType):
    department_name = graphene.String()
    manager_name = graphene.String()
    manager_image_url = graphene.String()
        
        

class Query(graphene.ObjectType):
    all_org_personnel = graphene.List(OrgPersonnelType)
    all_org_department = graphene.List(OrgDepartmentType)
    all_org_dept_category = graphene.List(OrgDeptCategoryType)
    all_org_personnel_group = graphene.List(OrgPersonnelGroupType)
    all_org_pos_category = graphene.List(OrgPosCategoryType)
    all_org_position = graphene.List(OrgPositionType)
    all_org_provision_procedure = graphene.List(OrgProvisionProcedureType)
    all_org_qualifications = graphene.List(OrgQualificationsType)
    all_org_remuneration_item = graphene.List(OrgRemunerationItemType)
    all_org_salary_structure = graphene.List(OrgSalaryStructureType)
    all_org_scale = graphene.List(OrgScaleType)
    all_org_typeof_personnel = graphene.List(OrgTypeofPersonnelType)

    def resolve_all_org_personnel(self, info):
        return OrgPersonnel.objects.all()

    def resolve_all_org_department(self, info):
        return OrgDepartment.objects.all()

    def resolve_all_org_dept_category(self, info):
        return OrgDeptCategory.objects.all()

    def resolve_all_org_personnel_group(self, info):
        return OrgPersonnelGroup.objects.all()

    def resolve_all_org_pos_category(self, info):
        return OrgPosCategory.objects.all()

    def resolve_all_org_position(self, info):
        return OrgPosition.objects.all()

    def resolve_all_org_provision_procedure(self, info):
        return OrgProvisionProcedure.objects.all()

    def resolve_all_org_qualifications(self, info):
        return OrgQualifications.objects.all()

    def resolve_all_org_remuneration_item(self, info):
        return OrgRemunerationItem.objects.all()

    def resolve_all_org_salary_structure(self, info):
        return OrgSalaryStructure.objects.all()

    def resolve_all_org_scale(self, info):
        return OrgScale.objects.all()

    def resolve_all_org_typeof_personnel(self, info):
        return OrgTypeofPersonnel.objects.all()

    
    #Fields
    
    org_personnel_by_id = graphene.Field(OrgPersonnelType, id=graphene.Int())
    org_department_by_id = graphene.Field(OrgDepartmentType, id=graphene.Int())
    org_dept_category_by_id = graphene.Field(OrgDeptCategoryType, id=graphene.Int())
    org_personnel_group_by_id = graphene.Field(OrgPersonnelGroupType, id=graphene.Int())
    org_pos_category_by_id = graphene.Field(OrgPosCategoryType, id=graphene.Int())
    org_position_by_id = graphene.Field(OrgPositionType, id=graphene.Int())
    org_provision_procedure_by_id = graphene.Field(OrgProvisionProcedureType, id=graphene.Int())
    org_qualifications_by_id = graphene.Field(OrgQualificationsType, id=graphene.Int())
    org_remuneration_item_by_id = graphene.Field(OrgRemunerationItemType, id=graphene.Int())
    org_salary_structure_by_id = graphene.Field(OrgSalaryStructureType, id=graphene.Int())
    org_scale_by_id = graphene.Field(OrgScaleType, id=graphene.Int())
    org_typeof_personnel_by_id = graphene.Field(OrgTypeofPersonnelType, id=graphene.Int())

    def resolve_org_personnel_by_id(self, info, id):
        return OrgPersonnel.objects.get(pk=id)

    def resolve_org_department_by_id(self, info, id):
        return OrgDepartment.objects.get(pk=id)

    def resolve_org_dept_category_by_id(self, info, id):
        return OrgDeptCategory.objects.get(pk=id)

    def resolve_org_personnel_group_by_id(self, info, id):
        return OrgPersonnelGroup.objects.get(pk=id)

    def resolve_org_pos_category_by_id(self, info, id):
        return OrgPosCategory.objects.get(pk=id)

    def resolve_org_position_by_id(self, info, id):
        return OrgPosition.objects.get(pk=id)

    def resolve_org_provision_procedure_by_id(self, info, id):
        return OrgProvisionProcedure.objects.get(pk=id)

    def resolve_org_qualifications_by_id(self, info, id):
        return OrgQualifications.objects.get(pk=id)

    def resolve_org_remuneration_item_by_id(self, info, id):
        return OrgRemunerationItem.objects.get(pk=id)

    def resolve_org_salary_structure_by_id(self, info, id):
        return OrgSalaryStructure.objects.get(pk=id)

    def resolve_org_scale_by_id(self, info, id):
        return OrgScale.objects.get(pk=id)

    def resolve_org_typeof_personnel_by_id(self, info, id):
        return OrgTypeofPersonnel.objects.get(pk=id)
    
#   Complex queries 
    
    manager_info_for_department = graphene.Field(ManagerInfoType, department_id=graphene.Int())

    def resolve_manager_info_for_department(self, info, department_id):
        try:
            department = OrgDepartment.objects.get(pk=department_id)
 
            # Get the manager position for the specified department
            manager_position = OrgPosition.objects.get(id__isnull=False, orgdepartment=department)
            
            # Get the personnel occupying the manager position
            manager_personnel = OrgPersonnel.objects.get(current_position=manager_position)

            return ManagerInfoType(
                department_name=department.name,
                manager_name=manager_personnel.name,
                manager_image_url=manager_personnel.image_url
            )
        except OrgPosition.DoesNotExist or OrgPersonnel.DoesNotExist or OrgDepartment.DoesNotExist:
            return None

    managers_info_for_all_departments = graphene.List(ManagerInfoType)

    def resolve_managers_info_for_all_departments(self, info):
        manager_info_list = []

        # Get all departments
        departments = OrgDepartment.objects.all()

        for department in departments:
            # Call the manager_info_for_department resolver for each department
            manager_info = self.resolve_manager_info_for_department(info, department.id)

            # Add manager info to the list
            if manager_info:
                manager_info_list.append(manager_info)

        return manager_info_list

schema = graphene.Schema(query=Query)