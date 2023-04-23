from pydantic import BaseModel

class ApartTransactionDto(BaseModel):
    law_dong_cd: str
    si_do_nm: str
    si_gun_gu_nm: str
    eup_myeon_dong_nm: str
    ri_nm: str
    law_dong_rank: str
