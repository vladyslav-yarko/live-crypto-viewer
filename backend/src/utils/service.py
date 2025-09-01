from typing import Optional, Union
import uuid


class Service:
    def __init__(
        self,
        session: Optional[AsyncSession] = None
        ):
        self.repo = None
    
    async def get(self, page: Optional[int], **kwargs) -> Union[dict, tuple[int, str]]:
        full_data = await self.repo(self.session).get(page, **kwargs)
        data, total, offset = full_data
        count = len(data)
        has_next = False
        if page is not None:
            has_next = (page * offset) < total
        res = {
            "data": data,
            "page": page,
            "count": count,
            "total": total,
            "hasNext": has_next
        }
        return res
    
    async def get_one(self, id: Union[int, uuid.UUID]) -> Union[Base, tuple[int, str]]:
        data = await self.repo(self.session).get_one_by_id(id)
        if not data:
            data = (422, "Id has not found")
        return data
    
    async def create_one(self, data: dict) -> dict:
        obj = await self.repo(self.session).create_one(**data)
        return obj.to_dict()
    
    async def update_one(self, id: Union[int, uuid.UUID], data: dict) -> Union[dict, tuple[int, str]]:
        obj = await self.get_one(id)
        if isinstance(obj, tuple):
            return obj
        obj = await self.repo(self.session).update_one(id, **data)
        return obj.to_dict()
    
    async def delete_one(self, id: Union[int, uuid.UUID]) -> Union[dict, tuple[int, str]]:
        obj = await self.get_one(id)
        if isinstance(obj, tuple):
            return obj
        obj = await self.repo(self.session).delete_one(id)
        return obj.to_dict()
