from pydantic import BaseModel


class AuctionMaster(BaseModel):
    jiwonNm: str
    jiwonNmEnc: str
    saNo: str

    def __hash__(self):
        return hash((self.jiwonNm, self.jiwonNmEnc, self.saNo))

