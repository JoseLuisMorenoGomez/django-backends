import strawberry
from typing import List

@strawberry.type
class OrgDepartmentType:
    id: strawberry.ID
    name: str
    parent: 'OrgDepartmentType'   
    manager_position: 'OrgPositionType'   
    category: 'OrgDeptCategoryType'
    subdepartments: List['OrgDepartmentType']
    
@strawberry.type
class OrgPersonnelGroupType:
    id: strawberry.ID
    name: str
    code: str

@strawberry.type
class OrgTypeofPersonnelType:
    id: strawberry.ID
    name: str

@strawberry.type
class OrgPosCategoryType:
    id: strawberry.ID
    name: str

@strawberry.type
class OrgDeptCategoryType:
    id: strawberry.ID
    name: str

@strawberry.type
class OrgPositionType:
    id: strawberry.ID
    name: str
    category: 'OrgPosCategoryType' 
    is_singularized: bool
    salary_structure: 'OrgSalaryStructureType' 
    typeof_personnel: 'OrgTypeofPersonnelType' 
    provision_procedure: 'OrgProvisionProcedureType' 
    is_idle: bool
    personnel_group: 'OrgPersonnelGroupType' 
    qualification: 'OrgQualificationsType' 
    code: str

@strawberry.type
class OrgProvisionProcedureType:
    id: strawberry.ID
    name: str
    code: str

@strawberry.type
class OrgQualificationsType:
    id: strawberry.ID
    name: str
    code: str

@strawberry.type
class OrgRemunerationItemType:
    id: strawberry.ID
    name: str

@strawberry.type
class OrgSalaryStructureType:
    id: strawberry.ID
    position_id: int
    remuneration_item: 'OrgRemunerationItemType' 
    from_date: str
    to_date: str
    amount: int

