import strawberry
from strawberry.django import auto

# Import your Django models
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

# Define your Strawberry types
@strawberry.type
class OrgDepartmentType(auto.ModelType):
    class Meta:
        model = OrgDepartment

@strawberry.type
class OrgPersonnelGroupType(auto.ModelType):
    class Meta:
        model = OrgPersonnelGroup

@strawberry.type
class OrgTypeofPersonnelType(auto.ModelType):
    class Meta:
        model = OrgTypeofPersonnel

@strawberry.type
class OrgPosCategoryType(auto.ModelType):
    class Meta:
        model = OrgPosCategory

@strawberry.type
class OrgDeptCategoryType(auto.ModelType):
    class Meta:
        model = OrgDeptCategory

@strawberry.type
class OrgPositionType(auto.ModelType):
    class Meta:
        model = OrgPosition

@strawberry.type
class OrgProvisionProcedureType(auto.ModelType):
    class Meta:
        model = OrgProvisionProcedure

@strawberry.type
class OrgQualificationsType(auto.ModelType):
    class Meta:
        model = OrgQualifications

@strawberry.type
class OrgRemunerationItemType(auto.ModelType):
    class Meta:
        model = OrgRemunerationItem

@strawberry.type
class OrgSalaryStructureType(auto.ModelType):
    class Meta:
        model = OrgSalaryStructure

# Define your queries
@strawberry.type
class Query:
    @strawberry.field
    def get_org_department(self, id: strawberry.ID) -> OrgDepartmentType:
        return OrgDepartment.objects.get(id=id)

    @strawberry.field
    def get_org_position(self, id: strawberry.ID) -> OrgPositionType:
        return OrgPosition.objects.get(id=id)

    # Add more queries for other models as needed

# Create your schema
schema = strawberry.Schema(query=Query)
