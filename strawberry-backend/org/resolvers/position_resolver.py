# position_resolver.py

from ..models import OrgPosition
import strawberry


@strawberry.field
def resolve_all_positions():
    return OrgPosition.objects.all()

@strawberry.field
def resolve_position_by_id(id:int):
    return OrgPosition.objects.filter(id=id).first()   
 