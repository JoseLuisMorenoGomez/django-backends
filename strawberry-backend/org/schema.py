import strawberry
from strawberry.extensions.query_depth_limiter import QueryDepthLimiter
from typing import List

from .types import *
from .resolvers.departmet_resolver import *
from .resolvers.position_resolver  import *
from .models import *


@strawberry.type
class Query:
#### Deparments

    @strawberry.field
    def subdepartments(id:int) -> List[OrgDepartmentType]:
        return resolve_subdepartments(id)

   
    @strawberry.field
    def departmentById(id:int) -> OrgDepartmentType:
        
        return resolve_department_hierarchy(id)
    


### Positions

    @strawberry.field
    def positionsList(self) -> List[OrgPositionType]:   
        return resolve_all_positions()
    
    @strawberry.field
    def positionById(self, id:int) -> OrgPositionType:   
        return resolve_position_by_id(id)
    
schema = strawberry.Schema(query=Query, extensions=[QueryDepthLimiter(4)],)
