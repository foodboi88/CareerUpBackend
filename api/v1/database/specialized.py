from sqlalchemy import Column, ForeignKey, Integer, String, Text

from .base import Base, Crud


class SpecializedCrud(Crud, Base):
    __tablename__ = "specialized"

    id = Column(String(255), primary_key=True)
    specialized_name = Column(String(255))
    specialized_description = Column(Text)
    personality_type_id = Column(String(255))
    cluster = Column(Integer)
    branch_id = Column(String(255), ForeignKey("branch.id"))

    @classmethod
    async def find_all_by_personality(cls, personality: str):
        return await cls.fetch_all(
            cls.select()
                .where(cls.personality_type_id == personality)
        )

    @classmethod
    async def find_all_by_cluster_and_branch_id(cls, cluster: int, branch_id: str, id: str):
        return await cls.fetch_all(
            cls.select()
                .where(cls.cluster == cluster)
                .where(cls.branch_id == branch_id)
                .where(cls.id != id)
        )
