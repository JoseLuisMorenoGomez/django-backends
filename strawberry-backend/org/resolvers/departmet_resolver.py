# department_resolvers.py
from ..models import OrgDepartment
from ..types import OrgDepartmentType

  
def resolve_subdepartments(id):
      department = OrgDepartment.objects.filter(id=id)
      return OrgDepartment.objects.filter(parent=department)


department_hierarchy: OrgDepartmentType

def resolve_department_hierarchy(department_id: int):
    
        def build_department_structure(department):
            subdepartments = OrgDepartment.objects.filter(parent=department)
            subdepartment_nodes = [build_department_structure(sub) for sub in subdepartments]
            return OrgDepartmentType(id=department.id, name=department.name,  parent=department.parent, manager_position=department.manager_position, category=department.category, subdepartments=subdepartment_nodes)

        # Obtén el departamento raíz a partir del ID proporcionado
        my_department = OrgDepartment.objects.get(id=department_id)

        # Construye la estructura jerárquica a partir del nodo raíz
        return build_department_structure(my_department)




    

